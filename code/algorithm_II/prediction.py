import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict
from datetime import datetime

# read in tianchi_mobile_recommend_train_user.csv
train_data = pd.read_csv('F:/activities/tianchi_mobile_recommend_train_user.csv')

# read in potential user list
user = pd.read_csv('F:/activities/TianChi_TeamPSU/data/algorithm_II/cleaned_user_behavior_statistics.csv')
user_list = user.user_id

# read in potential item list
item = pd.read_csv('F:/activities/TianChi_TeamPSU/data/tianchi_mobile_train_item.csv')

# open prediction file
file_prediction = csv.writer(open('F:/activities/TianChi_TeamPSU/data/algorithm_II/prediction.csv', 'wb'))
file_prediction.writerow(['user_id', 'item_id', 'PC1', 'PC2', 'prediction'])

for usr in user_list:
    for i in range(0, len(item)):
        itm = item.item_id.values[i]
        catg = item.item_category.values[i]
        usr_data = train_data[train_data.user_id == usr]
        usr_itm_data = usr_data[usr_data.item_id == itm]
        usr_catg_data = usr_data[usr_data.item_category == catg]
        
        # do some cleaning
        if len(usr_itm_data) == 0:
            continue
        if len(usr_catg_data) == 0:
            continue
        if len(usr_itm_data[usr_itm_data.behavior_type == 4]) > 0:
            continue
        
        # attributes
        bh_1_itm = len(usr_itm_data[usr_itm_data.behavior_type == 1])
        bh_2_itm = len(usr_itm_data[usr_itm_data.behavior_type == 2])
        bh_3_itm = len(usr_itm_data[usr_itm_data.behavior_type == 3])
        
        bh_1_catg = len(usr_catg_data[usr_catg_data.behavior_type == 1])
        bh_2_catg = len(usr_catg_data[usr_catg_data.behavior_type == 2])
        bh_3_catg = len(usr_catg_data[usr_catg_data.behavior_type == 3])
        
        sml_set = set(usr_catg_data.item_id).difference(set([itm]))
        bh_1_sml = 0
        bh_2_sml = 0
        bh_3_sml = 0
        
        for sml_itm in sml_set:
            sml_itm_data = usr_catg_data[usr_catg_data.item_id == sml_itm]
            bh_1_sml = bh_1_sml + len(sml_itm_data[sml_itm_data.behavior_type == 1])
            bh_2_sml = bh_2_sml + len(sml_itm_data[sml_itm_data.behvaior_type == 2])
            bh_3_sml = bh_3_sml + len(sml_itm_data[sml_itm_data.behavior_type == 3])
            
        if len(sml_set) != 0:
            bh_1_sml = bh_1_sml / len(sml_set)
            bh_2_sml = bh_2_sml / len(sml_set)
            bh_3_sml = bh_3_sml / len(sml_set)
            
        begn_time = min(usr_itm_data.time)
        delta = datetime.strptime('2014-12-19', '%Y-%m-%d') - datetime.strptime(begn_time, '%Y-%m-%d')
        bh_len = delta.days + 1
        
        # center and scale attributes
        [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10] = [6.53875791, 0.12418482, 0.68109557, 31.69704902, 0.58156500,\
                                                     1.52230815, 2.02866391, 0.03115706, 0.10885471, 2.11924332]
        [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10] = [2.754703, 0.2075941, 0.4787845, 29.99228, 1.426054, 1.579553,\
                                                     0.7027484, 0.06459551, 0.1314128, 1.380503]
        z_bh_1_itm = (bh_1_itm - m1) / s1
        z_bh_2_itm = (bh_2_itm - m2) / s2
        z_bh_3_itm = (bh_3_itm - m3) / s3
        
        z_bh_1_catg = (bh_1_catg - m4) / s4
        z_bh_2_catg = (bh_2_catg - m5) / s5
        z_bh_3_catg = (bh_3_catg - m6) / s6
        
        z_bh_1_sml = (bh_1_sml - m7) / s7
        z_bh_2_sml = (bh_2_sml - m8) / s8
        z_bh_3_sml = (bh_3_sml - m9) / s9
        
        z_bh_len = (bh_len - m10) / s10
        
        # PC scores
        PC1 = -0.4072042*z_bh_1_itm - 0.2641443*z_bh_2_itm - 0.2914348*z_bh_3_itm - 0.3963483*z_bh_1_catg -\
              0.3196858*z_bh_2_catg - 0.3181409*z_bh_3_catg - 0.3552390*z_bh_1_sml - 0.2538538*z_bh_2_sml -\
              0.1606399*z_bh_3_sml - 0.3202060*z_bh_len
        PC2 = -0.04086871*z_bh_1_itm - 0.44231264*z_bh_2_itm + 0.39787698*z_bh_3_itm - 0.03131084*z_bh_1_catg -\
              0.37226067*z_bh_2_catg + 0.41263706*z_bh_3_catg + 0.08421064*z_bh_1_sml - 0.38557650*z_bh_2_sml +\
              0.41895031*z_bh_3_sml + 0.05723137*z_bh_len
                
        # prediction 
        prediction = 0
        if PC1 > - 0.8333 and PC2 > - 1 and PC1 + PC2 - 2 < 0:
            prediction = 1
        
        file_prediction.writerow([usr, itm, PC1, PC2, prediction])

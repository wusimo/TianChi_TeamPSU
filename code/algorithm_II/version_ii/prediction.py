def user_item_attributes(usr_itm_data, usr_catg_data):
    
    bh_1_itm = bh_2_itm = bh_3_itm = []
    bh_1_catg = bh_2_catg = bh_3_catg = []
    bh_1_sml = bh_2_sml = bh_3_sml = []
    cycle = []
    
    bh_1_itm = float(len(usr_itm_data[usr_itm_data.behavior_type == 1]))
    bh_2_itm = float(len(usr_itm_data[usr_itm_data.behavior_type == 2]))
    bh_3_itm = float(len(usr_itm_data[usr_itm_data.behavior_type == 3]))
    
    bh_1_catg = float(len(usr_catg_data[usr_catg_data.behavior_type == 1]))
    bh_2_catg = float(len(usr_catg_data[usr_catg_data.behavior_type == 2]))
    bh_3_catg = float(len(usr_catg_data[usr_catg_data.behavior_type == 3]))
    
    itm = usr_itm_data.item_id.values[0]
    sml_set = set(usr_catg_data.item_id).difference(set([itm]))
    
    if len(sml_set) == 0:
        bh_1_sml = bh_2_sml = bh_3_sml = 0.0
    else:
        bh_1_sml = (bh_1_catg - bh_1_itm) / len(sml_set)
        bh_2_sml = (bh_2_catg - bh_2_itm) / len(sml_set)
        bh_3_sml = (bh_3_catg - bh_3_itm) / len(sml_set)
    
    bgn_bh_time = min(usr_itm_data.time_difference)
    bgn_bh_data = usr_itm_data[usr_itm_data.time_difference == bgn_bh_time]
    bgn_bh_date_str = bgn_bh_data.time.values[0][0:10]
    bgn_bh_date = datetime.strptime(bgn_bh_date_str, '%Y-%m-%d')
    ref_date = datetime.strptime('2014-12-19', '%Y-%m-%d')
    
    cycle = float((ref_date - bgn_bh_date).days + 1)
    return([bh_1_itm, bh_2_itm, bh_3_itm, bh_1_catg, bh_2_catg, bh_3_catg,\
            bh_1_sml, bh_2_sml, bh_3_sml, cycle])

def usr_item_princomp(att):
    [m_1_itm, m_2_itm, m_3_itm] = [5.7555680, 0.1997837, 0.6311102]
    [m_1_catg, m_2_catg, m_3_catg] = [38.5381298, 0.8879383, 1.5610360]
    [m_1_sml, m_2_sml, m_3_sml] = [2.5680700, 0.0519341, 0.1316246]
    m_cycle = 5.6488279
    
    [s_1_itm, s_2_itm, s_3_itm] = [3.2568950, 0.3119098, 0.4850263]
    [s_1_catg, s_2_catg, s_3_catg] = [44.1866186, 2.0628901, 2.0415250]
    [s_1_sml, s_2_sml, s_3_sml] = [0.8320718, 0.1033156, 0.1741298]
    s_cycle = 3.1528194
    
    [c1_1_itm, c1_2_itm, c1_3_itm] = [0.10951815, 0.49251711, -0.36971803]
    [c1_1_catg, c1_2_catg, c1_3_catg] = [0.15485697, 0.42548986, -0.29311532]
    [c1_1_sml, c1_2_sml, c1_3_sml] = [0.03850667, 0.42663047, -0.35644810]
    c1_cycle = 0.08515158
    
    [c2_1_itm, c2_2_itm, c2_3_itm] = [-0.45210565, -0.09718716, -0.35541942]
    [c2_1_catg, c2_2_catg, c2_3_catg] = [-0.45764596, -0.25623531, -0.45844107]
    [c2_1_sml, c2_2_sml, c2_3_sml] = [-0.25303797, -0.09091449, -0.22312720]
    c2_cycle = -0.22910300
    
    [bh_1_itm, bh_2_itm, bh_3_itm] = att[0:3]
    [bh_1_catg, bh_2_catg, bh_3_catg] = att[3:6]
    [bh_1_sml, bh_2_sml, bh_3_sml] = att[6:9]
    cycle = att[9]
    
    [z_1_itm, z_2_itm, z_3_itm] = [(bh_1_itm - m_1_itm)/s_1_itm, (bh_2_itm - m_2_itm)/s_2_itm, (bh_3_itm - m_3_itm)/s_3_itm]
    [z_1_catg, z_2_catg, z_3_catg] = [(bh_1_catg - m_1_catg)/s_1_catg, (bh_2_catg - m_2_catg)/s_2_catg, (bh_3_catg - m_3_catg)/s_3_catg]
    [z_1_sml, z_2_sml, z_3_sml] = [(bh_1_sml - m_1_sml)/s_1_sml, (bh_2_sml - m_2_sml)/s_2_sml, (bh_3_sml - m_3_sml)/s_3_sml]
    z_cycle = (cycle - m_cycle)/s_cycle
    
    PC1 = c1_1_itm*z_1_itm + c1_2_itm*z_2_itm + c1_3_itm*z_3_itm + c1_1_catg*z_1_catg + c1_2_catg*z_2_catg +\
          c1_3_catg*z_3_catg + c1_1_sml*z_1_sml + c1_2_sml*z_2_sml +c1_3_sml*z_3_sml + c1_cycle*z_cycle
                            
    PC2 = c2_1_itm*z_1_itm + c2_2_itm*z_2_itm + c2_3_itm*z_3_itm + c2_1_catg*z_1_catg + c2_2_catg*z_2_catg +\
          c2_3_catg*z_3_catg + c2_1_sml*z_1_sml + c2_2_sml*z_2_sml +c2_3_sml*z_3_sml + c2_cycle*z_cycle
    
    return([PC1, PC2])
    

    
## MAIN BODY 
#
#
import pandas as pd
import numpy as np
import csv
from datetime import datetime
from datetime import timedelta

# read in ref_set
ref_data = pd.read_csv('F:/activities/TianChi/data/ref_set.csv')
ref_num = len(ref_data)

# read in cleaned train data
train_data = pd.read_csv('F:/activities/TianChi/data/cleaned_tianchi_mobile_recommend_train_user.csv')
poten_user_set = set(train_data.user_id)  

# prediction set
pred_data = csv.writer(open('F:/activities/TianChi/data/pred_set.csv', 'wb'))
pred_data.writerow(['user_id', 'item_id', 'PC1', 'PC2', 'prediction'])

for i in range(0, ref_num):
    print i
    
    usr = ref_data.user_id.values[i]
    itm = ref_data.item_id.values[i]
    
    # get the attributes
    if usr not in poten_user_set:
        continue
        
    usr_data = train_data[train_data.user_id == usr]
    
    usr_itm_data = usr_data[usr_data.item_id == itm]
    if len(usr_itm_data) == 0:
        continue
        
    usr_itm_bgt_data = usr_itm_data[usr_itm_data.behavior_type == 4]
    if len(usr_itm_bgt_data) > 0:
        continue
    
    catg = usr_itm_data.item_category.values[0]
    usr_catg_data = usr_data[usr_data.item_category == catg]
    usr_catg_bgt_data = usr_catg_data[usr_catg_data.behavior_type == 4]
    if len(usr_catg_bgt_data) > 0:
        continue
    

    att = user_item_attributes(usr_itm_data, usr_catg_data)
    [PC1, PC2] = usr_item_princomp(att)
    
    pred_data.writerow([usr, itm] + [PC1, PC2])
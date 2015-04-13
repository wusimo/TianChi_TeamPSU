import pandas as pd
import numpy as np
import csv
import time
from datetime import datetime

# read in tianchi_mobile_recommend_train_user.csv
orgn_data = pd.read_csv('F:/activities/TianChi/data/tianchi_mobile_recommend_train_user.csv')


# cleaned data file
clnd_data = csv.writer(open('F:/activities/TianChi/data/cleaned_tianchi_mobile_recommend_train_user.csv', 'wb'))
clnd_data.writerow(['user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category', 'time', 'time_difference'])

# clean original data
# 1. inactive user(bought less than 10 different items in normal days after 2014-11-22 00) are eliminated
# 2. sort the data by user_id, item_category, and time


# get the time difference to 2014-01-01 00
orgn_data["timdiff"] = 0.0
for i in range(0, len(orgn_data)):
    record_time = time.strptime(orgn_data.time.values[i], '%Y-%m-%d %H')
    orgn_data.timdiff.values[i] = (record_time.tm_yday - 1) * 24 + record_time.tm_hour
    
# sort the data by time
orgn_data = orgn_data.sort_index(by=['user_id', 'item_category', 'timdiff'], ascending = [1, 1, 1])

# eliminate inactive user
ignr_lft = (time.strptime('2014-11-21 23', '%Y-%m-%d %H')).tm_yday * 24

dbl_12_lft = (time.strptime('2014-12-11 23', '%Y-%m-%d %H')).tm_yday * 24
dbl_12_rgt = (time.strptime('2014-12-12 23', '%Y-%m-%d %H')).tm_yday * 24
dbl_12_11_lft = (time.strptime('2014-12-10 23', '%Y-%m-%d %H')).tm_yday * 24

ref_lft = (time.strptime('2014-12-17 23', '%Y-%m-%d %H')).tm_yday * 24

user_set = set(orgn_data.user_id)

flag = 1
for usr in user_set:
    print flag
    flag = flag + 1
    
    usr_data = orgn_data[orgn_data.user_id == usr]
    usr_data = usr_data[usr_data.timdiff <= ref_lft]
    
    usr_bgt_data = usr_data[usr_data.behavior_type == 4]
    bgt_set = set(usr_bgt_data.item_id)
    catg_set = set(usr_bgt_data.item_category)
    
    if len(bgt_set) < 8:
        continue
    if len(catg_set) < 4:
        continue
        
    ignr_cnt = 0
    for bgt_itm in bgt_set:
        itm_data = usr_data[usr_data.item_id == bgt_itm]
        itm_bgt_data = itm_data[itm_data.behavior_type == 4]
        
        fst_bgt_time = min(itm_bgt_data.timdiff)
        if fst_bgt_time <= ignr_lft:
            ignr_cnt = ignr_cnt + 1
            continue
            
        if fst_bgt_time >= dbl_12_lft and fst_bgt_time <= dbl_12_rgt:
            bgn_bh_time = min(itm_data.timdiff)
            if bgn_bh_time >= dbl_12_11_lft:
                ignr_cnt = ignr_cnt + 1
 #####################################       
        fst_bgt_time = min(itm_bgt_data.timdiff)
        fst_bgt_data = itm_bgt_data[itm_bgt_data.timdiff == fst_bgt_time]
        fst_bgt_date_str = fst_bgt_data.time.values[0][0:10]
        fst_bgt_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d')
        
        bgn_bh_time = min(itm_data.timdiff)
        bgn_bh_data = itm_data[itm_data.timdiff == bgn_bh_time]
        bgn_bh_date_str = bgn_bh_data.time.values[0][0:10]
        bgn_bh_date = datetime.strptime(bgn_bh_date_str, '%Y-%m-%d')
        
        delta = (fst_bgt_date - bgn_bh_date).days + 1
        if delta <= 1:
            ignr_cnt = ignr_cnt + 1
   
 #######################################               
    if len(bgt_set) - ignr_cnt >= 7:
        for i in range(0, len(usr_data)):
            clnd_data.writerow(usr_data.values[i])
import time

ignr_lft = (time.strptime('2014-11-21 23', '%Y-%m-%d %H')).tm_yday * 24
dbl_12_lft = (time.strptime('2014-12-11 23', '%Y-%m-%d %H')).tm_yday * 24
dbl_12_rgt = (time.strptime('2014-12-12 23', '%Y-%m-%d %H')).tm_yday * 24 
dbl_12_11_lft = (time.strptime('2014-12-10 23', '%Y-%m-%d %H')).tm_yday * 24


# average times of different behaviors on boughten item
def behavior_boughten_item_average(usr_data, boughten_item_set):

    # if the user didn't buy any staff, then browsing times, masking times, and
    # adding times are 0
    if len(boughten_item_set) == 0:
        return([0.0, 0.0, 0.0])
    
    bh_1_lst = list()
    bh_2_lst = list()
    bh_3_lst = list()

    # get the total times of different behaviors across all items boughten by usr
    for itm in boughten_item_set:
        itm_data = usr_data[usr_data.item_id == itm] # data of itm, includs all related behaviors
        itm_bgt_data = itm_data[itm_data.behavior_type == 4]
        
        fst_bgt_time = min(itm_bgt_data.time_difference)
        if fst_bgt_time <= ignr_lft:
            continue
            
        if fst_bgt_time >= dbl_12_lft and fst_bgt_time <= dbl_12_rgt:
            bgn_bh_time = min(itm_data.time_difference)
            if bgn_bh_time >= dbl_12_11_lft:
                continue
                
        fst_bgt_data = itm_bgt_data[itm_bgt_data.time_difference == fst_bgt_time]
        fst_bgt_date_str = fst_bgt_data.time.values[0][0:10]
        fst_bgt_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d')
        bgn_bh_time = min(itm_data.time_difference)
        bgn_bh_data = itm_data[itm_data.time_difference == bgn_bh_time]
        bgn_bh_date_str = bgn_bh_data.time.values[0][0:10]
        bgn_bh_date = datetime.strptime(bgn_bh_date_str, '%Y-%m-%d')
        delta = (fst_bgt_date - bgn_bh_date).days + 1
        if delta <= 1:
            continue
        
        for i in range(0, len(itm_data)):
            itm_data.time.values[i] = itm_data.time.values[i][0:10]
            
        itm_data = itm_data[itm_data.time_difference <= fst_bgt_time]
        itm_data = itm_data[itm_data.time != fst_bgt_date_str]
        
        bh_1_lst.append(float(len(itm_data[itm_data.behavior_type == 1])))
        bh_2_lst.append(float(len(itm_data[itm_data.behavior_type == 2])))
        bh_3_lst.append(float(len(itm_data[itm_data.behavior_type == 3])))
   
    if len(bh_1_lst) != 0:
        bh_1_avrg = np.mean(bh_1_lst)
        bh_2_avrg = np.mean(bh_2_lst)
        bh_3_avrg = np.mean(bh_3_lst)
        return([bh_1_avrg, bh_2_avrg, bh_3_avrg])
    else:
        return([0.0, 0.0, 0.0])



# average times of different behaviors on bought category
def behavior_boughten_category_average(usr_data, boughten_category_set):

    # if happens, usr is an inactive usr, he/she didn't buy anthing during the 29 days
    if len(boughten_category_set) == 0:
        return([0.0, 0.0, 0.0])
    
    bh_1_lst = list()
    bh_2_lst = list()
    bh_3_lst = list()
    
    # calculate the times of different behaviors on boughten categories
    for catg in boughten_category_set:
        catg_data = usr_data[usr_data.item_category == catg] # data concerned with catg, includes all types of behaviors
        catg_bgt_data = catg_data[catg_data.behavior_type == 4] # usr may bought something from catg for several times
        
        fst_bgt_time = min(catg_bgt_data.time_difference) # get the date when usr first bought something from catg
        if fst_bgt_time <= ignr_lft:
            continue
            
        if fst_bgt_time >= dbl_12_lft and fst_bgt_time <= dbl_12_rgt:
            bgn_bh_time = min(catg_data.time_difference)
            if bgn_bh_time >= dbl_12_11_lft:
                continue
        
        fst_bgt_data = catg_bgt_data[catg_bgt_data.time_difference == fst_bgt_time]
        fst_bgt_date_str = fst_bgt_data.time.values[0][0:10]
        fst_bgt_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d')
        bgn_bh_time = min(catg_data.time_difference)
        bgn_bh_data = catg_data[catg_data.time_difference == bgn_bh_time]
        bgn_bh_date_str = bgn_bh_data.time.values[0][0:10]
        bgn_bh_date = datetime.strptime(bgn_bh_date_str, '%Y-%m-%d')
        delta = (fst_bgt_date - bgn_bh_date).days + 1
        if delta <= 1:
            continue
        
        for i in range(0, len(catg_data)):
            catg_data.time.values[i] = catg_data.time.values[i][0:10]
        
        catg_data = catg_data[catg_data.time_difference <= fst_bgt_time]
        catg_data = catg_data[catg_data.time != fst_bgt_date_str]
        
        bh_1_lst.append(float(len(catg_data[catg_data.behavior_type == 1])))
        bh_2_lst.append(float(len(catg_data[catg_data.behavior_type == 2])))
        bh_3_lst.append(float(len(catg_data[catg_data.behavior_type == 3])))
    
    if len(bh_1_lst) > 0:
        bh_1_avrg = np.mean(bh_1_lst)
        bh_2_avrg = np.mean(bh_2_lst)
        bh_3_avrg = np.mean(bh_3_lst)
        return([bh_1_avrg, bh_2_avrg, bh_3_avrg])
    else:
        return([0.0, 0.0, 0.0])


# average times of different behaviors on similiar items with respect to boughten item
# similiar item is defined as any other item in that category where the boughten item belongs to
def behavior_similar_item_average(usr_data, boughten_item_set):
    
    if len(boughten_item_set) == 0:
        return([0.0, 0.0, 0.0])
    
    bh_1_lst = list()
    bh_2_lst = list()
    bh_3_lst = list()

    # suppose the boughten item set for usr is given by {I_1, I_2, ..., I_n}
    # I_i belongs to C_i, where C_i is an category, then C_i \ {I_i} is the
    # similiar item set for I_i, denote it as S_i, we first get the average times
    # of different behaviors on item in S_i, denote it as bh_m_i, where m = 1, 2, 3,
    # corresponding to browsing, marking, adding. Then we get sum(bh_m_i) / n, which
    # is the average times of behavior m on similiar item
    
    for itm in boughten_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        itm_bgt_data = itm_data[itm_data.behavior_type == 4] 
        catg = itm_data.item_category.values[0]
        catg_data = usr_data[usr_data.item_category == catg]
        
        fst_bgt_time = min(itm_bgt_data.time_difference) 
        if fst_bgt_time <= ignr_lft:
            continue
            
        if fst_bgt_time >= dbl_12_lft and fst_bgt_time <= dbl_12_rgt:
            bgn_bh_time = min(catg_data.time_difference)
            if bgn_bh_time >= dbl_12_11_lft:
                continue
                
        fst_bgt_data = itm_bgt_data[itm_bgt_data.time_difference == fst_bgt_time]
        fst_bgt_date_str = fst_bgt_data.time.values[0][0:10]
        fst_bgt_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d')
        bgn_bh_time = min(itm_data.time_difference)
        bgn_bh_data = itm_data[itm_data.time_difference == bgn_bh_time]
        bgn_bh_date_str = bgn_bh_data.time.values[0][0:10]
        bgn_bh_date = datetime.strptime(bgn_bh_date_str, '%Y-%m-%d')
        delta = (fst_bgt_date - bgn_bh_date).days + 1
        if delta <= 1:
            continue
        
        for i in range(0, len(catg_data)):
            catg_data.time.values[i] = catg_data.time.values[i][0:10]
                                                                
        catg_data = catg_data[catg_data.time_difference <= fst_bgt_time] 
        catg_data = catg_data[catg_data.time != fst_bgt_date_str]
        
        sml_itm_set = set(catg_data.item_id).difference(set([itm]))
        
        if len(sml_itm_set) == 0:
            continue
   
        bh_sml_1_lst = list()
        bh_sml_2_lst = list()
        bh_sml_3_lst = list()
        
        for sml_itm in sml_itm_set:
            sml_itm_data = catg_data[catg_data.item_id == sml_itm]
            bh_sml_1_lst.append(float(len(sml_itm_data[sml_itm_data.behavior_type == 1])))
            bh_sml_2_lst.append(float(len(sml_itm_data[sml_itm_data.behavior_type == 2])))
            bh_sml_3_lst.append(float(len(sml_itm_data[sml_itm_data.behavior_type == 3])))
            
        bh_1_lst.append(np.mean(bh_sml_1_lst))
        bh_2_lst.append(np.mean(bh_sml_2_lst))
        bh_3_lst.append(np.mean(bh_sml_3_lst))

    if len(bh_1_lst) > 0:
        bh_1_avrg = np.mean(bh_1_lst)
        bh_2_avrg = np.mean(bh_2_lst)
        bh_3_avrg = np.mean(bh_3_lst)
        return([bh_1_avrg, bh_2_avrg, bh_3_avrg])
    else:
        return([0.0, 0.0, 0.0])


# cycle on bought item, from the very begining of browing that item to the end of buying it
def cycle_boughten_item(usr_data, boughten_item_set):

    # an inactive user, we think the cycle for buying an item is 1000 days, simply neglect such user
    # when you get process to prediction part
    if len(boughten_item_set) == 0:
        return 1000.0
    
    cycle_lst = list()
    
    # get the total cycle length for boughten items
    for itm in boughten_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        itm_bgt_data = itm_data[itm_data.behavior_type == 4]
        
        fst_bgt_time = min(itm_bgt_data.time_difference)
        if fst_bgt_time <= ignr_lft:
            continue
            
        if fst_bgt_time >= dbl_12_lft and fst_bgt_time <= dbl_12_rgt:
            bgn_bh_time = min(itm_data.time_difference)
            if bgn_bh_time >= dbl_12_11_lft:
                continue
                
        fst_bgt_data = itm_bgt_data[itm_bgt_data.time_difference == fst_bgt_time]
        fst_bgt_date_str = fst_bgt_data.time.values[0][0:10]
        fst_bgt_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d')
        bgn_bh_time = min(itm_data.time_difference)
        bgn_bh_data = itm_data[itm_data.time_difference == bgn_bh_time]
        bgn_bh_date_str = bgn_bh_data.time.values[0][0:10]
        bgn_bh_date = datetime.strptime(bgn_bh_date_str, '%Y-%m-%d')
        delta = (fst_bgt_date - bgn_bh_date).days + 1
        if delta <= 1:
            continue
            
        cycle_lst.append(float(delta))
    
    if len(cycle_lst) > 0:
        cycle_avrg = np.mean(cycle_lst)
        return cycle_avrg
    else:
        return 1000.0


def propotion_active_window(usr_data, boughten_item_set):
    
    if len(boughten_item_set) == 0:
        return([-1.0, -1.0, -1.0])
    
    act_1d_lst = list()
    act_2d_lst = list()
    act_3d_lst = list()
    
    for itm in boughten_item_set:
        itm_data = usr_data[usr_data.item_id == itm]        
              
        for i in range(0, len(itm_data)):
            itm_data.time.values[i] = itm_data.time.values[i][0:10]
            
        itm_bgt_data = itm_data[itm_data.behavior_type == 4]
        
        fst_bgt_time = min(itm_bgt_data.time_difference)
        if fst_bgt_time <= ignr_lft:
            continue
            
        if fst_bgt_time >= dbl_12_lft and fst_bgt_time <= dbl_12_rgt:
            bgn_bh_time = min(itm_data.time_difference)
            if bgn_bh_time >= dbl_12_11_lft:
                continue
        
        fst_bgt_data = itm_bgt_data[itm_bgt_data.time_difference == fst_bgt_time]
        fst_bgt_date_str = fst_bgt_data.time.values[0]
        fst_bgt_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d')
        bgn_bh_time = min(itm_data.time_difference)
        bgn_bh_data = itm_data[itm_data.time_difference == bgn_bh_time]
        bgn_bh_date_str = bgn_bh_data.time.values[0]
        bgn_bh_date = datetime.strptime(bgn_bh_date_str, '%Y-%m-%d')
        delta = (fst_bgt_date - bgn_bh_date).days + 1
        if delta <= 1:
            continue
            
            
        bef_1d_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d') - timedelta(days=1)
        bef_2d_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d') - timedelta(days=2)
        bef_3d_date = datetime.strptime(fst_bgt_date_str, '%Y-%m-%d') - timedelta(days=3)
        bef_1d_date_str = datetime.strftime(bef_1d_date, '%Y-%m-%d')
        bef_2d_date_str = datetime.strftime(bef_2d_date, '%Y-%m-%d')
        bef_3d_date_str = datetime.strftime(bef_3d_date, '%Y-%m-%d')
        
        bef_1d_data = itm_data[itm_data.time == bef_1d_date_str]
        bef_2d_data = itm_data[itm_data.time == bef_2d_date_str]
        bef_3d_data = itm_data[itm_data.time == bef_3d_date_str]
        
        if len(bef_1d_data) > 0:
            act_1d_lst.append(1.0)
        else:
            act_1d_lst.append(0.0)
        
        if len(bef_1d_data) > 0 or len(bef_2d_data) > 0:
            act_2d_lst.append(1.0)
        else:
            act_2d_lst.append(0.0)
        if len(bef_1d_data) > 0 or len(bef_2d_data) > 0 or len(bef_2d_data) > 0:
            act_3d_lst.append(1.0)
        else:
            act_3d_lst.append(0.0)
    
    if len(act_1d_lst) > 0:
        act_1d_prop = np.mean(act_1d_lst)
        act_2d_prop = np.mean(act_2d_lst)
        act_3d_prop = np.mean(act_3d_lst)
        return([act_1d_prop, act_2d_prop, act_3d_prop])
    else:
        return([-1.0, -1.0, -1.0])
    
        
## MAIN BODY 
#
#
import pandas as pd
import numpy as np
import csv
from datetime import datetime
from datetime import timedelta

# READ IN USER DATA
# Customize your file path!!!
user_file = 'F:/activities/TianChi/data/cleaned_tianchi_mobile_recommend_train_user.csv'
user_data = pd.read_csv(user_file)

# OUTPUT FILE
#Customize your file path!!!
stat_file = 'F:/activities/TianChi/data/user_behavior_attributes.csv'
file_user_stat = csv.writer(open(stat_file, 'wb'))
file_user_stat.writerow(['user_id', 'bh_1_itm_avrg', 'bh_2_itm_avrg', 'bh_3_itm_avrg', \
                         'bh_1_catg_avrg', 'bh_2_catg_avrg', 'bh_3_catg_avrg', \
                         'bh_1_sml_avrg', 'bh_2_sml_avrg', 'bh_3_sml_avrg', 'cycle_avrg'])


# get behavior statistics for each user
user_set = set(user_data.user_id)

flag = 1
for usr in user_set:
    print flag
    flag = flag + 1
    
    usr_data = user_data[user_data.user_id == usr] 
    usr_boughten_data = usr_data[usr_data.behavior_type == 4] 
    item_set = set(usr_data.item_id) 
    category_set = set(usr_data.item_category) 
    boughten_item_set = set(usr_boughten_data.item_id) 
    boughten_category_set = set(usr_boughten_data.item_category) 
    
    [bh_1_itm_avrg, bh_2_itm_avrg, bh_3_itm_avrg] = behavior_boughten_item_average(usr_data, boughten_item_set)
    [bh_1_catg_avrg, bh_2_catg_avrg, bh_3_catg_avrg] = behavior_boughten_category_average(usr_data, boughten_category_set)
    [bh_1_sml_avrg, bh_2_sml_avrg, bh_3_sml_avrg] = behavior_similar_item_average(usr_data, boughten_item_set)
    cycle_avrg = cycle_boughten_item(usr_data, boughten_item_set)
 #   [act_1d_prop, act_2d_prop, act_3d_prop] = propotion_active_window(usr_data, boughten_item_set)
    
    file_user_stat.writerow([usr] + [bh_1_itm_avrg, bh_2_itm_avrg, bh_3_itm_avrg] +\
                            [bh_1_catg_avrg, bh_2_catg_avrg, bh_3_catg_avrg] +\
                            [bh_1_sml_avrg, bh_2_sml_avrg, bh_3_sml_avrg] + [cycle_avrg])

##it finds some statistics of user behavior
# results are saved in a table

import pandas as pd
import numpy as np
import json
import csv
import os
import behavior_statistics_functions
from collections import defaultdict

root_path = 'F:/activities/'
user_file = root_path + 'tianchi_mobile_recommend_train_user.csv'

# read in user data
user_data = pd.read_csv(user_file)
# prepare the user_behavior_statistics output file
stat_file = root_path + 'TianChi_TeamPSU/data/algorithm_II/user_behavior_statistics.csv'
file_user_stat = csv.writer(open(stat_file), 'wb')
file_user_stat.writerow(['user_id', 'behavior_1_total', 'behavior_2_total', 'behavior_3_total' \
                         'behavior_1_bought_itm_avrg', 'behavior_2_bought_itm_avrg', 'behavior_3_bought_itm_avrg' \
                         'behavior_1_unbought_itm_avrg', 'behavior_2_unbought_itm_avrg', 'behavior_3_unbought_itm_avrg' \
                         'behavior_1_bought_catg_avrg', 'behavior_2_bought_catg_avrg', 'behavior_3_bought_catg_avrg' \
                         'behavior_1_unbought_catg_avrg', 'behavior_2_unbought_catg_avrg', 'behavior_3_unbought_catg_avrg' \
                         'behavior_1_similar_avrg', 'behavior_2_similar_avrg', 'behavior_3_similar_avrg' \
                         'cycle_bought_itm_avrg', 'cycle_unbought_itm_avrg'])

# sort the data by time, then change time format, omit hour information
user_data = user_data.sort('time')
for i range(0, len(user_data)):
    user_data.time[i] = user_data.time[i][0:10]

user_data = user_data[user_data.time >= '2014-11-20']
user_data = user_data[user_data.time <= '2014-12-16']

# get behavior statistics for each user
user_set = set(user_data.user_id)

for usr in user_set:
    usr_data = user_data[user_data.user_id == usr] # data of the particular user
    
    usr_bought_data = usr_data[usr_data.behavior_type == 4] # user bought something
    item_set = set(usr_data.item_id)
    category_set = set(usr_data.category_id)
    bought_item_set = set(usr_bought_data.item_id)
    bought_category_set = set(usr_bought_data.category_id)
    unbought_item_set = item_set.difference(bought_item_set)
    unbought_category_set = category_set.difference(bought_category_set)
    
    [behavior_1_totl, behavior_2_totl, behavior_3_totl, behavior_4_totl] = behaviors_total(usr_data)
    
    [behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg] = \
    behavior_bought_item_average(usr_data, bought_item_set)
    
    [behavior_1_unbought_itm_avrg, behavior_2_unbought_itm_avrg, behavior_3_unbought_itm_avrg] = \
    behavior_unbought_item_average(usr_data, unbought_item_set)
    
    [behavior_1_bought_catg_avrg, behavior_2_bought_catg_avrg, behavior_3_bought_catg_avrg] = \
    behavior_bought_category_average(usr_data, bought_category_set)
    
    [behavior_1_unbought_catg_avrg, behavior_2_unbought_catg_avrg, behavior_3_unbought_catg_avrg] = \
    behavior_unbought_category_average(usr_data, unbought_category_set)
    
    [behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg] = \
    behavior_similar_item_average(usr_data, bought_item_set)
    
    cycle_bought_itm_avrg = cycle_bought_item(usr_data, bought_item_set)
    
    cycle_unbought_itm_avrg = cycle_unbought_item(usr_data, unbought_item_set)
    
    file_user_stat.writerow([usr] + [behavior_1_totl, behavior_2_totl, behavior_3_totl, behavior_4_totl] + \
                            [behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg] + \
                            [behavior_1_unbought_itm_avrg, behavior_2_unbought_itm_avrg, behavior_3_unbought_itm_avrg] + \
                            [behavior_1_bought_catg_avrg, behavior_2_bought_catg_avrg, behavior_3_bought_catg_avrg] + \
                            [behavior_1_unbought_catg_avrg, behavior_2_unbought_catg_avrg, behavior_3_unbought_catg_avrg] + \
                            [behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg] + \
                            [cycle_bought_itm_avrg, cycle_unbought_itm_avrg])

os.remove(file_user_stat)

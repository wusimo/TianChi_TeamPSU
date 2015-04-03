# average times of different behaviors on bought item
def behavior_bought_item_average(usr_data, bought_item_set):

    # if the user didn't buy any staff
    if len(bought_item_set) == 0:
        return([0, 0, 0])
    
    behavior_1_bought_itm_sum = 0 # 1 for browse
    behavior_2_bought_itm_sum = 0
    behavior_3_bought_itm_sum = 0
    
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm] # usr's data on itm
        itm_bought_data = itm_data[itm_data.behavior_type == 4] # usr may buy itm for several times, extract all information 
                                                                # when usr bought itm
        first_bought_time = itm_bought_data.time[0] # find the first time usr bought itm
        itm_data = itm_data[itm_data.time <= first_bought_time] # user behavior data on bought item before 
                                                                # the first bought time, we don't care usr's
                                                                # behavior after the first time he/she bought it
        
        behavior_1_bought_itm_sum = behavior_1_bought_itm_sum + len(itm_data[itm_data.behavior_type == 1]) # total times of browsing on all 
                                                                                                           # itm in bought_item_set
        behavior_2_bought_itm_sum = behavior_2_bought_itm_sum + len(itm_data[itm_data.behavior_type == 2])
        behavior_3_bought_itm_sum = behavior_3_bought_itm_sum + len(itm_data[itm_data.behavior_type == 3])
        
    behavior_1_bought_itm_avrg = behavior_1_bought_itm_sum / len(bought_item_set) # average times of browsing on bought item
    behavior_2_bought_itm_avrg = behavior_2_bought_itm_sum / len(bought_item_set)
    behavior_3_bought_itm_avrg = behavior_3_bought_itm_sum / len(bought_item_set)
    
    return([behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg])



# the following code finds each user's average times of different behaviors on bought items 
#
#
import pandas as pd
import numpy as np
import json
import csv
import os


#import behavior_statistics_functions
from collections import defaultdict

# read in user data
user_file = 'F:/activities/TianChi_TeamPSU/data/algorithm_II/test_tianchi_mobile_recommend_train_user.csv'
user_data = pd.read_csv(user_file)

# prepare the user_behavior_statistics output file
stat_file = 'F:/activities/TianChi_TeamPSU/data/algorithm_II/test_user_behavior_statistics.csv'
file_user_stat = csv.writer(open(stat_file, 'wb'))
file_user_stat.writerow(['user_id', 'behavior_1_bought_itm_avrg', 'behavior_2_bought_itm_avrg', 'behavior_3_bought_itm_avrg'])

# sort the data by time, then change time format, omit hour information
user_data = user_data.sort('time')
for i in range(0, len(user_data)):
    user_data.time[i] = user_data.time[i][0:10]

# drop the data before 2014-11-20 or behind 2014-12-16
user_data = user_data[user_data.time >= '2014-11-20']
user_data = user_data[user_data.time <= '2014-12-16']

# get behavior statistics for each user
user_set = set(user_data.user_id)

for usr in user_set:
    usr_data = user_data[user_data.user_id == usr] # data of the particular user
    usr_bought_data = usr_data[usr_data.behavior_type == 4] # user bought something
    item_set = set(usr_data.item_id) # set of items where usr has at least one behavior on
    category_set = set(usr_data.item_category) # set of categories whre usr has at least one behavior on
    bought_item_set = set(usr_bought_data.item_id) # set of bought items
    bought_category_set = set(usr_bought_data.item_category) # set of bought categories
    unbought_item_set = item_set.difference(bought_item_set) # set of unbought items
    unbought_category_set = category_set.difference(bought_category_set) # set of unbought categories
    
    [behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg] = behavior_bought_item_average(usr_data, bought_item_set)
    
    file_user_stat.writerow([usr] + [behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg])
    
# close the file
os.remove(file_user_stat)

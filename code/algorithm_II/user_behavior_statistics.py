# total times of different behaviors
def behaviors_total(usr_data):
    
    behavior_1_totl = len(usr_data[usr_data.behavior_type == 1])
    behavior_2_totl = len(usr_data[usr_data.behavior_type == 2])
    behavior_3_totl = len(usr_data[usr_data.behavior_type == 3])
    behavior_4_totl = len(usr_data[usr_data.behavior_type == 4])
    
    return([behavior_1_totl, behavior_2_totl, behavior_3_totl, behavior_4_totl])

# average times of different behaviors on bought item
def behavior_bought_item_average(usr_data, bought_item_set):

    # if the user didn't buy any staff
    if len(bought_item_set) == 0:
        return([0, 0, 0])
    
    behavior_1_bought_itm_sum = 0
    behavior_2_bought_itm_sum = 0
    behavior_3_bought_itm_sum = 0
    
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        itm_bought_data = itm_data[itm_data.behavior_type == 4]
        first_bought_time = min(itm_bought_data.time)
        itm_data = itm_data[itm_data.time <= first_bought_time] # user behavior data on bought item before 
                                                                # the first bought time
        
        behavior_1_bought_itm_sum = behavior_1_bought_itm_sum + len(itm_data[itm_data.behavior_type == 1])
        behavior_2_bought_itm_sum = behavior_2_bought_itm_sum + len(itm_data[itm_data.behavior_type == 2])
        behavior_3_bought_itm_sum = behavior_3_bought_itm_sum + len(itm_data[itm_data.behavior_type == 3])
        
    behavior_1_bought_itm_avrg = behavior_1_bought_itm_sum / len(bought_item_set)
    behavior_2_bought_itm_avrg = behavior_2_bought_itm_sum / len(bought_item_set)
    behavior_3_bought_itm_avrg = behavior_3_bought_itm_sum / len(bought_item_set)
    
    return([behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg])


# average times of different behaviors on unbought item
def behavior_unbought_item_average(usr_data, unbought_item_set):

    if len(unbought_item_set) == 0:
        return([0, 0, 0])
    
    behavior_1_unbought_itm_sum = 0
    behavior_2_unbought_itm_sum = 0
    behavior_3_unbought_itm_sum = 0
    
    for itm in unbought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        behavior_1_unbought_itm_sum = behavior_1_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 1])
        behavior_2_unbought_itm_sum = behavior_2_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 2])
        behavior_3_unbought_itm_sum = behavior_3_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 3])
        
    behavior_1_unbought_itm_avrg = behavior_1_unbought_itm_sum / len(unbought_item_set)
    behavior_2_unbought_itm_avrg = behavior_2_unbought_itm_sum / len(unbought_item_set)
    behavior_3_unbought_itm_avrg = behavior_3_unbought_itm_sum / len(unbought_item_set)
    
    return([behavior_1_unbought_itm_avrg, behavior_2_unbought_itm_avrg, behavior_3_unbought_itm_avrg])


# average times of different behaviors on bought category
def behavior_bought_category_average(usr_data, bought_category_set):
    
    if len(bought_category_set) == 0:
        return([0, 0, 0])
    
    behavior_1_bought_catg_sum = 0
    behavior_2_bought_catg_sum = 0
    behavior_3_bought_catg_sum = 0
    
    for catg in bought_category_set:
        catg_data = usr_data[usr_data.item_category == catg]
        catg_bought_data = catg_data[catg_data.behavior_type == 4]
        first_bought_time = min(catg_bought_data.time)
        catg_data = catg_data[catg_data.time <= first_bought_time] # user behavior data on bought category before 
                                                                   # the first bought time
        
        behavior_1_bought_catg_sum = behavior_1_bought_catg_sum + len(catg_data[catg_data.behavior_type == 1])
        behavior_2_bought_catg_sum = behavior_2_bought_catg_sum + len(catg_data[catg_data.behavior_type == 2])
        behavior_3_bought_catg_sum = behavior_3_bought_catg_sum + len(catg_data[catg_data.behavior_type == 3])
        
    behavior_1_bought_catg_avrg = behavior_1_bought_catg_sum / len(bought_category_set)
    behavior_2_bought_catg_avrg = behavior_2_bought_catg_sum / len(bought_category_set)
    behavior_3_bought_catg_avrg = behavior_3_bought_catg_sum / len(bought_category_set)
    
    return([behavior_1_bought_catg_avrg, behavior_2_bought_catg_avrg, behavior_3_bought_catg_avrg])


# average times of different behaviors on unbought category
def behavior_unbought_category_average(usr_data, unbought_category_set):
    
    if len(unbought_category_set) == 0:
        return([0, 0, 0])
    
    behavior_1_unbought_catg_sum = 0
    behavior_2_unbought_catg_sum = 0
    behavior_3_unbought_catg_sum = 0
    
    for catg in unbought_category_set:
        catg_data = usr_data[usr_data.item_category == catg]
        behavior_1_unbought__catg_sum = behavior_1_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 1])
        behavior_2_unbought_catg_sum = behavior_2_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 2])
        behavior_3_unbought_catg_sum = behavior_3_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 3])
        
    behavior_1_unbought_catg_avrg = behavior_1_unbought_catg_sum / len(unbought_category_set) 
    behavior_2_unbought_catg_avrg = behavior_2_unbought_catg_sum / len(unbought_category_set)
    behavior_3_unbought_catg_avrg = behavior_3_unbought_catg_sum / len(unbought_category_set)
    
    return([behavior_1_unbought_catg_avrg, behavior_2_unbought_catg_avrg, behavior_3_unbought_catg_avrg])


# average times of different behaviors on similiar items with respect to bought item
def behavior_similar_item_average(usr_data, bought_item_set):
    
    if len(bought_item_set) == 0:
        return([0, 0, 0])
    
    behavior_1_similar_sum = 0
    behavior_2_similar_sum = 0
    behavior_3_similar_sum = 0
    
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        catg = itm_data.item_category.values[0]
        itm_bought_data = itm_data[itm_data.behavior_type == 4]
        first_bought_time = min(itm_bought_data.time)
        catg_data = usr_data[usr_data.item_category == catg]
        catg_data = catg_data[catg_data.time <= first_bought_time]
        similar_itm_set = set(catg_data.item_id) # similar items in the same category
        similar_itm_set = similar_itm_set.difference(set([itm]))
        
        if len(similar_itm_set) == 0:
            continue
            
        behavior_1_similar_within_sum = 0
        behavior_2_similar_within_sum = 0
        behavior_3_similar_within_sum = 0
        
        for within_itm in similar_itm_set:
            within_itm_data = catg_data[catg_data.item_id == within_itm]
            behavior_1_similar_within_sum = behavior_1_similar_within_sum + len(within_itm_data.behavior_type == 1)
            behavior_2_similar_within_sum = behavior_2_similar_within_sum + len(within_itm_data.behavior_type == 2)
            behavior_3_similar_within_sum = behavior_3_similar_within_sum + len(within_itm_data.behavior_type == 3)
    
        behavior_1_similar_sum = behavior_1_similar_sum + behavior_1_similar_within_sum / len(similar_itm_set)
        behavior_2_similar_sum = behavior_2_similar_sum + behavior_2_similar_within_sum / len(similar_itm_set)
        behavior_3_similar_sum = behavior_3_similar_sum + behavior_3_similar_within_sum / len(similar_itm_set)

    behavior_1_similar_avrg = behavior_1_similar_sum / len(bought_item_set)
    behavior_2_similar_avrg = behavior_2_similar_sum / len(bought_item_set)
    behavior_3_similar_avrg = behavior_3_similar_sum / len(bought_item_set)
    
    return([behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg])


# cycle on bought item, from the very begining of browing that item to the end of buying it
def cycle_bought_item(usr_data, bought_item_set):
    
    if len(bought_item_set) == 0:
        return 1000
    
    cycle_bought_itm_sum = 0
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        begin_behavior_time = min(itm_data.time)
        itm_bought_data = itm_data[itm_data.behavior_type == 4]
        first_bought_time = min(itm_bought_data.time)
        delta = datetime.strptime(first_bought_time, '%Y-%m-%d') - datetime.strptime(begin_behavior_time, '%Y-%m-%d')
        cycle_bought_itm_sum = cycle_bought_itm_sum + delta.days + 1
    
    cycle_bought_itm_avrg = cycle_bought_itm_sum / len(bought_item_set)
    
    return cycle_bought_itm_avrg

# cycle on unbought item, from the very begining of browing that item to the end of buying it
def cycle_unbought_item(usr_data, unbought_item_set):
    
    if len(unbought_item_set) == 0:
        return 1000
    
    cycle_unbought_itm_sum = 0
    for itm in unbought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        begin_behavior_time = min(itm_data.time)
        end_behavior_time = max(itm_data.time)
        delta = datetime.strptime(end_behavior_time, '%Y-%m-%d') - datetime.strptime(begin_behavior_time, '%Y-%m-%d')
        cycle_unbought_itm_sum = cycle_unbought_itm_sum + delta.days + 1
    
    cycle_unbought_itm_avrg = cycle_unbought_itm_sum / len(unbought_item_set)
    
    return cycle_unbought_itm_avrg

    

# the following code finds each user's average times of different behaviors on bought items 
#
#
import pandas as pd
import numpy as np
import json
import csv
import os
from collections import defaultdict
from datetime import datetime

# READ IN USER DATA
# Customize your file path!!!
user_file = 'F:/activities/TianChi_TeamPSU/data/algorithm_II/test_tianchi_mobile_recommend_train_user.csv'
user_data = pd.read_csv(user_file)

# OUTPUT FILE
#Customize your file path!!!
stat_file = 'F:/activities/TianChi_TeamPSU/data/algorithm_II/test_user_behavior_statistics.csv'
file_user_stat = csv.writer(open(stat_file, 'wb'))
file_user_stat.writerow(['user_id', 'behavior_1_total', 'behavior_2_total', 'behavior_3_total', 'behavior_4_total', \
                         'behavior_1_bought_itm_avrg', 'behavior_2_bought_itm_avrg', 'behavior_3_bought_itm_avrg', \
                         'behavior_1_unbought_itm_avrg', 'behavior_2_unbought_itm_avrg', 'behavior_3_unbought_itm_avrg', \
                         'behavior_1_bought_catg_avrg', 'behavior_2_bought_catg_avrg', 'behavior_3_bought_catg_avrg', \
                         'behavior_1_unbought_catg_avrg', 'behavior_2_unbought_catg_avrg', 'behavior_3_unbought_catg_avrg', \
                         'behavior_1_similar_avrg', 'behavior_2_similar_avrg', 'behavior_3_similar_avrg', \
                         'cycle_bought_itm_avrg', 'cycle_unbought_itm_avrg'])

# sort the data by time, then change time format, omit hour information
user_data = user_data.sort('time')
for i in range(0, len(user_data)):
    user_data.time[i] = user_data.time[i][0:10]

# drop the data before 2014-11-20 or behind 2014-12-16
user_data = user_data[user_data.time >= '2014-11-20']
user_data = user_data[user_data.time <= '2014-12-16']

# get behavior statistics for each user
user_set = set(user_data.user_id)

#flag = 1
for usr in user_set:
#   print flag
#   flag = flag + 1
    usr_data = user_data[user_data.user_id == usr] # data of the particular user
    usr_bought_data = usr_data[usr_data.behavior_type == 4] # user bought something
    item_set = set(usr_data.item_id)
    category_set = set(usr_data.item_category)
    bought_item_set = set(usr_bought_data.item_id)
    bought_category_set = set(usr_bought_data.item_category)
    unbought_item_set = item_set.difference(bought_item_set)
    unbought_category_set = category_set.difference(bought_category_set)
    
    [behavior_1_totl, behavior_2_totl, behavior_3_totl, behavior_4_totl] = behaviors_total(usr_data)    
    
    [behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg] = behavior_bought_item_average(usr_data, bought_item_set)
    
    [behavior_1_unbought_itm_avrg, behavior_2_unbought_itm_avrg, behavior_3_unbought_itm_avrg] = behavior_unbought_item_average(usr_data, unbought_item_set)
    
    [behavior_1_bought_catg_avrg, behavior_2_bought_catg_avrg, behavior_3_bought_catg_avrg] = behavior_bought_category_average(usr_data, bought_category_set)
    
    [behavior_1_unbought_catg_avrg, behavior_2_unbought_catg_avrg, behavior_3_unbought_catg_avrg] = behavior_unbought_category_average(usr_data, unbought_category_set)
    
    [behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg] = behavior_similar_item_average(usr_data, bought_item_set)
    
    cycle_bought_itm_avrg = cycle_bought_item(usr_data, bought_item_set)
    
    cycle_unbought_itm_avrg = cycle_unbought_item(usr_data, unbought_item_set)
    
    file_user_stat.writerow([usr] + [behavior_1_totl, behavior_2_totl, behavior_3_totl, behavior_4_totl] + \
                            [behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg] + \
                            [behavior_1_unbought_itm_avrg, behavior_2_unbought_itm_avrg, behavior_3_unbought_itm_avrg] + \
                            [behavior_1_bought_catg_avrg, behavior_2_bought_catg_avrg, behavior_3_bought_catg_avrg] + \
                            [behavior_1_unbought_catg_avrg, behavior_2_unbought_catg_avrg, behavior_3_unbought_catg_avrg] + \
                            [behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg] + \
                            [cycle_bought_itm_avrg, cycle_unbought_itm_avrg])
    
# total times of different behaviors
# 1 for browsing
# 2 for marking
# 3 for adding
# 4 for buying

def behaviors_total(usr_data):
    
    behavior_1_totl = round(float(len(usr_data[usr_data.behavior_type == 1])), 3)
    behavior_2_totl = round(float(len(usr_data[usr_data.behavior_type == 2])), 3)
    behavior_3_totl = round(float(len(usr_data[usr_data.behavior_type == 3])), 3)
    behavior_4_totl = round(float(len(usr_data[usr_data.behavior_type == 4])), 3)
    
    return([behavior_1_totl, behavior_2_totl, behavior_3_totl, behavior_4_totl])

# average times of different behaviors on boughten item
def behavior_bought_item_average(usr_data, bought_item_set):

    # if the user didn't buy any staff, then browsing times, masking times, and
    # adding times are 0
    if len(bought_item_set) == 0:
        return([0.0, 0.0, 0.0])
    
    behavior_1_bought_itm_sum = 0.0
    behavior_2_bought_itm_sum = 0.0
    behavior_3_bought_itm_sum = 0.0

    # get the total times of different behaviors across all items boughten by usr
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm] # data of itm, includs all related behaviors
        itm_bought_data = itm_data[itm_data.behavior_type == 4] # usr may bought itm for several times
        first_bought_time = min(itm_bought_data.time) # get the date when usr first bought it
        itm_data = itm_data[itm_data.time <= first_bought_time] # user behavior data on bought item before 
                                                                # the first time he/she bought it
        
        behavior_1_bought_itm_sum = behavior_1_bought_itm_sum + len(itm_data[itm_data.behavior_type == 1])
        behavior_2_bought_itm_sum = behavior_2_bought_itm_sum + len(itm_data[itm_data.behavior_type == 2])
        behavior_3_bought_itm_sum = behavior_3_bought_itm_sum + len(itm_data[itm_data.behavior_type == 3])
        
    behavior_1_bought_itm_avrg = round(behavior_1_bought_itm_sum / len(bought_item_set), 3) # average times of browsing before usr finally
                                                                                            # decided to buy something
    behavior_2_bought_itm_avrg = round(behavior_2_bought_itm_sum / len(bought_item_set), 3)
    behavior_3_bought_itm_avrg = round(behavior_3_bought_itm_sum / len(bought_item_set), 3)
    
    return([behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg])


# average times of different behaviors on unbought item
def behavior_unbought_item_average(usr_data, unbought_item_set):

    if len(unbought_item_set) == 0:
        return([0.0, 0.0, 0.0])
    
    behavior_1_unbought_itm_sum = 0.0
    behavior_2_unbought_itm_sum = 0.0
    behavior_3_unbought_itm_sum = 0.0
    
    for itm in unbought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        behavior_1_unbought_itm_sum = behavior_1_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 1])
        behavior_2_unbought_itm_sum = behavior_2_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 2])
        behavior_3_unbought_itm_sum = behavior_3_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 3])
        
    behavior_1_unbought_itm_avrg = round(behavior_1_unbought_itm_sum / len(unbought_item_set), 3)
    behavior_2_unbought_itm_avrg = round(behavior_2_unbought_itm_sum / len(unbought_item_set), 3)
    behavior_3_unbought_itm_avrg = round(behavior_3_unbought_itm_sum / len(unbought_item_set), 3)
    
    return([behavior_1_unbought_itm_avrg, behavior_2_unbought_itm_avrg, behavior_3_unbought_itm_avrg])


# average times of different behaviors on bought category
def behavior_bought_category_average(usr_data, bought_category_set):

    # if happens, usr is an inactive usr, he/she didn't buy anthing during the 29 days
    if len(bought_category_set) == 0:
        return([0.0, 0.0, 0.0])
    
    behavior_1_bought_catg_sum = 0.0
    behavior_2_bought_catg_sum = 0.0
    behavior_3_bought_catg_sum = 0.0

    # calculate the times of different behaviors on boughten categories
    for catg in bought_category_set:
        catg_data = usr_data[usr_data.item_category == catg] # data concerned with catg, includes all types of behaviors
        catg_bought_data = catg_data[catg_data.behavior_type == 4] # usr may bought something from catg for several times
        first_bought_time = min(catg_bought_data.time) # get the date when usr first bought something from catg
        catg_data = catg_data[catg_data.time <= first_bought_time] # user behavior data on bought category before 
                                                                   # the first bought time
        
        behavior_1_bought_catg_sum = behavior_1_bought_catg_sum + len(catg_data[catg_data.behavior_type == 1])
        behavior_2_bought_catg_sum = behavior_2_bought_catg_sum + len(catg_data[catg_data.behavior_type == 2])
        behavior_3_bought_catg_sum = behavior_3_bought_catg_sum + len(catg_data[catg_data.behavior_type == 3])
        
    behavior_1_bought_catg_avrg = round(behavior_1_bought_catg_sum / len(bought_category_set), 3) # average browsing times before usr decided to
                                                                                                  # buy something from TaoBao
    behavior_2_bought_catg_avrg = round(behavior_2_bought_catg_sum / len(bought_category_set), 3)
    behavior_3_bought_catg_avrg = round(behavior_3_bought_catg_sum / len(bought_category_set), 3)
    
    return([behavior_1_bought_catg_avrg, behavior_2_bought_catg_avrg, behavior_3_bought_catg_avrg])


# average times of different behaviors on unbought category
def behavior_unbought_category_average(usr_data, unbought_category_set):
    
    if len(unbought_category_set) == 0:
        return([0.0, 0.0, 0.0])
    
    behavior_1_unbought_catg_sum = 0.0
    behavior_2_unbought_catg_sum = 0.0
    behavior_3_unbought_catg_sum = 0.0
    
    for catg in unbought_category_set:
        catg_data = usr_data[usr_data.item_category == catg]
        behavior_1_unbought_catg_sum = behavior_1_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 1])
        behavior_2_unbought_catg_sum = behavior_2_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 2])
        behavior_3_unbought_catg_sum = behavior_3_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 3])
        
    behavior_1_unbought_catg_avrg = round(behavior_1_unbought_catg_sum / len(unbought_category_set), 3) 
    behavior_2_unbought_catg_avrg = round(behavior_2_unbought_catg_sum / len(unbought_category_set), 3)
    behavior_3_unbought_catg_avrg = round(behavior_3_unbought_catg_sum / len(unbought_category_set), 3)
    
    return([behavior_1_unbought_catg_avrg, behavior_2_unbought_catg_avrg, behavior_3_unbought_catg_avrg])


# average times of different behaviors on similiar items with respect to boughten item
# similiar item is defined as any other item in that category where the boughten item belongs to
def behavior_similar_item_average(usr_data, bought_item_set):
    
    if len(bought_item_set) == 0:
        return([0.0, 0.0, 0.0])
    
    behavior_1_similar_sum = 0.0
    behavior_2_similar_sum = 0.0
    behavior_3_similar_sum = 0.0

    # suppose the boughten item set for usr is given by {I_1, I_2, ..., I_n}
    # I_i belongs to C_i, where C_i is an category, then C_i \ {I_i} is the
    # similiar item set for I_i, denote it as S_i, we first get the average times
    # of different behaviors on item in S_i, denote it as bh_m_i, where m = 1, 2, 3,
    # corresponding to browsing, marking, adding. Then we get sum(bh_m_i) / n, which
    # is the average times of behavior m on similiar item
    
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        catg = itm_data.item_category.values[0] # get the category of itm
        itm_bought_data = itm_data[itm_data.behavior_type == 4] # usr may bought itm for several times
        first_bought_time = min(itm_bought_data.time) # get the date when usr bought itm for the first time
        catg_data = usr_data[usr_data.item_category == catg] # data concerned with catg
        catg_data = catg_data[catg_data.time <= first_bought_time] # we don't care the data after the firt time usr bought
                                                                   # something from that category, people's behavior feature
                                                                   # generally changes when he/she buy something again, since
                                                                   # he/she already collected a lot information before
        similar_itm_set = set(catg_data.item_id) 
        similar_itm_set = similar_itm_set.difference(set([itm])) # similar items in the same category
        
        if len(similar_itm_set) == 0:
            continue
   
        behavior_1_similar_within_sum = 0.0
        behavior_2_similar_within_sum = 0.0
        behavior_3_similar_within_sum = 0.0
        
        for within_itm in similar_itm_set:
            within_itm_data = catg_data[catg_data.item_id == within_itm]
            behavior_1_similar_within_sum = behavior_1_similar_within_sum + len(within_itm_data[within_itm_data.behavior_type == 1])
            behavior_2_similar_within_sum = behavior_2_similar_within_sum + len(within_itm_data[within_itm_data.behavior_type == 2])
            behavior_3_similar_within_sum = behavior_3_similar_within_sum + len(within_itm_data[within_itm_data.behavior_type == 3])

        # behavior_m_similar_within_sum / len(similar_itm_set) is bh_m_i, m = 1, 2, 3
        behavior_1_similar_sum = behavior_1_similar_sum + behavior_1_similar_within_sum / len(similar_itm_set)
        behavior_2_similar_sum = behavior_2_similar_sum + behavior_2_similar_within_sum / len(similar_itm_set)
        behavior_3_similar_sum = behavior_3_similar_sum + behavior_3_similar_within_sum / len(similar_itm_set)

    behavior_1_similar_avrg = round(behavior_1_similar_sum / len(bought_item_set), 3)
    behavior_2_similar_avrg = round(behavior_2_similar_sum / len(bought_item_set), 3)
    behavior_3_similar_avrg = round(behavior_3_similar_sum / len(bought_item_set), 3)
    
    return([behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg])


# cycle on bought item, from the very begining of browing that item to the end of buying it
def cycle_bought_item(usr_data, bought_item_set):

    # an inactive user, we think the cycle for buying an item is 1000 days, simply neglect such user
    # when you get process to prediction part
    if len(bought_item_set) == 0:
        return 1000.0
    
    cycle_bought_itm_sum = 0.0
    # get the total cycle length for boughten items
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        begin_behavior_time = min(itm_data.time) # the very begining when usr had a behavior on itm
        itm_bought_data = itm_data[itm_data.behavior_type == 4] 
        first_bought_time = min(itm_bought_data.time) # the date when usr bougth itm for the first time
        delta = datetime.strptime(first_bought_time, '%Y-%m-%d') - datetime.strptime(begin_behavior_time, '%Y-%m-%d')
        cycle_bought_itm_sum = cycle_bought_itm_sum + delta.days + 1 # + 1 is very important for further function development consistency
                                                                     # for example, if begin_behavior_time = '20114-11-24', first_bought_time
                                                                     # = '2014-11-24', then delta.days = 0. we assume the shortest buying cycle
                                                                     # is 1 day
    
    cycle_bought_itm_avrg = round(cycle_bought_itm_sum / len(bought_item_set), 3)
    
    return cycle_bought_itm_avrg

# cycle on unbought item, from the very begining of browing that item to the end of buying it
def cycle_unbought_item(usr_data, unbought_item_set):
    
    if len(unbought_item_set) == 0:
        return 1000.0
    
    cycle_unbought_itm_sum = 0.0
    for itm in unbought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        begin_behavior_time = min(itm_data.time)
        end_behavior_time = max(itm_data.time)
        delta = datetime.strptime(end_behavior_time, '%Y-%m-%d') - datetime.strptime(begin_behavior_time, '%Y-%m-%d')
        cycle_unbought_itm_sum = cycle_unbought_itm_sum + delta.days + 1
    
    cycle_unbought_itm_avrg = round(cycle_unbought_itm_sum / len(unbought_item_set), 3)
    
    return cycle_unbought_itm_avrg

    

## MAIN BODY 
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
user_file = './test_tianchi_mobile_recommend_train_user.csv'
user_data = pd.read_csv(user_file)

# OUTPUT FILE
#Customize your file path!!!
stat_file = './test_user_behavior_statistics.csv'
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

# drop the data before 2014-11-20 or behind 2014-12-16, for accuracy consideration
# for forecasting, you must use the whold data with respect to time
user_data = user_data[user_data.time >= '2014-11-20']
user_data = user_data[user_data.time <= '2014-12-16']

# get behavior statistics for each user
user_set = set(user_data.user_id)

#flag = 1
for usr in user_set:
#   print flag
#   flag = flag + 1
    usr_data = user_data[user_data.user_id == usr] # data of usr
    usr_bought_data = usr_data[usr_data.behavior_type == 4] # usr bought something
    item_set = set(usr_data.item_id) # set of all items where usr had behavior(s) on
    category_set = set(usr_data.item_category) # set of all categories where usr had behavior(s) on
    bought_item_set = set(usr_bought_data.item_id) # set of all boughten items 
    bought_category_set = set(usr_bought_data.item_category) # set of all boughten categories, a boughten category is defined as
                                                             # a category in which at least on item was boughten by usr
    unbought_item_set = item_set.difference(bought_item_set) # set of all items usr didn't buy at last but had behavior(s) on 
    unbought_category_set = category_set.difference(bought_category_set) # set of all categories usr didn't buy at last but had behavior(s) on
    
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
    

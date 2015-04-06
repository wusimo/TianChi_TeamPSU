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
stat_file = 'F:/activities/TianChi_TeamPSU/data/algorithm_II/test_user_behavior_similar_statistics.csv'
file_user_stat = csv.writer(open(stat_file, 'wb'))
file_user_stat.writerow(['user_id', 'behavior_1_similar_avrg', 'behavior_2_similar_avrg', 'behavior_3_similar_avrg'])
#file_user_stat.writerow(['user_id', 'behavior_1_total', 'behavior_2_total', 'behavior_3_total', 'behavior_4_total', \
#                         'behavior_1_bought_itm_avrg', 'behavior_2_bought_itm_avrg', 'behavior_3_bought_itm_avrg', \
#                         'behavior_1_unbought_itm_avrg', 'behavior_2_unbought_itm_avrg', 'behavior_3_unbought_itm_avrg', \
#                         'behavior_1_bought_catg_avrg', 'behavior_2_bought_catg_avrg', 'behavior_3_bought_catg_avrg', \
#                         'behavior_1_unbought_catg_avrg', 'behavior_2_unbought_catg_avrg', 'behavior_3_unbought_catg_avrg', \
#                         'behavior_1_similar_avrg', 'behavior_2_similar_avrg', 'behavior_3_similar_avrg', \
#                         'cycle_bought_itm_avrg', 'cycle_unbought_itm_avrg'])

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

for usr in user_set:
    usr_data = user_data[user_data.user_id == usr] # data of usr
    usr_bought_data = usr_data[usr_data.behavior_type == 4] # usr bought something
    bought_item_set = set(usr_bought_data.item_id) # set of all boughten items 
 
    [behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg] = behavior_similar_item_average(usr_data, bought_item_set)

    file_user_stat.writerow([usr] + [behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg])
    

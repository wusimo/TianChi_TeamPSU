## there are some buyers whose behavior is hard to interpret or predict
# these people either decide to buy an item within the very day he/she
# starts to browse the product information or after only a few behaviors
# on the category where that item belongs to

import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict

user_data = pd.read_csv("F:/activities/tianchi_mobile_recommend_train_user.csv") # read in user data
# change the format of time, omit hour information and sort the data by time
for i in range(0, len(user_data)):
    user_data.time[i] = user_data.time[i][0:10]
user_data = user_data.sort('time')

file_hot_minded = csv.writer(open("F:/activities/TianChi_TeamPSU/data/hot_minded_transaction_volume.csv", 'wb'))
file_hot_minded.writerow(['date', 'transaction_vol'])

day_list = set(user_data.time)
# find the transaction of each day contributed by hot minded buyer
for day in day_list:
    day_data = user_data[user_data.time == day]
    deal_day_data = day_data[day_data.behavior_type == 4]
    hot_minded_transaction_count = 0
    
    user_list = list(deal_day_data.user_id)
    category_list = list(deal_day_data.item_category)
    item_list = list(deal_day_data.item_id)
    
    # judge whether a "buy" action is a crazy one
    for i in range(0, len(deal_day_data)):
                
        # does the user have any other behavior on this item before?
        previous_data = user_data[user_data.user_id == user_list[i]] 
        previous_data = previous_data[previous_data.item_id == item_list[i]]
        previous_data = previous_data[previous_data.time < day]
        
        if len(previous_data) == 0:
            hot_minded_transaction_count = hot_minded_transaction_count + 1
            break
        
        # does the user have less than 10 behaviors on the category before?
        previous_data = user_data[user_data.user_id == user_list[i]]
        previous_data = previous_data[previous_data.item_category == category_list[i]]
        previous_data = previous_data[previous_data.time < day]
        
        if len(previous_data) <= 10:
            hot_minded_transaction_count = hot_minded_transaction_count + 1
            
    # output to file
    file_hot_minded.writerow([day, hot_minded_transaction_count])

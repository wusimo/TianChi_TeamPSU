import pandas as pd
import numpy as np
import json
from collections import defaultdict
import csv

# read in data
data = pd.read_csv("./tianchi_mobile_recommend_train_user.csv")
#data2 = data[data.behavior_type==2]
#data3 = data[data.behavior_type==3] # all the behavior of type:add to cart
user_list = set(data.user_id)   # obtain the set of all users

potential_user_category = defaultdict(list)
for user in user_list:
    user_data = data[data.user_id==user]    # the tables only contains the information of each individual user
    user_buy_data = user_data[user_data.behavior_type==4]
    
    if len(user_buy_data)<5:#poor guy fuck off
        print 'poor guy'
        continue
    
    user_category_list = set(user_data.item_category)
    for category_id in user_category_list:
        user_category_table = user_data[user_data.item_category==category_id]
        if (4 in user_category_table.behavior_type.values) or ( 3 in user_category_table.behavior_type.values):
            print 'already bought'
            continue
        if len(user_category_table) < 3:
            print 'not enough information'
            continue
        
        last_interaction_time = int(max(user_category_table.time.values).replace("-","").replace(" ",""))
        if last_interaction_time < 2014121500:
                print 'not active'
                continue
        
        user_item_list = set(user_category_table.item_id)  # the set contains all categories 'interested' by user
    
    
        for item_id in user_item_list:
            user_item_table = user_data[user_data.item_id==item_id]
        
            
            last_interaction_time = int(max(user_item_table.time.values).replace("-","").replace(" ",""))
        
            if last_interaction_time < 2014121500:
                print 'item not active'
                continue
        
            total_interaction_time = len(user_item_table) 
            if total_interaction_time < 4:
                print 'item not interested in'
                continue
            
            potential_user_category[user].append(item_id)

# output this dictionary to a file
writer = csv.writer(open('potential_user_item_after_time_filtering.csv', 'wb'))
for key, value in potential_user_category.items():
    writer.writerow([key,value])

    
# if you want to read this dictionary file
# reader = csv.reader(open('potential_user_category.csv','rb'))
# potential_user_category = dict(x for x in reader)    
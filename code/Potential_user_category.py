import pandas as pd
import numpy as np
import json
from collections import defaultdict
# read in data
data=pd.read_csv("D:/Anaconda/tianchi_mobile_recommend_train_user.csv")
data2=data[data.behavior_type==2]
# all the behavior of type:add to cart 
data3=data[data.behavior_type==3]
user_list=set(data.user_id)# obtain the set of all users
potential_user_category=defaultdict(list)
for user in user_list:
    user_data=data[data.user_id==user]# the tables only contains the information of each individual user
    user_item_category_list=set(user_data.item_category)# the set contains all categories 'interested' by user
    for category in user_item_category_list:
        user_item_in_certain_category=user_data[user_data.item_category==category]
        if 3 in user_item_in_certain_category.behavior_type.values and 4 not in user_item_in_certain_category.behavior_type.values:
            potential_user_category[user].append(category)
# output this dictionary to a file
writer = csv.writer(open('potential_user_category.csv','wb'))
for key, value in potential_user_category.items():
    writer.writerow([key,value])
# if you want to read this dictionary file
# reader = csv.reader(open('potential_user_category.csv','rb'))
# potential_user_category = dict(x for x in reader)
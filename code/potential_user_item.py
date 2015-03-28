import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict
# read in data
data = pd.read_csv("D:/Anaconda/tianchi_mobile_recommend_train_user.csv")


## data cleaning for the potential_user_item_category list
# read in the predict list of item and category
predict_item = pd.read_csv("D:/Anaconda/tianchi_mobile_recommend_train_item.csv")
# read in the potential user category list
reader = csv.reader(open('potential_user_category.csv','rb'))
potential_user_category = dict(x for x in reader)
# finding potential user_item pairs
potential_user_category_list = defaultdict(list)
for key in potential_user_category.keys():
    #construct the user_category_list
    user_category_list = potential_user_category[key].split(",")
    user_category_list[0] = user_category_list[0][1:]
    user_category_list[-1] = user_category_list[-1][:-1]
    #
    for category in user_category_list:
        # if the user's interest category is not in the must be predicted list, then we can get rid off it
        if int(category) not in predict_item.item_category.values:
            user_category_list.remove(category)
    if len(user_category_list):# which means the list is not empty
        potential_user_category_list[key] = user_category_list


def user_category_table(user,item_category,data):
    user_table = data[data.user_id == user]
    user_table_1 = user_table[user_table.item_category == item_category]
    user_table = user_table_1[user_table.behavior_type == 3]
    user_table_1 = user_table.sort('time')
    return user_table
        
        
potential_user_item = defaultdict(set)        
for key in potential_user_category_list.keys():
    for category in potential_user_category_list[key]:
        # Construct user_category_table
        A_table = user_category_table(int(key),int(category),data)
        user_item_table=A_table[A_table.behavior_type == 3]
        B_table = predict_item[predict_item.item_category == int(category)]
        item_set = set(A_table.item_id).intersection(set(B_table.item_id))
        if len(item_set):
            potential_user_item[int(key)] = item_set 

writer = csv.writer(open('potential_user_item.csv','wb'))
for key, value in potential_user_category.items():
    writer.writerow([key,value])
# if you want to read this dictionary file
# reader = csv.reader(open('potential_user_item.csv','rb'))
# potential_user_category = dict(x for x in reader)
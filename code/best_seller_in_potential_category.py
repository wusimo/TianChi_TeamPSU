import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict

# read in data
user_data = pd.read_csv("F:/activities/tianchi_mobile_recommend_train_user.csv")
potential_item_info = pd.read_csv("F:/activities/TianChi_TeamPSU/data/tianchi_mobile_recommend_train_item.csv")

potential_item = set(potential_item_info.item_id)
potential_category = set(potential_item_info.item_category)

file_potential_best_seller = csv.writer(open("F:/activities/TianChi_TeamPSU/data/potential_best_seller.csv", 'wb'))
file_potential_best_seller.writerow(['category', 'item'])

for category in potential_category:
    category_data = user_data[user_data.item_category == category]
    category_data = category_data[category_data.behavior_type == 4]
    
    item_list = set(category_data.item_id)
    item_index = 0
    item_sales = 0
    for item in item_list:
        item_data = category_data[category_data.item_id == item]
        if item_sales < len(item_data):
            item_sales = len(item_data)
            item_index = item
    
    if item_index in item_list:
        file_potential_best_seller.writerow([category, item_index])
## it finds the best seller in each potential category
#  the result is stored in best_seller_in_potential_category.csv
#

import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict

# read in user data and potential(forecast) item information
user_data = pd.read_csv("F:/activities/tianchi_mobile_recommend_train_user.csv")
potential_item_info = pd.read_csv("F:/activities/TianChi_TeamPSU/data/tianchi_mobile_recommend_train_item.csv")

potential_item = set(potential_item_info.item_id) # items need to be forecasted
potential_category = set(potential_item_info.item_category) # categories need to be forecasted

file_potential_best_seller = csv.writer(open("F:/activities/TianChi_TeamPSU/data/best_seller_in_potential_category.csv", 'wb'))
file_potential_best_seller.writerow(['category', 'item'])

# find best seller in each potential category 
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
    
    # if the best seller is also in potential item list
    if item_index in potential_item:
        file_potential_best_seller.writerow([category, item_index])
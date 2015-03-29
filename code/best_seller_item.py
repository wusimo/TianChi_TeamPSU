import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict

# read in data
data=pd.read_csv("F:/activities/TianChi/tianchi_mobile_recommend_train_user.csv")
category_list = set(data.item_category)

file_best_seller = csv.writer(open("F:/activities/TianChi/TianChi_TeamPSU/data/best_seller_item.csv", 'wb'))
file_best_seller.writerow(['category', 'item'])

for category in category_list:
    category_data = data[data.item_category==category]
    category_data = category_data[category_data.behavior_type==4]
    item_list = set(category_data.item_id)
    item_index = 0
    item_sales = 0
    for item in item_list:
        item_data = category_data[category_data.item_id==item]
        if item_sales < len(item_data) + 1:
            item_sales = len(item_data) + 1
            item_index = item
    file_best_seller.writerow([category, item_index])

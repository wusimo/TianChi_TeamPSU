## it obtains the interseption of potential_user_item with
#  best seller in each potential category
#

import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict

potential_user_item_reader = csv.reader(open('F:/activities/TianChi_TeamPSU/data/' \
                                             'potential_user_item.csv', 'rb'))
potential_user_item_info = dict(x for x in potential_user_item_reader)
potential_best_seller_info = pd.read_csv('F:/activities/TianChi_TeamPSU/data/best' \
                                         '_seller_in_potential_category.csv')

file_prediction = csv.writer(open('F:/activities/TianChi_TeamPSU/data/prediction_' \
                                  'by_best_seller_intercept_potential_deal.csv', 'wb'))
file_prediction.writerow(['user_id', 'item_id'])

best_seller_list = list(potential_best_seller_info.item)
for i in range(0, len(best_seller_list)):
    best_seller_list[i] = str(best_seller_list[i])[0:-2]
    
best_seller_set = set(best_seller_list)

for user in potential_user_item_info.keys():
    item_list = potential_user_item_info[user][5:-2].split(',')
    for item in item_list:
        if item in best_seller_set:
            file_prediction.writerow([user, item])
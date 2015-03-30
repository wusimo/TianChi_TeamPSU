## it obtains each day's transaction volume
#  the result is stored in each_day_transaction_volume.csv
#

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

file_transaction_volume = csv.writer(open("F:/activities/TianChi_TeamPSU/data/each_day_transaction_volume.csv", 'wb'))
file_transaction_volume.writerow(['date', 'transaction_volume'])

# obtain the transaction volume of each day
day_list = set(user_data.time)
for day in day_list:
    day_data = user_data[user_data.time == day]
    transaction_data = day_data[day_data.behavior_type == 4]
    transaction_vol = len(transaction_data)
    file_transaction_volume.writerow([day, transaction_vol])

import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict

# read in data
data = pd.read_csv("F:/activities/tianchi_mobile_recommend_train_user.csv")

for i in range(0, len(data)):
    data.time[i] = data.time[i][0: 10]
    
normal_days_data = data[data.time != "2014-11-11"]
normal_days_data = normal_days_data[normal_days_data.time != "2014-12-12"]

transaction_times = len(normal_days_data[normal_days_data.behavior_type == 4])
avrg_transaction_times = transaction_times / 28
print avrg_transaction_times

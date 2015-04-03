# code used for randomly selecting 1000 users for test data and save them into thousand_selected_data(Panda Frame)
import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict
import random
# read in data
data = pd.read_csv("D:/Anaconda/tianchi_mobile_recommend_train_user.csv")
#data2 = data[data.behavior_type==4]
user_set = set(data.user_id.values)
selected_user_set = random.sample(user_set, 1000)
selected_data = data[data['user_id'].isin(selected_user_set)]
selected_data.to_csv('thousand_selected_data', sep='\t', encoding='utf-8')

# if you want to read this file
#pd.read_csv("thousand_selected_data")
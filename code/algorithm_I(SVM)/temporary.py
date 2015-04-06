import pandas as pd
import csv
from collections import defaultdict

a=0
criteria1 = 0.3

# read in potential_user_item_after_time_filtering
reader = csv.reader(open('D:/TianChi/TianChi_TeamPSU/data/algorithm_I/potential_user_item_after_time_filtering.csv', 'rb'))
potential_user_item_after_time_filtering = dict(x for x in reader)

data = pd.read_csv("D:/Anaconda/tianchi_mobile_recommend_train_user.csv")

# read in user_behavior_table
user_behavior_statistics = pd.read_csv("D:/TianChi/TianChi_TeamPSU/data/Algorithm_II/user_behavior_statistics.csv")

# read in need to be predicted item_list
predict_item = pd.read_csv("D:/TianChi/TianChi_TeamPSU/data/tianchi_mobile_recommend_train_item.csv")

item_set = set(predict_item.item_id)

potential_user_item_list = defaultdict(list)

for key in potential_user_item_after_time_filtering.keys():
        
        user = int(key)
        user_behavior = user_behavior_statistics[user_behavior_statistics.user_id==int(key)]
        if int(user_behavior.cycle_bought_itm_avrg.values[0]) > 30:# which means this user is unpredictable
            continue
        user_item_list = potential_user_item_after_time_filtering[key].split(",")
        user_item_list[0] = user_item_list[0][1:]
        user_item_list[-1] = user_item_list[-1][:-1]
        
        for item in user_item_list:
            if int(item) not in item_set:
                continue
            user_item_table = data[(data.user_id==user)&(data.item_id)==int(item)]
            a+=1
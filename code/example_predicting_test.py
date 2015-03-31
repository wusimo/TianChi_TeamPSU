import pandas as pd
import numpy as np
import json
import csv
from collections import defaultdict
# read in data

# example predict and forcasting code

data = pd.read_csv("D:/Anaconda/tianchi_mobile_recommend_train_user.csv")
data2 = data[data.behavior_type==4]
# pick a crazy buyer
datatest = data2[data2.user_id == 142391834]
# learning the centroid
a,b=predict_centroid(142391834,data)
# predicting 
c=0
for i in range(0,len(datatest)):
    if not forecasting(142391834,int(datatest.item_id.values[i]),a,b,data,datatest.time.values[i]):
        c+=1
error_rate = c/len(datatest)
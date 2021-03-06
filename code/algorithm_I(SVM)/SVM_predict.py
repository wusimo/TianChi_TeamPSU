from sklearn import svm
import pandas as pd
import csv

#data = pd.read_csv("D:/Anaconda/tianchi_mobile_recommend_train_user.csv")
reader = csv.reader(open('/Users/Simo/TianChi_TeamPSU/data/potential_user_item.csv','rb'))
potential_user_item = dict(x for x in reader)
writer = csv.writer(open('/Users/Simo/Documents/Tianchi_local/predicting_list_test.csv','wb'))

for i in range(0,7):#len(potential_user_item.items())
    user = int(potential_user_item.items()[i][0])
    #def SVM_training(user,data,alpha,beta)
    
    user_table = data[data.user_id==user].sort('time')
    bought_table = user_table[user_table.behavior_type==4]
    user_bought = set(bought_table.item_id.values)    
    user_bought_list_x = []
    user_bought_list_y = []
    user_unbought_list_x = []
    user_unbought_list_y = []
    user_buy_list = []
    user_unbuy_list = []
    alpha=6
    beta=0.5
    
    if len(bought_table):
        
        for item in user_bought:
        
            table = user_table[user_table.item_id==item]
            buy_time = min(table[table.behavior_type==4].time)
            table = table[table.time<=buy_time]
            category = user_table[user_table.item_id==item].item_category.values[0]
            unbought_table = user_table[user_table.item_category==category]
            unbought_table = unbought_table[unbought_table.item_id!=item]
            unbought_table = unbought_table[unbought_table.time<buy_time]
            for ii in range(0,len(table)):
                a = 600/((int(buy_time.replace("-","").replace(" ",""))+1-int(table.time.values[ii].replace("-","").replace(" ","")))**beta)
                b = int(table.behavior_type.values[ii])**alpha
                user_bought_list_x.append(a)
                user_bought_list_y.append(b)
                for jj in range(0,len(unbought_table)):
                    a = 600/((int(buy_time.replace("-","").replace(" ",""))+1-int(unbought_table.time.values[jj].replace("-","").replace(" ","")))**beta)
                    b = int(unbought_table.behavior_type.values[jj])**alpha
                    user_unbought_list_x.append(a)
                    user_unbought_list_y.append(b)
                    if len(user_bought_list_x)&len(user_unbought_list_x):#create 2 barycenter used for forcasting
                        x = [p for p in user_bought_list_x]
                        y = [p for p in user_bought_list_y]
                        buy_centroid = [sum(x) / len(user_bought_list_x), sum(y) / len(user_bought_list_y)]

                        x = [p for p in user_unbought_list_x]
                        y = [p for p in user_unbought_list_y]
                        unbuy_centroid = [sum(x) / len(user_unbought_list_x), sum(y) / len(user_unbought_list_y)]
                        user_buy_list.append(buy_centroid)
                        user_unbuy_list.append(unbuy_centroid)
    
        
    user_buy_list.extend(user_unbuy_list)
    fitting_list = user_buy_list
    #fitting_list.append(user_unbuy_list)
    temp_list = [1 for ii in range(0,len(user_buy_list)-len(user_unbuy_list))]
    temp_list.extend([0 for ii in range(0,len(user_unbuy_list))])
    label_list = temp_list
    if fitting_list:
        clf = svm.SVC()
        clf.fit(fitting_list, label_list)  
        
        
        item_list = potential_user_item.items()[i][1][5:-2].split(",")
        buy_date = "2014-12-19 06"
        for jjj in range(0,len(item_list)):
        
            table = user_table[user_table.item_id==int(item_list[jjj])]
            table = table[table.time<buy_date]
            list_x = []
            list_y = []
            for iiii in range(0,len(table)):
                a = 600/((int(buy_date.replace("-","").replace(" ",""))+1-int(table.time.values[iiii].replace("-","").replace(" ","")))**beta)
                b = int(table.behavior_type.values[iiii])**alpha
                list_x.append(a)
                list_y.append(b)
        if len(list_x)!=0:
            x = [p for p in list_x]
            y = [p for p in list_y]
            centroid = (sum(x) / len(list_x), sum(y) / len(list_y))
            if clf.predict(centroid):
                writer.writerow([user,int(item_list[jjj])])
                        
                   

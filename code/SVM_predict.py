from sklearn import svm

data = pd.read_csv("D:/Anaconda/tianchi_mobile_recommend_train_user.csv")
reader = csv.reader(open('potential_user_item.csv','rb'))
potential_user_item = dict(x for x in reader)
writer = csv.writer(open('predicting_list.csv','wb'))

for i in range(0,len(potential_user_item.items())):
    user = int(potential_user_item.items()[i][0])
    #datatest = data2[data2.user_id == user]
    # learning the centroid
    user_table = data[data.user_id==user_id]
    user_table = user_table.sort('time')
    full_set = set(user_table.item_id.values)
    bought_table = user_table[user_table.behavior_type==4]
    #the set of all items bought by user
    user_bought = set(bought_table.item_id.values)
    
    user_bought_list_x = []
    user_bought_list_y = []

    user_unbought_list_x = []
    user_unbought_list_y = []

    user_buy_list = []
    user_unbuy_list = []

    for item in user_bought:
        table = user_table[user_table.item_id==item]
        buy_time = min(table[table.behavior_type==4].time)
        table = table[table.time<buy_time]
        category = user_table[user_table.item_id==item].item_category.values[0]
        unbought_table = user_table[user_table.item_category==category]
        unbought_table = unbought_table[unbought_table.item_id!=item]
        unbought_table = unbought_table[unbought_table.time<buy_time]
        for i in range(0,len(table)):
            a = 600/((int(buy_time.replace("-","").replace(" ",""))-int(table.time.values[i].replace("-","").replace(" ","")))**beta)
            b = int(table.behavior_type.values[i])**alpha
            user_bought_list_x.append(a)
            user_bought_list_y.append(b)
        for j in range(0,len(unbought_table)):
            a = 600/((int(buy_time.replace("-","").replace(" ",""))-int(unbought_table.time.values[j].replace("-","").replace(" ","")))**beta)
            b = int(unbought_table.behavior_type.values[j])**alpha
            user_unbought_list_x.append(a)
            user_unbought_list_y.append(b)
        if len(user_bought_list_x)&len(user_unbought_list_x):#create 2 barycenter used for forcasting
            x = [p for p in user_bought_list_x]
            y = [p for p in user_bought_list_y]
            buy_centroid = (sum(x) / len(user_bought_list_x), sum(y) / len(user_bought_list_y))

            x = [p for p in user_unbought_list_x]
            y = [p for p in user_unbought_list_y]
            unbuy_centroid = (sum(x) / len(user_unbought_list_x), sum(y) / len(user_unbought_list_y))
        
            user_buy_list.append(buy_centroid)
            user_unbuy_list.append(unbuy_centroid)
    
    fitting_list = []
    fitting_list.append(user_buy_list).append(user_unbuy_list)
    label_list = [1 for i in range(0,len(user_buy_list))].append([0 for i in range(0,len(user_unbuy_list))])
    
    clf = svm.SVC()
    clf.fit(fitting_list, label_list)  
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
    gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
    shrinking=True, tol=0.001, verbose=False)
    
    item_list = potential_user_item.items()[i][1][5:-2].split(",")
    buy_date = "2014-12-19 06"
    for j in range(0,len(item_list)):
        
        table = user_table[user_table.item_id==item_id]
        table = table[table.time<buy_date]
        list_x = []
        list_y = []
        for i in range(0,len(table)):
                a = 600/((int(buy_date.replace("-","").replace(" ",""))-int(table.time.values[i].replace("-","").replace(" ","")))**beta)
                b = int(table.behavior_type.values[i])**alpha
                list_x.append(a)
                list_y.append(b)
        if len(list_x)!=0:
            x = [p for p in list_x]
            y = [p for p in list_y]
            centroid = (sum(x) / len(list_x), sum(y) / len(list_y))
            if clf.predict[centroid]:
                writer.writerow([user,int(item_list[j])])



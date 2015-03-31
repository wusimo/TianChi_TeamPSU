# SVM for a single user using history buying and not buying information
def predict_centroid(user_id,data,alpha=6,beta=0.5):
    user_table = data[data.user_id==user_id]
    user_table = user_table.sort('time')
    full_set = set(user_table.item_id.values)
    bought_table = user_table[user_table.behavior_type==4]
    #the set of all items bought by user
    user_bought = set(bought_table.item_id.values)
    #the set of all items did not bought by but take action by user
    user_unbought = full_set.difference_update(user_bought)
    # constructing plot information
    
    user_bought_list_x = []
    user_bought_list_y = []

    user_unbought_list_x = []
    user_unbought_list_y = []

    alpha=6
    beta=0.5

    for item in user_bought:
        table = user_table[user_table.item_id==item]
        buy_time = min(table[table.behavior_type==4].time)
        table = table[table.time<buy_time]
        category = user_table[user_table.item_id==item].item_category.values[0]
        unbought_table = user_table[user_table.item_category==category]
        unbought_table = unbought_table[unbought_table.item_id!=item]
        unbought_table = unbought_table[unbought_table.time<buy_time]
        for i in range(0,len(table)):
            a = (int(buy_time.replace("-","").replace(" ",""))-int(table.time.values[i].replace("-","").replace(" ","")))**beta
            b = int(table.behavior_type.values[i])**alpha
            user_bought_list_x.append(a)
            user_bought_list_y.append(b)
        for j in range(0,len(unbought_table)):
            a = (int(buy_time.replace("-","").replace(" ",""))-int(unbought_table.time.values[j].replace("-","").replace(" ","")))**beta
            b = int(unbought_table.behavior_type.values[j])**alpha
            user_unbought_list_x.append(a)
            user_unbought_list_y.append(b)

    #create 2 barycenter used for forcasting
    x = [p for p in user_bought_list_x]
    y = [p for p in user_bought_list_y]
    buy_centroid = (sum(x) / len(user_bought_list_x), sum(y) / len(user_bought_list_y))

    x = [p for p in user_unbought_list_x]
    y = [p for p in user_unbought_list_y]
    unbuy_centroid = (sum(x) / len(user_unbought_list_x), sum(y) / len(user_unbought_list_y))
    return(buy_centroid,unbuy_centroid)
    #forcasting
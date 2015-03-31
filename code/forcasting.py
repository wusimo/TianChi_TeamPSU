def forecasting(user_id,item_id,buy_centroid,unbuycentroid,data,buy_date,alpha=6,beta=0.5):
    alpha=6
    beta=0.5
    table = data[data.user_id==user_id]
    table = table[table.item_id==item_id]
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
        a = (centroid[0]-buy_centroid[0])**2+(centroid[1]-buy_centroid[1])**2
        b = (centroid[0]-unbuy_centroid[0])**2+(centroid[1]-unbuy_centroid[1])**2
        if a>b:
            return False
        else:
            return True
    else:
        return False
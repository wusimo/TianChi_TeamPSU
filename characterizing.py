import pandas as pd
#data = pd.read_csv("/Users/Simo/Documents/Tianchi_local/data/tianchi_mobile_recommend_train_user.csv")
#user_behavior_statistics = pd.read_csv("/Users/Simo/TianChi_TeamPSU/data/algorithm_II/user_behavior_statistics.csv")
def characterizing(data,user_behavior_statistics,user_id,item_id,predicting_date=0,alpha=6,beta=0.5):
    alpha=6
    beta=0.5
    user_behavior_table = user_behavior_statistics[user_behavior_statistics.user_id==user_id]
    user_click_list = []
    user_add_list = []
    user_table = data[data.user_id==user_id]
    user_item_table = user_table[user_table.item_id==item_id]
    user_item_table = user_item_table.sort('time')
    if not predicting_date:
        buy_time = min(user_item_table[user_item_table.behavior_type==4].time)
        predicting_date = int(buy_time.replace("-","").replace(" ",""))
    else:
        buy_time = predicting_date
    user_item_table = user_item_table[user_item_table.time<=buy_time]
    click_times = len(user_item_table[user_item_table.behavior_type==1])
    click_table = user_item_table[user_item_table.behavior_type==1]
    for i in range(0,len(click_table)):
        a = ((predicting_date+1-int(click_table.time.values[i].replace("-","").replace(" ",""))))
        user_click_list.append(a)  
    
    add_times = len(user_item_table[user_item_table.behavior_type==2])
    add_table = user_item_table[user_item_table.behavior_type==2]
    for i in range(0,len(add_table)):
        a = ((predicting_date+1-int(add_table.time.values[i].replace("-","").replace(" ",""))))
        user_add_list.append(a)
    if len(user_click_list)&int(user_behavior_table.cycle_bought_itm_avrg.values[0]):
        click_centroid = float(sum(user_click_list))/len(user_click_list)
        click_centroid = float(click_centroid)/(float(user_behavior_table.cycle_bought_itm_avrg.values[0])*100)
        if len(user_add_list)&int(user_behavior_table.behavior_2_bought_itm_avrg.values[0]):
            add_centroid = float(sum(user_add_list))/len(user_add_list)
            click_times = float(click_times)/float((user_behavior_table.behavior_2_bought_itm_avrg.values[0])*100)
        else:
            add_times = 0.0
            add_centroid = 0.0
            
        return(click_times,click_centroid,add_times,add_centroid)
    else:
        return(0.0,0.0,0.0,0.0)
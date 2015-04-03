##it finds some statistics of user behavior
# results are saved in a table

# total times of different behaviors
def behaviors_total(usr_data):
    
    behavior_1_totl = len(usr_data[usr_data.behavior_type == 1])
    behavior_2_totl = len(usr_data[usr_data.behavior_type == 2])
    behavior_3_totl = len(usr_data[usr_data.behavior_type == 3])
    behavior_4_totl = len(usr_data[usr_data.behavior_type == 4])
    
    return([behavior_1_totl, behavior_2_totl, behavior_3_totl, behavior_4_totl])

# average times of different behaviors on bought item
def behavior_bought_item_average(usr_data, bought_item_set):

    # if the user didn't buy any staff
    if len(bought_item_set) == 0:
        return([0, 0, 0])
    
    behavior_1_bought_itm_sum = 0
    behavior_2_bought_itm_sum = 0
    behavior_3_bought_itm_sum = 0
    
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        itm_bought_data = itm_data[itm_data.behavior_type == 4]
        first_bought_time = itm_bought_data.time[0]
        itm_data = itm_data[itm_data.time <= first_bought_time] # user behavior data on bought item before 
                                                                # the first bought time
        
        behavior_1_bought_itm_sum = behavior_1_bought_itm_sum + len(itm_data[itm_data.behavior_type == 1])
        behavior_2_bought_itm_sum = behavior_2_bought_itm_sum + len(itm_data[itm_data.behavior_type == 2])
        behavior_3_bought_itm_sum = behavior_3_bought_itm_sum + len(itm_data[itm_data.behavior_type == 3])
        
    behavior_1_bought_itm_avrg = behavior_1_bought_itm_sum / len(bought_item_set)
    behavior_2_bought_itm_avrg = behavior_2_bought_itm_sum / len(bought_item_set)
    behavior_3_bought_itm_avrg = behavior_3_bought_itm_sum / len(bought_item_set)
    
    return([behavior_1_bought_itm_avrg, behavior_2_bought_itm_avrg, behavior_3_bought_itm_avrg])


# average times of different behaviors on unbought item
def behavior_unbought_item_average(usr_data, unbought_item_set):

    if len(unbought_item_set) == 0:
        return([0, 0, 0])
    
    behavior_1_unbought_itm_sum = 0
    behavior_2_unbought_itm_sum = 0
    behavior_3_unbought_itm_sum = 0
    
    for itm in unbought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        behavior_1_unbought_itm_sum = behavior_1_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 1])
        behavior_2_unbought_itm_sum = behavior_2_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 2])
        behavior_3_unbought_itm_sum = behavior_3_unbought_itm_sum + len(itm_data[itm_data.behavior_type == 3])
        
    behavior_1_unbought_itm_avrg = behavior_1_itm_unbought_sum / len(unbought_item_set)
    behavior_2_unbought_itm_avrg = behavior_2_itm_unbought_sum / len(unbought_item_set)
    behavior_3_unbought_itm_avrg = behavior_3_itm_unbought_sum / len(unbought_item_set)
    
    return([behavior_1_unbought_itm_avrg, behavior_2_unbought_itm_avrg, behavior_3_unbought_itm_avrg])


# average times of different behaviors on bought category
def behavior_bought_category_average(usr_data, bought_category_set):
    
    if len(bought_category_set) == 0:
        return([0, 0, 0])
    
    behavior_1_bought_catg_sum = 0
    behavior_2_bought_catg_sum = 0
    behavior_3_bought_catg_sum = 0
    
    for catg in bought_category_set:
        catg_data = usr_data[usr_data.item_category == catg]
        catg_bought_data = catg_data[catg_data.behavior_type == 4]
        first_bought_time = catg_bought_data.time[0]
        catg_data = catg_data[catg_data.time <= first_bought_time] # user behavior data on bought category before 
                                                                   # the first bought time
        
        behavior_1_bought_catg_sum = behavior_1_bought_catg_sum + len(catg_data[catg_data.behavior_type == 1])
        behavior_2_bought_catg_sum = behavior_2_bought_catg_sum + len(catg_data[catg_data.behavior_type == 2])
        behavior_3_bought_catg_sum = behavior_3_bought_catg_sum + len(catg_data[catg_data.behavior_type == 3])
        
    behavior_1_bought_catg_avrg = behavior_1_bought_catg_sum / len(bought_catg_set)
    behavior_2_bought_catg_avrg = behavior_2_bought_catg_sum / len(bought_catg_set)
    behavior_3_bought_catg_avrg = behavior_3_bought_catg_sum / len(bought_catg_set)
    
    return([behavior_1_bought_catg_avrg, behavior_2_bought_catg_avrg, behavior_3_bought_catg_avrg])


# average times of different behaviors on unbought category
def behavior_unbought_category_average(usr_data, unbought_category_set):
    
    if len(unbought_category_set) == 0:
        return([0, 0, 0])
    
    behavior_1_unbought_catg_sum = 0
    behavior_2_unbought_catg_sum = 0
    behavior_3_unbought_catg_sum = 0
    
    for catg in unbought_category_set:
        catg_data = usr_data[usr_data.item_category == catg]
        behavior_1_unbought__catg_sum = behavior_1_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 1])
        behavior_2_unbought_catg_sum = behavior_2_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 2])
        behavior_3_unbought_catg_sum = behavior_3_unbought_catg_sum + len(catg_data[catg_data.behavior_type == 3])
        
    behavior_1_unbought_catg_avrg = behavior_1_unbought_catg_sum / len(unbought_category_set) 
    behavior_2_unbought_catg_avrg = behavior_2_unbought_catg_sum / len(unbought_category_set)
    behavior_3_unbought_catg_avrg = behavior_3_unbought_catg_sum / len(unbought_category_set)
    
    return([behavior_1_unbought_catg_avrg, behavior_2_unbought_catg_avrg, behavior_3_unbought_catg_avrg])


# average times of different behaviors on similiar items with respect to bought item
def behavior_similar_item_average(usr_data, bought_item_set):
    
    if len(bought_item_set) == 0:
        return([0, 0, 0])
    
    behavior_1_similar_item_sum = 0
    behavior_2_similar_item_sum = 0
    behavior_3_similar_item_sum = 0
    
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        catg = itm_data.item_category[0]
        itm_bought_data = itm_data[itm_data.behavior_type == 4]
        first_bought_time = itm_bought_data.time[0]
        catg_data = usr_data[usr_data.item_category == catg]
        catg_data = catg_data[catg_data.time <= first_bought_time]
        similar_itm_set = set(catg_data.item_id).difference(set(itm)) # similar items in the same category
        
        if len(similar_itm_set) == 0:
            continue
            
        behavior_1_similar_within_sum = 0
        behavior_2_similar_within_sum = 0
        behavior_3_similar_within_sum = 0
        
        for within_itm in similar_itm_set:
            within_itm_data = catg_data[catg_data.item_id == within_itm]
            behavior_1_similar_within_sum = behavior_1_similar_within_sum + len(within_itm_data.behavior_type == 1)
            behavior_2_similar_within_sum = behavior_2_similar_within_sum + len(within_itm_data.behavior_type == 2)
            behavior_3_similar_within_sum = behavior_3_similar_within_sum + len(within_itm_data.behavior_type == 3)
    
        behavior_1_similar_sum = behavior_1_similar_sum + behavior_1_similar_within_sum / len(similar_itm_set)
        behavior_2_similar_sum = behavior_2_similar_sum + behavior_2_similar_within_sum / len(similar_itm_set)
        behavior_3_similar_sum = behavior_3_similar_sum + behavior_3_similar_within_sum / len(similar_itm_set)

    behavior_1_similar_avrg = behavior_1_similar_sum / len(bought_item_set)
    behavior_2_similar_avrg = behavior_2_similar_sum / len(bought_item_set)
    behavior_3_similar_avrg = behavior_3_similar_sum / len(bought_item_set)
    
    return([behavior_1_similar_avrg, behavior_2_similar_avrg, behavior_3_similar_avrg])


# cycle on bought item, from the very begining of browing that item to the end of buying it
def cycle_bought_item(usr_data, bought_item_set):
    
    if len(bought_item_set) == 0:
        return 1000
    
    cycle_bought_itm_sum = 0
    for itm in bought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        begin_behavior_time = itm_data.time[0]
        itm_bought_data = itm_data[itm_dat.behavior_type == 4]
        first_bought_time = itm_bought_data.time[0]
        cycle_bought_itm_sum = cycle_bought_itm_sum + first_bought_time - begin_behavior_time + 1
    
    cycle_bought_itm_avrg = cycle_bought_itm_sum / len(bought_item_set)
    
    return cycle_bought_itm_avrg

# cycle on unbought item, from the very begining of browing that item to the end of buying it
def cycle_unbought_item(usr_data, unbought_item_set):
    
    if len(unbought_item_set) == 0:
        return 1000
    
    cycle_unbought_itm_sum = 0
    for itm in unbought_item_set:
        itm_data = usr_data[usr_data.item_id == itm]
        begin_behavior_time = itm_data.time[0]
        end_behavior_time = itm_data.time[len(itm_data)-1]
        cycle_unbought_itm_sum = cycle_unbought_itm_sum + end_behavior_time - begin_behavior_time + 1
    
    cycle_unbought_itm_avrg = cycle_unbought_itm_sum / len(unbought_item_set)
    
    return cycle_unbought_itm_avrg

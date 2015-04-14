def train_data_extraction(rootFile, orgn_data_file, train_data_file):
    # read in tianchi_mobile_recommend_train_user.csv
    orgn_data = pd.read_csv(rootFile + orgn_data_file)

    # get the time difference to 2014-01-01 00
    orgn_data["timdiff"] = 0.0
    for i in range(0, len(orgn_data)):
        record_time = time.strptime(orgn_data.time.values[i], '%Y-%m-%d %H')
        orgn_data.timdiff.values[i] = (record_time.tm_yday - 1) * 24 + record_time.tm_hour

    # sort the data by time
    orgn_data = orgn_data.sort_index(by=['user_id', 'item_category', 'timdiff'], ascending = [1, 1, 1])
    orgn_data.to_csv(rootFile + 'tianchi_mobile_recommend_train_user.csv',\
                      sep=',', index=False, encoding='utf-8')

    # partition date
    par_time = time.strptime('2014-12-17 23', '%Y-%m-%d %H')
    par_time_diff = par_time.tm_yday * 24

    # save the training data
    train_data = orgn_data[orgn_data.timdiff <= par_time_diff]
    train_data.to_csv(rootFile + train_data_file, sep=',', index=False, encoding='utf-8')
    
    return [orgn_data, train_data]

##############
#
#
#
#############

def sample_preparation(orgn_data, train_data, rootFile, sample_data_file):
    # read in tianchi_mobile_recommend_train_user.csv

    # partition time
    par_time = time.strptime('2014-12-17 23', '%Y-%m-%d %H')
    par_time_diff = par_time.tm_yday * 24

    # train_data
    #train_data = orgn_data[orgn_data.timdiff <= par_time_diff]
    user_set = set(train_data.user_id)

    test_data = orgn_data[orgn_data.timdiff > par_time_diff]
    item_set = set(test_data.item_id)
    category_set = set(train_data.item_category)


    # attributes of users, items, and categories
    user_att = {} # total buying times in the past month
    item_att = {} # total sales in the past two weeks
    category_att = {} # total sales in the past two weeks

    for usr in user_set:
        usr_data = train_data[train_data.user_id == usr]
        usr_bgt_data = usr_data[usr_data.behavior_type == 4]
        user_att[usr] = float(len(usr_bgt_data))

    # 2014-12-03 ~ 2014-12-17
    par_time = time.strptime('2014-12-03 00', '%Y-%m-%d %H')
    par_time_diff = par_time.tm_yday * 24

    for itm in item_set:
        itm_data = train_data[train_data.item_id == itm]
        itm_two_wk_data = itm_data[itm_data.timdiff >= par_time_diff]
        itm_two_wk_bgt_data = itm_two_wk_data[itm_two_wk_data.behavior_type == 4]
        item_att[itm] = float(len(itm_two_wk_bgt_data))

    for catg in category_set:
        catg_data = train_data[train_data.item_category == catg]
        catg_two_wk_data = catg_data[catg_data.timdiff >= par_time_diff]
        catg_two_wk_bgt_data = catg_two_wk_data[catg_two_wk_data.behavior_type == 4]
        category_att[catg] = float(len(catg_two_wk_bgt_data))
    
    
    sample_data = []
    test_date = datetime.strptime('2014-12-18', '%Y-%m-%d')
    for usr in user_set:
        for itm in item_set:
        
            train_usr_data = train_data[train_data.user_id == usr]
            train_usr_itm_data = train_usr_data[train_usr_data.item_id == itm]
        
            # usr never had too few behavior on itm during the training period
            if len(train_usr_itm_data) < 5:
                continue
            # usr once bought itm during the training period
            train_usr_itm_bgt_data = train_usr_itm_data[train_usr_itm_data.behavior_type == 4]
            if len(train_usr_itm_bgt_data):
                continue
        
            test_itm_data = test_data[test_data.item_id == itm]
            catg = test_itm_data.item_category.values[0]
        
            usr_att = user_att[usr]
            itm_att = item_att[itm]
            catg_att = category_att[catg]
    
            usr_data = train_data[train_data.user_id == usr]
            usr_itm_data = usr_data[usr_data.item_id == itm]
            bh_1 = float(len(usr_itm_data[usr_itm_data.behavior_type == 1]))
            bh_2 = float(len(usr_itm_data[usr_itm_data.behavior_type == 2]))
            bh_3 = float(len(usr_itm_data[usr_itm_data.behavior_type == 3]))
    
            lst_bh_time = max(usr_itm_data.timdiff)
            lst_bh_data = usr_itm_data[usr_itm_data.timdiff == lst_bh_time]
            lst_bh_date_str = lst_bh_data.time.values[0][0:10]
            lst_bh_date = datetime.strptime(lst_bh_date_str, '%Y-%m-%d')
            lst_bh_diff = float((test_date - lst_bh_date).days + 1)
    
            fst_bh_time = min(usr_itm_data.timdiff)
            fst_bh_data = usr_itm_data[usr_itm_data.timdiff == fst_bh_time]
            fst_bh_date_str = fst_bh_data.time.values[0][0:10]
            fst_bh_date = datetime.strptime(fst_bh_date_str, '%Y-%m-%d')
            fst_bh_diff = float((test_date - fst_bh_date).days + 1)
          
            test_itm_usr_data = test_itm_data[test_itm_data.user_id == usr]
            test_itm_usr_bgt_data = test_itm_usr_data[test_itm_usr_data.behavior_type == 4]
            if len(test_itm_usr_bgt_data) == 0: # usr didn't buy itm on 2014-12-18
                sample_data.extend([(usr, itm, usr_att, itm_att, catg_att, bh_1, bh_2, bh_3, lst_bh_diff, fst_bh_diff, 0)])
            else: # usr bought itm on 2014-12-18
                sample_data.extend([(usr, itm, usr_att, itm_att, catg_att, bh_1, bh_2, bh_3, lst_bh_diff, fst_bh_diff, 1)])


    df = pd.DataFrame(sample_data)
    df.columns = ('user_id', 'item_id', 'user_att', 'item_att', 'category_att',\
                  'bh_1_tol', 'bh_2_tol', 'bh_3_tol', 'lst_bh_diff', 'fst_bh_diff', 'group')
    df.to_csv(rootFile + 'sample.csv', sep=',', index=False, encoding='utf-8') 
    
    return df
    
##############
#
#
#
#############

def SVM_method(sample_data, rootFile, svm_file):
    X = []
    y = []

    for i in range(0, len(sample_data)):
        usr_att = sample_data.user_att.values[i]
        itm_att = sample_data.item_att.values[i]
        catg_att = sample_data.category_att.values[i]
    
        bh_1 = sample_data.bh_1_tol.values[i]
        bh_2 = sample_data.bh_2_tol.values[i]
        bh_3 = sample_data.bh_3_tol.values[i]
    
        lst_bh_diff = sample_data.lst_bh_diff.values[i]
        fst_bh_diff = sample_data.fst_bh_diff.values[i]
    
        grp = sample_data.group.values[i]
    
        X.extend([(usr_att, itm_att, catg_att, bh_1, bh_2, bh_3, lst_bh_diff, fst_bh_diff)])
        y.extend([grp])

    clf = svm.SVC()
    clf.fit(X, y)

    joblib.dump(clf, rootFile + svm_file)

##############
#
# MAIN BODY
#
#############

import pandas as pd
import csv
import time
from sklearn import svm
from datetime import datetime
from sklearn.externals import joblib


rootFile = 'F:/activities/TianChi/data/'
orgn_data_file = 'tianchi_mobile_recommend_train_user.csv'
train_data_file = 'train_tianchi_mobile_recommend_train_user.csv'
sample_data_file = 'sample.csv'
svm_file = 'zrm_SVM.pkl'

[orgn_data, train_data] = train_data_extraction(rootFile, orgn_data_file, train_data_file)
sample_data = sample_preparation(orgn_data, train_data, rootFile, sample_data_file)
svm_data = SVM_method(sample_data, rootFile, svm_file)

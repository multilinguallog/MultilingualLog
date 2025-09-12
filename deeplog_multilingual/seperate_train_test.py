import pandas as pd

# target_file = './data/BGL/English/BGL_English.log_structured.csv'
# train_file = './data/BGL/English/BGL_English_train.log_structured.csv'
# test_file = './data/BGL/English/BGL_English_test.log_structured.csv'
#
# target_df = pd.read_csv(target_file)
# headers = target_df.columns.to_list()
#
# num_test = int(len(target_df)*0.9)
# train_list = []
# test_list = []
# for index, row in target_df.iterrows():
#     if index < num_test:
#         test_list.append(row.to_list())
#     else:
#         train_list.append(row.to_list())
#
# train_df = pd.DataFrame(train_list, columns=headers)
# test_df = pd.DataFrame(test_list, columns=headers)
# train_df.to_csv(train_file, index=False)
# test_df.to_csv(test_file, index=False)

datasets = ['Apache', 'BGL', 'Hadoop', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']

for dataset in datasets:
    print(dataset)
    target_file = './data/' + dataset + '/Mix/' + dataset + '_mixed.log_structured.csv'
    train_file = './data/' + dataset + '/Mix/' + dataset + '_mixed_train.log_structured.csv'
    test_file = './data/' + dataset + '/Mix/' + dataset + '_mixed_test.log_structured.csv'

    target_df = pd.read_csv(target_file)
    # headers = ['LineId','Date','Time', 'Translated','Tokenized','Content','EventId']
    # headers = ['LineId','Time','Translated','Content','EventId']
    # headers = ['LineId','Logrecord','Date','Time','Pid','Level','Component','ADDR','Content','EventId','EventTemplate']
    headers = target_df.columns.to_list()

    num_test = int(len(target_df)*0.9)
    train_list = []
    test_list = []
    for index, row in target_df.iterrows():
        if index < num_test:
            test_list.append(row.to_list())
        else:
            train_list.append(row.to_list())

    train_df = pd.DataFrame(train_list, columns=headers)
    test_df = pd.DataFrame(test_list, columns=headers)
    train_df.to_csv(train_file, index=False)
    test_df.to_csv(test_file, index=False)
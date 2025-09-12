import pandas as pd
import random

def assign_groups(lst, n_groups=5):
    random.shuffle(lst)  # 打乱顺序
    k, m = divmod(len(lst), n_groups)
    group_dict = {}
    start = 0
    for i in range(n_groups):
        end = start + k + (1 if i < m else 0)
        for item in lst[start:end]:
            group_dict[item] = i + 1  # 1 for Chinese, 2 for English, 3 for Japanese, 4 for Korean, 5 for French
        start = end
    return group_dict

datasets = ['Apache', 'BGL', 'Hadoop', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']

for dataset in datasets:
    mixed_info_file = '../data/downstream/data/' + dataset + '/translated_file/Mixed/Mixed_info.csv'
    mixed_file_csv = '../data/downstream/data/' + dataset + '/translated_file/Mixed/mixed_log.csv'
    mixed_file_log = '../data/downstream/data/' + dataset + '/translated_file/Mixed/mixed_log.log'

    mixed_info_df = pd.read_csv(mixed_info_file)
    event_id_list = list(dict.fromkeys(mixed_info_df['EventId'].to_list()))
    event_id_dict = assign_groups(event_id_list)
    log_file_writer = open(mixed_file_log, 'w')

    for index, row in mixed_info_df.iterrows():
        event_id = row['EventId']
        match event_id_dict[event_id]:
            case 1:
                content = row['Chinese']
                content = content.replace('\n', '')
                log_file_writer.write(content + '\n')
            case 2:
                content = row['Content']
                content = content.replace('\n', '')
                log_file_writer.write(content + '\n')
            case 3:
                content = row['Japanese']
                content = content.replace('\n', '')
                log_file_writer.write(content + '\n')
            case 4:
                content = row['Korean']
                content = content.replace('\n', '')
                log_file_writer.write(content + '\n')
            case 5:
                content = row['French']
                content = content.replace('\n', '')
                log_file_writer.write(content + '\n')

    log_file_writer.close()
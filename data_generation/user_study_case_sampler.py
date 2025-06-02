import pandas as pd
import random

def generate_user_study_df(user_study_cases_df):
    user_study_df = pd.DataFrame(columns=['Origin', 'Translated_A', 'Translated_B', 'GroundTruth'])
    for index, row in user_study_cases_df.iterrows():
        ori_log = row['Origin']
        translated_log_template = row['Translated']
        translated_log_line = row['TranslatedByLine']

        change_flag = random.randint(0, 1)
        if change_flag == 0:
            user_study_row = [ori_log, translated_log_template, translated_log_line, 'A']
            user_study_df.loc[len(user_study_df)] = user_study_row
        else:
            user_study_row = [ori_log, translated_log_line, translated_log_template, 'B']
            user_study_df.loc[len(user_study_df)] = user_study_row
    return user_study_df

datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']
# datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']
language = 'French'
sample_size = 10

for dataset in datasets:
    user_study_pool_file = '../../output/Userstudy/V2/' + language + '/pool/' + dataset + '_userstudy.csv'
    user_study_file = '../../output/Userstudy/V2/' + language + '/sample/' + dataset + '_userstudy.csv'
    user_study_pool_df = pd.read_csv(open(user_study_pool_file))
    pool_size = user_study_pool_df.shape[0]
    if pool_size > sample_size:
        rows = user_study_pool_df.sample(n=sample_size)
        user_study_df = generate_user_study_df(rows)
        user_study_df.to_csv(user_study_file)
    else:
        user_study_df = generate_user_study_df(user_study_pool_df)
        user_study_df.to_csv(user_study_file)
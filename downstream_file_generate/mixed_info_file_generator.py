import pandas as pd

datasets = ['Apache', 'BGL', 'Hadoop', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']

for dataset in datasets:
    French_file = '../data/downstream/data/' + dataset + '/translated_file/French/' + dataset + '_translated.csv'
    Chinese_file = '../data/downstream/data/' + dataset + '/translated_file/Chinese/' + dataset + '_tokenized.csv'
    Japanese_file = '../data/downstream/data/' + dataset + '/translated_file/Japanese/' + dataset + '_tokenized.csv'
    Korean_file = '../data/downstream/data/' + dataset + '/translated_file/Korean/' + dataset + '_tokenized.csv'

    Mixed_info_file = '../data/downstream/data/' + dataset + '/translated_file/Mixed/Mixed_info.csv'

    french_df = pd.read_csv(French_file)
    french_df = french_df.rename(columns={'Translated':'French'})
    chinese_df = pd.read_csv(Chinese_file)[['Tokenized']]
    chinese_df = chinese_df.rename(columns={'Tokenized':'Chinese'})
    korean_df = pd.read_csv(Korean_file)[['Tokenized']]
    korean_df = korean_df.rename(columns={'Tokenized':'Korean'})
    japanese_df = pd.read_csv(Japanese_file)[['Tokenized']]
    japanese_df = japanese_df.rename(columns={'Tokenized':'Japanese'})

    mixed_df = pd.concat([french_df, chinese_df, korean_df, japanese_df], axis=1)
    mixed_df.to_csv(Mixed_info_file, index=False)
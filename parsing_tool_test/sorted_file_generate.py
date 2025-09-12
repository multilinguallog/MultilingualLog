import os
import pandas as pd

event_file_prefix = '../output/LibreLog/origin/Japanese/'
log_file_prefix = '../output/tokenized_log/Japanese/'
output_file_folder = '../output/LibreLog/sorted/Japanese/'

os.makedirs(output_file_folder, exist_ok=True)

datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'Proxifier', 'Spark', 'Zookeeper']

for dataset in datasets:
    print(dataset)
    event_file = event_file_prefix + dataset + '/3.csv'
    log_file = log_file_prefix + dataset + '_tokenized.log'
    output_file = output_file_folder + dataset + '.log_structured.csv'

    event_df = pd.read_csv(event_file)
    logs = open(log_file, 'r').readlines()
    output_df = pd.DataFrame(columns=['Content', 'EventTemplate'])

    for log in logs:
        log = log.replace('\n', '')
        related_df = event_df[event_df['Content'] == log]
        template = related_df.iloc[0]['RegexTemplate']
        if len(list(dict.fromkeys(related_df['RegexTemplate'].to_list()))) > 1:
            print("Parsing error")
        new_row = [log, template]
        output_df.loc[len(output_df)] = new_row

    output_df.to_csv(output_file, index=False)
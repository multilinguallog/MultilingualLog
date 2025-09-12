import pandas as pd

groundtruth_file = '../data/downstream/data/Zookeeper/translated_file/Korean/Zookeeper_translated.csv'
parsed_file = '../data/downstream/parsed/Zookeeper/Mixed/mixed_log.log_structured.csv'
downstream_file = '../data/downstream/parsed/Zookeeper/Mixed/Zookeeper_mixed.log_structured.csv'

groundtruth_df = pd.read_csv(groundtruth_file)
parsed_df = pd.read_csv(parsed_file)

# merged_df = pd.concat([groundtruth_df[['LineId', 'Date', 'Time', 'Translated', 'Tokenized']],
#                       parsed_df[['Content', 'EventId']]],
#                       axis=1)
merged_df = pd.concat([groundtruth_df[['LineId', 'Date','Time']],
                      parsed_df[['Content', 'EventId']]],
                      axis=1)
merged_df.to_csv(downstream_file, index=False)
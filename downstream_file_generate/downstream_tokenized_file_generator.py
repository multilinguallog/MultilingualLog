import pandas as pd
import sys

import jieba
from mecab import MeCab
from sudachipy import Dictionary, SplitMode

datasets = ['Apache', 'BGL', 'Hadoop', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'Proxifier', 'Spark', 'Zookeeper']
datasets = ['Spark']

tokenizer_obj = Dictionary().create()

for dataset in datasets:
    print(dataset)
    translated_file = '../data/downstream/data/' + dataset + '/translated_file/Japanese/' + dataset + '_translated.csv'
    tokenized_file_csv = '../data/downstream/data/' + dataset + '/translated_file/Japanese/' + dataset + '_tokenized.csv'
    tokenized_file_log = '../data/downstream/data/' + dataset + '/translated_file/Japanese/' + dataset + '_tokenized.log'

    translated_df = pd.read_csv(translated_file)
    headers = list(translated_df.columns) + ['Tokenized']
    tokenized_log_writer = open(tokenized_file_log, 'w')
    tokenized_output = []

    total = len(translated_df)
    for index, row in translated_df.iterrows():
        percent = (int(index) / total) * 100
        sys.stdout.write(f"\rProcessing: {percent:.2f}%")
        sys.stdout.flush()
        translated_content = row['Translated']
        translated_content = translated_content.replace('\n', '')

        tokens_sudachi = tokens = [m.surface() for m in tokenizer_obj.tokenize(translated_content, SplitMode.A)]
        tokenized_log_sudachi = " ".join(tokens_sudachi)
        new_row = row.to_list() + [tokenized_log_sudachi]

        tokenized_output.append(new_row)
        tokenized_log_writer.write(tokenized_log_sudachi + '\n')

    tokenized_log_writer.close()
    tokenized_df = pd.DataFrame(tokenized_output, columns=headers)
    tokenized_df.to_csv(tokenized_file_csv, index=False)

# translated_file = '../data/downstream/data/BGL/translated_file/Korean/BGL_translated.csv'
# tokenized_file_csv = '../data/downstream/data/BGL/translated_file/Korean/BGL_tokenized.csv'
# tokenized_file_log = '../data/downstream/data/BGL/translated_file/Korean/BGL_tokenized.log'
#
# translated_df = pd.read_csv(translated_file)
# headers = list(translated_df.columns) + ['Tokenized']
# tokenized_log_writer = open(tokenized_file_log, 'w')
# tokenized_output = []

"""Chinese"""
# total = len(translated_df)
# for index, row in translated_df.iterrows():
#     percent = (int(index) / total) * 100
#     sys.stdout.write(f"\rProcessing: {percent:.2f}%")
#     sys.stdout.flush()
#     translated_content = row['Translated']
#     translated_content = translated_content.replace('\n', '')
#     tokenized_content_tokens = list(jieba.cut(translated_content))
#     tokenized_content = " ".join(tokenized_content_tokens)
#     new_row = row.to_list() + [tokenized_content]
#     tokenized_output.append(new_row)
#     tokenized_log_writer.write(tokenized_content + '\n')
#
# tokenized_log_writer.close()
# tokenized_df = pd.DataFrame(tokenized_output, columns=headers)
# tokenized_df.to_csv(tokenized_file_csv, index=False)

"""Japanese"""
# tokenizer_obj = Dictionary().create()
# total = len(translated_df)
# for index, row in translated_df.iterrows():
#     percent = (int(index) / total) * 100
#     sys.stdout.write(f"\rProcessing: {percent:.2f}%")
#     sys.stdout.flush()
#     translated_content = row['Translated']
#     translated_content = translated_content.replace('\n', '')
#
#     tokens_sudachi = tokens = [m.surface() for m in tokenizer_obj.tokenize(translated_content, SplitMode.A)]
#     tokenized_log_sudachi = " ".join(tokens_sudachi)
#     new_row = row.to_list() + [tokenized_log_sudachi]
#     tokenized_output.append(new_row)
#     tokenized_log_writer.write(tokenized_log_sudachi + '\n')
#
# tokenized_log_writer.close()
# tokenized_df = pd.DataFrame(tokenized_output, columns=headers)
# tokenized_df.to_csv(tokenized_file_csv, index=False)

"""Korean"""
# mecab_tokenizer = MeCab()
# total = len(translated_df)
# for index, row in translated_df.iterrows():
#     percent = (int(index) / total) * 100
#     sys.stdout.write(f"\rProcessing: {percent:.2f}%")
#     sys.stdout.flush()
#     translated_content = row['Translated']
#     translated_content = translated_content.replace('\n', '')
#
#     tokens_mecab = mecab_tokenizer.morphs(translated_content)
#     tokenized_log_mecab = " ".join(tokens_mecab)
#     new_row = row.to_list() + [tokenized_log_mecab]
#     tokenized_output.append(new_row)
#     tokenized_log_writer.write(tokenized_log_mecab + '\n')
#
# tokenized_log_writer.close()
# tokenized_df = pd.DataFrame(tokenized_output, columns=headers)
# tokenized_df.to_csv(tokenized_file_csv, index=False)
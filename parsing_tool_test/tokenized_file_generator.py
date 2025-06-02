import jieba
import thulac
# from mecab import MeCab
from sudachipy import Dictionary, SplitMode

datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']
# thulac_tokenizer = thulac.thulac(seg_only=True)
# mecab_tokenizer = MeCab()
tokenizer_obj = Dictionary().create()

"""Tokenized file generator for Chinese log"""
# for dataset in datasets:
#     log_file = 'translated_log/Chinese/' + dataset + '_translated.log'
#     tokenized_log_file_jieba = 'tokenized_log/Chinese/Jieba/' + dataset + '_tokenized.log'
#     tokenized_log_file_thulac = 'tokenized_log/Chinese/THULAC/' + dataset + '_tokenized.log'
#     tokenized_file_writer_jieba = open(tokenized_log_file_jieba, 'w')
#     tokenized_file_writer_thulac = open(tokenized_log_file_thulac, 'w')
#
#     loglines = open(log_file, 'r').readlines()
#     for log in loglines:
#         log = log.replace('\n', '')
#
#         tokens_jieba = list(jieba.cut(log))
#         tokenized_log_jieba = " ".join(tokens_jieba)
#         tokenized_file_writer_jieba.write(tokenized_log_jieba + '\n')
#
#         tokenized_log_thulac = thulac_tokenizer.cut(log, text=True)
#         tokenized_file_writer_thulac.write(tokenized_log_thulac + '\n')
#
#     tokenized_file_writer_jieba.close()
#     tokenized_file_writer_thulac.close()

"""Tokenized file generator for Korean log"""
# for dataset in datasets:
#     log_file = 'translated_log/Korean/' + dataset + '_translated.log'
#     tokenized_log_file_mecab = 'tokenized_log/Korean/MeCab/' + dataset + '_tokenized.log'
#     tokenized_file_writer_mecab = open(tokenized_log_file_mecab, 'w')
#
#     loglines = open(log_file, 'r').readlines()
#     for log in loglines:
#         log = log.replace('\n', '')
#
#         tokens_mecab = mecab_tokenizer.morphs(log)
#         tokenized_log_mecab = " ".join(tokens_mecab)
#         tokenized_file_writer_mecab.write(tokenized_log_mecab + '\n')
#
#     tokenized_file_writer_mecab.close()

"""Tokenized file generator for Japanese log"""
for dataset in datasets:
    log_file = 'translated_log/Japanese/' + dataset + '_translated.log'
    tokenized_log_file_sudachi = 'tokenized_log/Japanese/sudachi/' + dataset + '_tokenized.log'
    tokenized_file_writer_sudachi = open(tokenized_log_file_sudachi, 'w')

    loglines = open(log_file, 'r').readlines()
    for log in loglines:
        log = log.replace('\n', '')

        tokens_sudachi = tokens = [m.surface() for m in tokenizer_obj.tokenize(log, SplitMode.A)]
        tokenized_log_sudachi = " ".join(tokens_sudachi)
        tokenized_file_writer_sudachi.write(tokenized_log_sudachi + '\n')

    tokenized_file_writer_sudachi.close()
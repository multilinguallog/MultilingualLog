from log_translator import LogTranslator_event

datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']
# datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']

for dataset in datasets:
    event_file = '../../data/original/' + dataset + '/' + dataset + '_content_2k_event.csv'
    template_file = '../../output/Template/V2/French/' + dataset + '/' + dataset + '_translated.csv'
    log_col = 'Log'
    template_col = 'Template'
    ori_col = 'Template'
    translated_col = 'Translated'
    translated_log_file = '../../output/Template/V2/French/' + dataset + '/' + dataset + '_translated.log'
    translated_event_file = '../../output/Template/V2/French/' + dataset + '/' + dataset + '_translated_event.csv'
    translator = LogTranslator_event(event_file, log_col, template_col, template_file, ori_col, translated_col,
                                     translated_log_file, translated_event_file)
    translator.translate()

# event_file = '../../data/original/Apache_content_2k_event.csv'
# template_file = '../../output/Apache_translated.csv'
# log_col = 'Log'
# template_col = 'Template'
# ori_col = 'Template'
# translated_col = 'Translated'
# translated_log_file = '../../output/Apache_translated.log'
#
# translator = LogTranslator_event(event_file, log_col, template_col, template_file, ori_col, translated_col, translated_log_file)
# translator.translate()
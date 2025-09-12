from data_generation.log_translator import LogTranslator_event

datasets = ['Apache', 'BGL', 'Hadoop', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'Proxifier', 'Spark', 'Zookeeper']

for dataset in datasets:
    event_file = '../data/downstream/data/' + dataset + '/' + dataset + '_structured.csv'
    template_file = '../data/downstream/data/' + dataset + '/' + dataset + '.Chinese_translated.csv'
    log_col = 'Content'
    template_col = 'EventTemplate'
    ori_col = 'Template'
    translated_col = 'Translated'
    translated_log_file = '../data/downstream/data/' + dataset + '/translated_file/Chinese/' + dataset + '_translated.log'
    translated_event_file = '../data/downstream/data/' + dataset + '/translated_file/Chinese/' + dataset + '_translated.csv'
    translator = LogTranslator_event(event_file, log_col, template_col, template_file, ori_col, translated_col,
                                     translated_log_file, translated_event_file)
    translator.translate_csv()
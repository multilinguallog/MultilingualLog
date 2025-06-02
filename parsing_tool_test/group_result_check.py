import pandas as pd
import os

def calculate_group_consistency(origin_parsed_file, parsed_result_file):
    df_origin = pd.read_csv(origin_parsed_file)
    df_parsedlog = pd.read_csv(parsed_result_file)

    n_inconsistency = 0
    for index_o, row_o in df_origin.iterrows():
        index_list_o = df_origin[df_origin['EventId'] == row_o['EventId']].index.to_list()
        row_p = df_parsedlog.iloc[index_o]
        index_list_p = df_parsedlog[df_parsedlog['EventId'] == row_p['EventId']].index.to_list()

        if index_list_p != index_list_o:
            n_inconsistency += 1
    print(float((2000 - n_inconsistency) / 2000))

def calculate_group_accuracy(groundtruth_file, parsed_result_file):
    df_groundtruth = pd.read_csv(groundtruth_file)
    df_parsedlog = pd.read_csv(parsed_result_file)

    n_inaccuracy = 0
    for index_g, row_g in df_groundtruth.iterrows():
        index_list_g = df_groundtruth[df_groundtruth['OriTemplate'] == row_g['OriTemplate']].index.to_list()
        row_p = df_parsedlog.iloc[index_g]
        index_list_p = df_parsedlog[df_parsedlog['EventId'] == row_p['EventId']].index.to_list()

        if index_list_p != index_list_g:
            n_inaccuracy += 1
    print(float((2000 - n_inaccuracy) / 2000))

def check_group_accuracy(groundtruth_file, parsed_result_file, check_result_file_structured, check_result_file_template):
    df_check_structured = pd.DataFrame(
        columns=['Origin', 'Translated', 'OriTemplate', 'TranslatedTemplate', 'EventTemplate'])
    df_check_template = pd.DataFrame(
        columns=['Origin', 'Translated', 'OriTemplate', 'TranslatedTemplate', 'EventTemplate'])

    df_groundtruth = pd.read_csv(groundtruth_file)
    df_parsedlog = pd.read_csv(parsed_result_file)

    event_dict = dict()
    n_inaccuracy = 0
    for index_g, row_g in df_groundtruth.iterrows():
        index_list_g = df_groundtruth[df_groundtruth['OriTemplate'] == row_g['OriTemplate']].index.to_list()
        row_p = df_parsedlog.iloc[index_g]
        index_list_p = df_parsedlog[df_parsedlog['EventId'] == row_p['EventId']].index.to_list()

        if index_list_p != index_list_g:
            log_ori = row_g['Origin']
            log_translated = row_p['Content']
            template_ori = row_g['OriTemplate']
            template_g = row_g['TranslatedTemplate']
            template_p = row_p['EventTemplate']
            check_result_row = [log_ori, log_translated, template_ori, template_g, template_p]
            n_inaccuracy += 1

            df_check_structured.loc[len(df_check_structured)] = check_result_row

            if template_g in event_dict.keys():
                if template_p in event_dict[template_g]:
                    pass
                else:
                    event_dict[template_g].append(template_p)
                    df_check_template.loc[len(df_check_template)] = check_result_row
            else:
                event_dict[template_g] = [template_p]
                df_check_template.loc[len(df_check_template)] = check_result_row
    print(float((2000-n_inaccuracy)/2000))

    df_check_structured.to_csv(check_result_file_structured)
    df_check_template.to_csv(check_result_file_template)

def check_group_consistency(origin_parsed_file, parsed_result_file, check_result_file_structured, check_result_file_template):
    df_check_structured = pd.DataFrame(
        columns=['Origin', 'Translated', 'OriTemplate', 'TranslatedTemplate'])
    df_check_template = pd.DataFrame(
        columns=['Origin', 'Translated', 'OriTemplate', 'TranslatedTemplate'])

    df_origin = pd.read_csv(origin_parsed_file)
    df_parsedlog = pd.read_csv(parsed_result_file)

    event_dict = dict()
    n_inconsistency = 0
    for index_o, row_o in df_origin.iterrows():
        index_list_o = df_origin[df_origin['EventId'] == row_o['EventId']].index.to_list()
        row_p = df_parsedlog.iloc[index_o]
        index_list_p = df_parsedlog[df_parsedlog['EventId'] == row_p['EventId']].index.to_list()

        if index_list_p != index_list_o:
            log_ori = row_o['Content']
            log_translated = row_p['Content']
            template_ori = row_o['EventTemplate']
            template_p = row_p['EventTemplate']
            check_result_row = [log_ori, log_translated, template_ori, template_p]
            n_inconsistency += 1

            df_check_structured.loc[len(df_check_structured)] = check_result_row

            if template_ori in event_dict.keys():
                if template_p in event_dict[template_ori]:
                    pass
                else:
                    event_dict[template_ori].append(template_p)
                    df_check_template.loc[len(df_check_template)] = check_result_row
            else:
                event_dict[template_ori] = [template_p]
                df_check_template.loc[len(df_check_template)] = check_result_row
    print(float((2000-n_inconsistency)/2000))

    df_check_structured.to_csv(check_result_file_structured)
    df_check_template.to_csv(check_result_file_template)

datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']
# datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'OpenSSH', 'OpenStack', 'Proxifier', 'Zookeeper']
datasets = ['Apache', 'BGL', 'HDFS', 'HealthApp', 'HPC', 'Mac', 'OpenStack', 'Spark']

for dataset in datasets:
    """check group accuracy"""
    print(dataset)
    groundtruth_file = 'translated_log/groundtruth/Chinese/' + dataset + '/' + dataset + '_translated_event.csv'
    parsed_result_file = 'parsing_result/NuLog/Origin/' + dataset + '/' + dataset + '.log_structured.csv'
    # parsed_result_file = 'parsing_result/Drain/Origin/' + dataset + '/' + dataset + '_tokenized.log_structured.csv'
    # parsed_result_file = 'parsing_result/Spell/French/' + dataset + '/' + dataset + '_translated.log_structured.csv'
    check_result_folder = 'group_check_result/groundtruth/NuLog/Origin/' + dataset
    check_result_file_structured = check_result_folder + '/' + dataset + '_check_structured.csv'
    check_result_file_template = check_result_folder + '/' + dataset + '_check_template.csv'

    os.makedirs(check_result_folder, exist_ok=True)

    # check_group_accuracy(groundtruth_file, parsed_result_file, check_result_file_structured, check_result_file_template)
    calculate_group_accuracy(groundtruth_file, parsed_result_file)

    """check group consistency"""
    # print(dataset)
    # origin_parsed_file = 'parsing_result/NuLog/Origin/' + dataset + '/' + dataset + '.log_structured.csv'
    # # origin_parsed_file = 'parsing_result/PILAR/Origin/' + dataset + '/' + dataset + '_tokenized.log_structured.csv'
    # parsed_result_file = 'parsing_result/NuLog/Korean/' + dataset + '/' + dataset + '_tokenized.log_structured.csv'
    # # parsed_result_file = 'parsing_result/NuLog/Japanese/' + dataset + '/' + dataset + '_translated.log_structured.csv'
    # check_result_folder = 'group_check_result/ori_parsing_result/NuLog/Korean/' + dataset
    # check_result_file_structured = check_result_folder + '/' + dataset + '_check_structured.csv'
    # check_result_file_template = check_result_folder + '/' + dataset + '_check_template.csv'
    #
    # # os.makedirs(check_result_folder, exist_ok=True)
    #
    # # check_group_consistency(origin_parsed_file, parsed_result_file, check_result_file_structured, check_result_file_template)
    # calculate_group_consistency(origin_parsed_file, parsed_result_file)


# groundtruth_file = 'translated_log/groundtruth/Chinese/BGL/BGL_translated_event.csv'
# parsed_result_file = 'parsing_result/Drain/Chinese/BGL/BGL_tokenized.log_structured.csv'
#
# check_result_file_structured = 'group_check_result/BGL_check_structured.csv'
# check_result_file_template = 'group_check_result/BGL_check_template.csv'

# df_check_structured = pd.DataFrame(columns=['Origin', 'Translated', 'OriTemplate', 'TranslatedTemplate', 'EventTemplate'])
# df_check_template = pd.DataFrame(columns=['Origin', 'Translated', 'OriTemplate', 'TranslatedTemplate', 'EventTemplate'])
#
# df_groundtruth = pd.read_csv(groundtruth_file)
# df_parsedlog = pd.read_csv(parsed_result_file)
#
# event_list_groundtruth = list(dict.fromkeys(df_groundtruth['OriTemplate'].to_list()))
# event_list_parsedlog = list(df_parsedlog['EventId'].to_list())
#
# event_dict = dict()
# for index_g, row_g in df_groundtruth.iterrows():
#     index_list_g = df_groundtruth[df_groundtruth['OriTemplate'] == row_g['OriTemplate']].index.to_list()
#     row_p = df_parsedlog.iloc[index_g]
#     index_list_p = df_parsedlog[df_parsedlog['EventId'] == row_p['EventId']].index.to_list()
#
#     if index_list_p != index_list_g:
#         log_ori = row_g['Origin']
#         log_translated = row_g['Translated']
#         template_ori = row_g['OriTemplate']
#         template_g = row_g['TranslatedTemplate']
#         template_p = row_p['EventTemplate']
#         check_result_row = [log_ori, log_translated, template_ori, template_g, template_p]
#
#         df_check_structured.loc[len(df_check_structured)] = check_result_row
#
#         if template_g in event_dict.keys():
#             if template_p in event_dict[template_g]:
#                 pass
#             else:
#                 event_dict[template_g].append(template_p)
#                 df_check_template.loc[len(df_check_template)] = check_result_row
#         else:
#             event_dict[template_g] = [template_p]
#             df_check_template.loc[len(df_check_template)] = check_result_row
#
# df_check_structured.to_csv(check_result_file_structured)
# df_check_template.to_csv(check_result_file_template)
import re
import pandas as pd

class LogTranslator_event:
    def __init__(self, event_file, log_col, template_col, template_file, ori_col, translated_col, translated_log_file, translated_event_file):
        self.event_file = event_file
        self.log_col = log_col
        self.template_col = template_col

        self.template_file = template_file
        self.ori_col = ori_col
        self.translated_col = translated_col

        self.translated_log_file = translated_log_file
        self.translated_event_file = translated_event_file

    def template_to_regex(self, template):
        regex = template
        regex = regex.replace("\\", "\\\\")
        regex = regex.replace(".", "\.")
        regex = regex.replace("*", "\*")

        regex = regex.replace("(", "\(")
        regex = regex.replace(")", "\)")

        regex = regex.replace("<\*>", "(.*)")

        regex = regex.replace("[", "\[")
        regex = regex.replace("]", "\]")

        regex = regex.replace("|", "\|")

        regex = regex.replace("+", "\+")
        regex = regex.replace("?", "\?")
        regex = regex.replace("$", "\$")
        regex = regex.replace("@", "\@")
        regex = regex.replace("^", "\^")

        # regex = regex.replace(":", "\:")
        # regex = regex.replace("\"", "\\\"")

        regex = regex + '$'

        return regex

    def translate(self):
        event_df = pd.read_csv(self.event_file)
        translated_df = pd.read_csv(self.template_file)
        translated_writer = open(self.translated_log_file, 'w')
        event_df_new = pd.DataFrame(columns=['Origin', 'Translated', 'OriTemplate', 'TranslatedTemplate'])

        for index, row in event_df.iterrows():
            ori_template = row[self.template_col]
            ori_log = row[self.log_col]

            translated_template = translated_df[translated_df[self.ori_col] == ori_template][self.translated_col].to_list()[0]
            translated_log = translated_template

            if ori_log == ori_template:
                translated_writer.write(translated_log + '\n')
                row_new = [ori_log, translated_log, ori_template, translated_template]
                event_df_new.loc[len(event_df_new)] = row_new
            else:
                regex = self.template_to_regex(ori_template)
                if re.match(regex, ori_log):
                    para_list = re.findall(regex, ori_log)[0]
                    if isinstance(para_list, tuple):
                        index_p = 0
                        while index_p < len(para_list):
                            dynamic_variable = para_list[index_p]
                            replace_symbol = '<d_' + str(index_p) + '>'
                            translated_log = translated_log.replace(replace_symbol, dynamic_variable)
                            index_p = index_p + 1
                        translated_writer.write(translated_log + '\n')
                        row_new = [ori_log, translated_log, ori_template, translated_template]
                        event_df_new.loc[len(event_df_new)] = row_new
                    else:
                        translated_log = translated_log.replace('<d_0>', para_list)
                        translated_writer.write(translated_log + '\n')
                        row_new = [ori_log, translated_log, ori_template, translated_template]
                        event_df_new.loc[len(event_df_new)] = row_new
                else:
                    print("ERROR! Cannot match the log with its corresponding template")

        event_df_new.to_csv(self.translated_event_file)

class LogTranslator:
    def __init__(self, template_file, ori_col, translated_col, logfile_ori, logfile_translated):
        self.template_file = template_file
        self.ori_col = ori_col
        self.translated_col = translated_col
        self.logfile_ori = logfile_ori
        self.logfile_translated = logfile_translated

    def template_to_regex(self, template):
        regex = template
        regex = regex.replace("\\", "\\\\")
        regex = regex.replace(".", "\.")
        regex = regex.replace("*", "\*")

        regex = regex.replace("(", "\(")
        regex = regex.replace(")", "\)")

        regex = regex.replace("<\*>", "(.*)")

        regex = regex.replace("[", "\[")
        regex = regex.replace("]", "\]")

        regex = regex.replace("|", "\|")

        regex = regex.replace("+", "\+")
        regex = regex.replace("?", "\?")
        regex = regex.replace("$", "\$")
        regex = regex.replace("@", "\@")
        regex = regex.replace("^", "\^")

        # regex = regex.replace(":", "\:")
        # regex = regex.replace("\"", "\\\"")

        regex = regex + '$'

        return regex

    def traslate(self):
        loglines_ori = open(self.logfile_ori).readlines()
        templates_df = pd.read_csv(self.template_file)
        templates_ori = templates_df[self.ori_col]
        templates_translated = templates_df[self.translated_col]
        translated_writer = open(self.logfile_translated, 'w')

        templates_translated_dict = {}
        template_index = 0
        while template_index < len(templates_ori):
            templates_translated_dict[templates_ori[template_index]] = templates_translated[template_index]
            template_index = template_index + 1

        constant_list = []
        regex_list = []
        template_ori_list = []
        for tmp_ori in templates_ori:
            if str(tmp_ori).__contains__('<*>'):
                regex = self.template_to_regex(tmp_ori)
                regex = '^' + regex
                regex_list.append(regex)
                template_ori_list.append(tmp_ori)
            else:
                constant_list.append(tmp_ori)

        for log in loglines_ori:
            if log in constant_list:
                log_translated = templates_translated_dict[log]
                translated_writer.write(log_translated)
            else:
                regex_index = 0
                while regex_index < len(regex_list):
                    regex = regex_list[regex_index]
                    tmp_ori = template_ori_list[regex_index]
                    tmp_translated = templates_translated_dict[tmp_ori]
                    if re.match(regex, log):
                        para_list = re.findall(regex, log)[0]
                        if isinstance(para_list, tuple):
                            n_para = len(para_list)
                            index_p = 0
                            log_translated = tmp_translated
                            while index_p < len(para_list):
                                dynamic_variable = para_list[index_p]
                                replace_symbol = '<d_' + str(index_p) + '>'
                                log_translated = log_translated.replace(replace_symbol, dynamic_variable)
                            translated_writer.write(log_translated)
                        else:
                            log_translated = tmp_translated.replace('<*>', para_list[0])
                            translated_writer.write(log_translated)
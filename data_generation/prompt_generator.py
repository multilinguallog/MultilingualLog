def template_format_changer(template):
    count = template.count('<*>')
    index = 0
    parts = template.split("<*>")
    new_template = parts[0]
    while index < count:
        replace_symbol = '<d_' + str(index) + '>'
        new_template = new_template + replace_symbol + parts[index+1]
        index = index+1
    return new_template

def prompt_generator(template):
    prompt_statement = "You are a logging practitioner. \
    You are provided with a log template written with English and you need to translate the log template into Chinese. \
    The output should be a translated log template written with Chinese."

    prompt_requirements = "You should follow the following requirements: \n\
    (1) The letter case of the translated template should be the same with original log template. \
    For example, there is an English log template: LDAP: SSL support unavailable \
    its corresponding translated Chinese log template should be: LDAP：SSL支持不可用 \
    LDAP and SSL should keep the same letter case with the original log template. \n\
    (2) The translated log template should pay attention to the order of dynamic information. \
    For example, there is an English log template: Node card VPD check: <d_0> node in processor card slot <d_1> do not match. VPD ecid <d_2>, found <d_3> \
    its corresponding translated Chinese log template should be: 节点卡VPD检查：处理器卡槽<d_1>中的<d_0>节点不匹配。VPD ecid为<d_2>,发现<d_3> \
    the order of the first dynamic information <d_0> and the second dynamic information <d_1> in original log template is changed in translated Chinese log template. \
    The reason is we need to keep the semantic information in translated Chinese log template is the same with the original English log template. \n\
    (3) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. \n\
    (4) Simple words like client should be translated. \n\
    (5) The output should only be the translated template"

    prompt_ori_template_header = "### log template:"

    new_template = template_format_changer(template)

    prompt = prompt_statement + '\n' + prompt_requirements + '\n' + prompt_ori_template_header + '\n' + new_template

    return prompt

def prommpt_generator_japanese(template):
    prompt_statement = "You are a logging practitioner. \
        You are provided with a log template written with English and you need to translate the log template into Japanese. \
        The output should be a translated log template written with Japanese."

    prompt_requirements = "You should follow the following requirements: \n\
        (1) The letter case of the translated template should be the same with original log template. \
        For example, there is an English log template: LDAP: SSL support unavailable \
        its corresponding translated Japanese log template should be: LDAP: SSLサポートは利用できません \
        LDAP and SSL should keep the same letter case with the original log template. \n\
        (2) The translated log template should pay attention to the order of dynamic information. \
        For example, there is an English log template: Node card VPD check: <d_0> node in processor card slot <d_1> do not match. VPD ecid <d_2>, found <d_3> \
        its corresponding translated Japanese log template should be: ノードカードVPDチェック：プロセッサーカードスロット<d_1>の<d_0>ノードが一致しません。VPD ecid <d_2>、検出 <d_3> \
        the order of the first dynamic information <d_0> and the second dynamic information <d_1> in original log template is changed in translated Chinese log template. \
        The reason is we need to keep the semantic information in translated Chinese log template is the same with the original English log template. \n\
        (3) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. \n\
        (4) Simple words like client should be translated. \n\
        (5) The output should only be the translated template"

    prompt_ori_template_header = "### log template:"

    new_template = template_format_changer(template)

    prompt = prompt_statement + '\n' + prompt_requirements + '\n' + prompt_ori_template_header + '\n' + new_template

    return prompt

def prompt_generator_french(template):
    prompt_statement = "You are a logging practitioner. \
        You are provided with a log template written with English and you need to translate the log template into French. \
        The output should be a translated log template written with French."

    prompt_requirements = "You should follow the following requirements: \n\
        (1) The letter case of the translated template should be the same with original log template. \
        For example, there is an English log template: LDAP: SSL support unavailable \
        its corresponding translated French log template should be: LDAP: support pour SSL non disponible \
        LDAP and SSL should keep the same letter case with the original log template. \n\
        (2) Simple words like client should be translated. \n\
        (3) The output should only be the translated template \n\
        (4) Some words are software engineering domain specific, you do not need to translate them into French"

    prompt_ori_template_header = "### log template:"

    new_template = template_format_changer(template)

    prompt = prompt_statement + '\n' + prompt_requirements + '\n' + prompt_ori_template_header + '\n' + new_template

    return prompt

def prompt_generator_korean(template):
    prompt_statement = "You are a logging practitioner. \
        You are provided with a log template written with English and you need to translate the log template into Korean. \
        The output should be a translated log template written with Korean."

    prompt_requirements = "You should follow the following requirements: \n\
        (1) The letter case of the translated template should be the same with original log template. \
        For example, there is an English log template: LDAP: SSL support unavailable \
        its corresponding translated Korean log template should be: LDAP: SSL 지원이 불가능합니다. \
        LDAP and SSL should keep the same letter case with the original log template. \n\
        (2) The translated log template should pay attention to the order of dynamic information. \
        For example, there is an English log template: Node card VPD check: <d_0> node in processor card slot <d_1> do not match. VPD ecid <d_2>, found <d_3> \
        its corresponding translated Korean log template should be: 노드 카드 VPD 검사: 프로세서 슬롯 <d_1>의 <d_0> 노드가 일치하지 않습니다. VPD ECID는 <d_2>이지만, <d_3>이 발견되었습니다. \
        the order of the first dynamic information <d_0> and the second dynamic information <d_1> in original log template is changed in translated Korean log template. \
        The reason is we need to keep the semantic information in translated Korean log template is the same with the original English log template. \n\
        (3) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. \n\
        (4) Simple words like client should be translated. \n\
        (5) The output should only be the translated template"

    prompt_ori_template_header = "### log template:"

    new_template = template_format_changer(template)

    prompt = prompt_statement + '\n' + prompt_requirements + '\n' + prompt_ori_template_header + '\n' + new_template

    return prompt

def prompt_generator_by_line(loglines):
    prompt_statement = """You are a logging practitioner.
    You are provided with 100 lines of logs and you need to translate these log into Chinese
    The output should only be 100 lines of translated logs written in Chinese. No explanation is needed."""

    prompt_requirements = """You should follow the following requirements:
    (1) The letter case of the translated template should be the same with original log template.
    For example, there is an English log template: LDAP: SSL support unavailable 
    its corresponding translated Chinese log template should be: LDAP：SSL支持不可用 
    LDAP and SSL should keep the same letter case with the original log template. 
    (2) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. 
    (3) Simple words like client should be translated. 
    (4) The translated logs should be separated with newline character like the input format"""

    prompt_log_lines_header = '#### Log lines:'

    prompt = prompt_statement + '\n' + '\n' + prompt_requirements + '\n' + '\n' + prompt_log_lines_header + '\n'
    for log in loglines:
        prompt = prompt + log + '\n'

    return prompt

def prompt_generator_by_line_korean(loglines):
    prompt_statement = """You are a logging practitioner.
    You are provided with 100 lines of logs and you need to translate these log into Korean
    The output should only be 100 lines of translated logs written in Korean. No explanation is needed."""

    prompt_requirements = """You should follow the following requirements:
    (1) The letter case of the translated template should be the same with original log template.
    For example, there is an English log template: LDAP: SSL support unavailable 
    its corresponding translated Korean log template should be: LDAP: SSL 지원이 불가능합니다.
    LDAP and SSL should keep the same letter case with the original log template. 
    (2) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. 
    (3) Simple words like client should be translated. 
    (4) The translated logs should be separated with newline character like the input format"""

    prompt_log_lines_header = '#### Log lines:'

    prompt = prompt_statement + '\n' + '\n' + prompt_requirements + '\n' + '\n' + prompt_log_lines_header + '\n'
    for log in loglines:
        prompt = prompt + log + '\n'

    return prompt

def prompt_generator_by_line_japanese(loglines):
    prompt_statement = """You are a logging practitioner.
    You are provided with 100 lines of logs and you need to translate these log into Japanese
    The output should only be 100 lines of translated logs written in Japanese. No explanation is needed."""

    prompt_requirements = """You should follow the following requirements:
    (1) The letter case of the translated template should be the same with original log template.
    For example, there is an English log template: LDAP: SSL support unavailable 
    its corresponding translated Japanese log template should be: LDAP: SSLサポートは利用できません
    LDAP and SSL should keep the same letter case with the original log template. 
    (2) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. 
    (3) Simple words like client should be translated. 
    (4) The translated logs should be separated with newline character like the input format"""

    prompt_log_lines_header = '#### Log lines:'

    prompt = prompt_statement + '\n' + '\n' + prompt_requirements + '\n' + '\n' + prompt_log_lines_header + '\n'
    for log in loglines:
        prompt = prompt + log + '\n'

    return prompt

def prompt_generator_by_line_french(loglines):
    prompt_statement = """You are a logging practitioner.
    You are provided with 100 lines of logs and you need to translate these log into French
    The output should only be 100 lines of translated logs written in French. No explanation is needed."""

    prompt_requirements = """You should follow the following requirements:
    (1) The letter case of the translated template should be the same with original log template.
    For example, there is an English log template: LDAP: SSL support unavailable 
    its corresponding translated French log template should be: LDAP: support pour SSL non disponible
    LDAP and SSL should keep the same letter case with the original log template. 
    (2) Simple words like client should be translated. 
    (3) The translated logs should be separated with newline character like the input format
    (4) Some words are software engineering domain specific, you do not need to translate them into French"""

    prompt_log_lines_header = '#### Log lines:'

    prompt = prompt_statement + '\n' + '\n' + prompt_requirements + '\n' + '\n' + prompt_log_lines_header + '\n'
    for log in loglines:
        prompt = prompt + log + '\n'

    return prompt

def prompt_generator_by_single_line(log):
    prompt_statement = """You are a logging practitioner.
        You are provided with one log and you need to translate this log into Chinese
        The output should only be the translated log written in Chinese. No explanation is needed."""

    prompt_requirements = """You should follow the following requirements:
        (1) The letter case of the translated log should be the same with original log.
        For example, there is an English log: LDAP: SSL support unavailable 
        its corresponding translated Chinese log should be: LDAP：SSL支持不可用 
        LDAP and SSL should keep the same letter case with the original log. 
        (2) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. 
        (3) Simple words like client should be translated. """

    prompt_log_line_header = '#### Log line:'

    prompt = prompt_statement + '\n' + '\n' + prompt_requirements + '\n' + '\n' + prompt_log_line_header + '\n' + log

    return prompt

def prompt_generator_by_single_line_French(log):
    prompt_statement = """You are a logging practitioner.
        You are provided with one log and you need to translate this log into French
        The output should only be the translated log written in French. No explanation is needed."""

    prompt_requirements = """You should follow the following requirements:
        (1) The letter case of the translated log should be the same with original log.
        For example, there is an English log: LDAP: SSL support unavailable 
        its corresponding translated French log should be: LDAP: support pour SSL non disponible
        LDAP and SSL should keep the same letter case with the original log. 
        (2) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. 
        (3) Simple words like client should be translated. 
        (4) Some words are software engineering domain specific, you do not need to translate them into French"""

    prompt_log_line_header = '#### Log line:'

    prompt = prompt_statement + '\n' + '\n' + prompt_requirements + '\n' + '\n' + prompt_log_line_header + '\n' + log

    return prompt

def prompt_generator_by_single_line_Japanese(log):
    prompt_statement = """You are a logging practitioner.
        You are provided with one log and you need to translate this log into Japanese
        The output should only be the translated log written in Japanese. No explanation is needed."""

    prompt_requirements = """You should follow the following requirements:
        (1) The letter case of the translated log should be the same with original log.
        For example, there is an English log: LDAP: SSL support unavailable 
        its corresponding translated Japanese log should be: LDAP: SSLサポートは利用できません
        LDAP and SSL should keep the same letter case with the original log. 
        (2) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. 
        (3) Simple words like client should be translated. """

    prompt_log_line_header = '#### Log line:'

    prompt = prompt_statement + '\n' + '\n' + prompt_requirements + '\n' + '\n' + prompt_log_line_header + '\n' + log

    return prompt

def prompt_generator_by_single_line_Korean(log):
    prompt_statement = """You are a logging practitioner.
        You are provided with one log and you need to translate this log into Korean
        The output should only be the translated log written in Korean. No explanation is needed."""

    prompt_requirements = """You should follow the following requirements:
        (1) The letter case of the translated log should be the same with original log.
        For example, there is an English log: LDAP: SSL support unavailable 
        its corresponding translated Korean log should be: LDAP: SSL 지원이 불가능합니다
        LDAP and SSL should keep the same letter case with the original log. 
        (2) There should be no whitespace between words or punctuations. However, there should be whitespace between two English words, two dynamic variables or one English word and a dynamic variable. 
        (3) Simple words like client should be translated. """

    prompt_log_line_header = '#### Log line:'

    prompt = prompt_statement + '\n' + '\n' + prompt_requirements + '\n' + '\n' + prompt_log_line_header + '\n' + log

    return prompt

def prompt_generator_v2(template):
    prompt_statement = "You are a logging practitioner. \
        You are provided with a log template written with English and you need to translate the log template into Chinese. \
        The output should be a translated log template written with Chinese."

    prompt_requirements = "You should follow the following requirements: \n\
        (1) The letter case of the translated template should be the same with original log template. \
        For example, there is an English log template: LDAP: SSL support unavailable \
        its corresponding translated Chinese log template should be: LDAP：SSL支持不可用 \
        LDAP and SSL should keep the same letter case with the original log template. \n\
        (2) The translated log template should pay attention to the order of dynamic information. \
        For example, there is an English log template: Node card VPD check: <d_0> node in processor card slot <d_1> do not match. VPD ecid <d_2>, found <d_3> \
        its corresponding translated Chinese log template should be: 节点卡VPD检查：处理器卡槽<d_1>中的<d_0>节点不匹配。VPD ecid为<d_2>,发现<d_3> \
        the order of the first dynamic information <d_0> and the second dynamic information <d_1> in original log template is changed in translated Chinese log template. \
        The reason is we need to keep the semantic information in translated Chinese log template is the same with the original English log template. \n\
        (3) Simple words like client should be translated. \n\
        (4) The output should only be the translated template"

    prompt_ori_template_header = "### log template:"

    new_template = template_format_changer(template)

    prompt = prompt_statement + '\n' + prompt_requirements + '\n' + prompt_ori_template_header + '\n' + new_template

    return prompt

def prompt_generator_French_v2(template):
    prompt_statement = "You are a logging practitioner. \
        You are provided with a log template written with English and you need to translate the log template into French. \
        The output should be a translated log template written with French."

    prompt_requirements = "You should follow the following requirements: \n\
        (1) The letter case of the translated template should be the same with original log template. \
        For example, there is an English log template: LDAP: SSL support unavailable \
        its corresponding translated French log template should be: LDAP: support pour SSL non disponible \
        LDAP and SSL should keep the same letter case with the original log template. \n\
        (2) Simple words like client should be translated. \n\
        (3) The output should only be the translated template \n\
        (4) Some words are software engineering domain specific, you do not need to translate them into French"

    prompt_ori_template_header = "### log template:"

    new_template = template_format_changer(template)

    prompt = prompt_statement + '\n' + prompt_requirements + '\n' + prompt_ori_template_header + '\n' + new_template

    return prompt

def prompt_generator_Japanese_v2(template):
    prompt_statement = "You are a logging practitioner. \
        You are provided with a log template written with English and you need to translate the log template into Japanese. \
        The output should be a translated log template written with Japanese."

    prompt_requirements = "You should follow the following requirements: \n\
        (1) The letter case of the translated template should be the same with original log template. \
        For example, there is an English log template: LDAP: SSL support unavailable \
        its corresponding translated Japanese log template should be: LDAP: SSLサポートは利用できません \
        LDAP and SSL should keep the same letter case with the original log template. \n\
        (2) The translated log template should pay attention to the order of dynamic information. \
        For example, there is an English log template: Node card VPD check: <d_0> node in processor card slot <d_1> do not match. VPD ecid <d_2>, found <d_3> \
        its corresponding translated Japanese log template should be: ノードカードVPDチェック：プロセッサーカードスロット<d_1>の<d_0>ノードが一致しません。VPD ecid <d_2>、検出 <d_3> \
        the order of the first dynamic information <d_0> and the second dynamic information <d_1> in original log template is changed in translated Japanese log template. \
        The reason is we need to keep the semantic information in translated Japanese log template is the same with the original English log template. \n\
        (3) Simple words like client should be translated. \n\
        (4) The output should only be the translated template"

    prompt_ori_template_header = "### log template:"

    new_template = template_format_changer(template)

    prompt = prompt_statement + '\n' + prompt_requirements + '\n' + prompt_ori_template_header + '\n' + new_template

    return prompt

def prompt_generator_Korean_v2(template):
    prompt_statement = "You are a logging practitioner. \
        You are provided with a log template written with English and you need to translate the log template into Korean. \
        The output should be a translated log template written with Korean."

    prompt_requirements = "You should follow the following requirements: \n\
        (1) The letter case of the translated template should be the same with original log template. \
        For example, there is an English log template: LDAP: SSL support unavailable \
        its corresponding translated Korean log template should be: LDAP: SSL 지원이 불가능합니다 \
        LDAP and SSL should keep the same letter case with the original log template. \n\
        (2) The translated log template should pay attention to the order of dynamic information. \
        For example, there is an English log template: Node card VPD check: <d_0> node in processor card slot <d_1> do not match. VPD ecid <d_2>, found <d_3> \
        its corresponding translated Korean log template should be: 노드 카드 VPD 검사: 프로세서 슬롯 <d_1>의 <d_0> 노드가 일치하지 않습니다. VPD ECID는 <d_2>이지만, <d_3>이 발견되었습니다 \
        the order of the first dynamic information <d_0> and the second dynamic information <d_1> in original log template is changed in translated Korean log template. \
        The reason is we need to keep the semantic information in translated Korean log template is the same with the original English log template. \n\
        (3) Simple words like client should be translated. \n\
        (4) The output should only be the translated template"

    prompt_ori_template_header = "### log template:"

    new_template = template_format_changer(template)

    prompt = prompt_statement + '\n' + prompt_requirements + '\n' + prompt_ori_template_header + '\n' + new_template

    return prompt
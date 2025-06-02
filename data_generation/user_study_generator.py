import pandas as pd
from openai import OpenAI
from prompt_generator import prompt_generator_by_single_line, prompt_generator_by_single_line_French, prompt_generator_by_single_line_Japanese, prompt_generator_by_single_line_Korean

datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']

gpt_key = ''

client = OpenAI(api_key=gpt_key)
for dataset in datasets:
    translated_event_file = '../../output/Template/V2/French/' + dataset + '/' + dataset + '_translated_event.csv'
    user_study_file = '../../output/Userstudy/V2/French/pool/' + dataset + '_userstudy.csv'
    user_study_df = pd.DataFrame(columns=['Origin', 'Translated', 'TranslatedByLine'])

    translated_event_df = pd.read_csv(open(translated_event_file))
    templates = list(dict.fromkeys(translated_event_df['OriTemplate'].tolist()))
    for template in templates:
        template_df = translated_event_df[translated_event_df['OriTemplate'] == template]
        row = template_df.sample(n=1)
        original_log = row['Origin'].iloc[0]
        translated_log = row['Translated'].iloc[0]
        prompt = prompt_generator_by_single_line_French(original_log)
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{"role": "assistant", "content": prompt}],
        )
        translated_log_by_line = response.choices[0].message.content
        user_study_row = [original_log, translated_log, translated_log_by_line]
        user_study_df.loc[len(user_study_df)] = user_study_row

    user_study_df.to_csv(user_study_file)
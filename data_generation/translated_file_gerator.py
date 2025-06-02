from prompt_generator import prompt_generator_v2, prompt_generator_French_v2, prompt_generator_Japanese_v2, prompt_generator_Korean_v2
import pandas as pd
from llm_config import deep_seek_key, gpt_key
from openai import OpenAI
import time
import tiktoken

datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']
client = OpenAI(api_key=gpt_key)
encoding = tiktoken.encoding_for_model('gpt-4o-mini')
# client = OpenAI(api_key=deep_seek_key, base_url="https://api.deepseek.com")

for dataset in datasets:
    start_time = time.time()
    dataset_translated_tokens = 0
    template_file = '../../data/original/' + dataset + '/' + dataset + '_content_2k_template.csv'
    translated_file = '../../output/Template/V2/French/' + dataset + '/' + dataset + '_translated.csv'
    template_col = 'Template'
    ori_col = 'Template'
    translated_col = 'Translated'

    template_df = pd.read_csv(template_file)
    templates = template_df[template_col].to_list()

    template_info = []

    for template in templates:
        prompt = prompt_generator_French_v2(template)
        dataset_translated_tokens += len(encoding.encode(prompt))
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{"role": "assistant", "content": prompt}],
        )
        dataset_translated_tokens += sum(len(encoding.encode((str(item)))) for item in response)
        translated_template = response.choices[0].message.content
        template_info.append([template, translated_template])

    translated_df = pd.DataFrame(template_info, columns=[ori_col, translated_col])
    translated_df.to_csv(translated_file)
    end_time = time.time()
    time_cost = end_time - start_time
    print(dataset + ': ' + str(time_cost))
    print(dataset + ' tokens: ' + str(dataset_translated_tokens))

# template_file = '../../data/original/HDFS/HDFS_content_2k_template.csv'
# translated_file = '../../output/HDFS/HDFS_translated.csv'
# template_col = 'Template'
# ori_col = 'Template'
# translated_col = 'Translated'

# template_df = pd.read_csv(template_file)
# templates = template_df[template_col].to_list()
#
# client = OpenAI(api_key=deep_seek_key, base_url="https://api.deepseek.com")
# template_info = []
#
# for template in templates:
#     prompt = prompt_generator((template))
#     response = client.chat.completions.create(
#         model='deepseek-chat',
#         messages=[{"role": "assistant", "content": prompt}],
#     )
#     translated_template = response.choices[0].message.content
#     template_info.append([template, translated_template])
#
# translated_df = pd.DataFrame(template_info, columns=[ori_col, translated_col])
# translated_df.to_csv(translated_file)
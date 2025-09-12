import os
import sys
import logging
import pandas as pd
from spellpy import spell

logging.basicConfig(level=logging.WARNING,
                    format='[%(asctime)s][%(levelname)s]: %(message)s')
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))


def deeplog_df_transfer(df, event_id_map):
    df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_Linux_Mac(df, event_id_map):
    df["datetime_str"] = df["Month"].astype(str) + " " + df["Date"].astype(str) + " " + df["Time"]
    df["datetime"] = pd.to_datetime(df["datetime_str"], format="%b %d %H:%M:%S")
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_OpenSSH(df, event_id_map):
    df["datetime_str"] = df["Date"].astype(str) + " " + df["Day"].astype(str) + " " + df["Time"]
    df["datetime"] = pd.to_datetime(df["datetime_str"], format="%b %d %H:%M:%S")
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_HDFS(df, event_id_map):
    df['datetime'] = pd.to_datetime(df['Date'].astype(str) + df['Time'].astype(str), format='%y%m%d%H%M%S', errors='coerce')
    df['datetime'] = pd.to_datetime(df['datetime'], unit='s')
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_Apache(df, event_id_map):
    df['datetime'] = pd.to_datetime(df['Time'])
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_BGL(df, event_id_map):
    df["datetime"] = pd.to_datetime(df["Timestamp"], unit="s")
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_HPC(df, event_id_map):
    df["datetime"] = pd.to_datetime(df["Time"], unit="s")
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_HealthApp(df, event_id_map):
    df["Time"] = df["Time"].str.replace(r":(\d{3})$", lambda m: ":" + m.group(1) + "000", regex=True)
    df["datetime"] = pd.to_datetime(df["Time"], format="%Y%m%d-%H:%M:%S:%f")
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_Proxifier(df, event_id_map):
    df["datetime"] = pd.to_datetime(df["Time"], format="%m.%d %H:%M:%S")
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_Spark(df, event_id_map):
    df["datetime"] = pd.to_datetime(
        df["Date"] + " " + df["Time"],
        format="%y/%m/%d %H:%M:%S",
        errors="coerce"
    )
    df = df.dropna(subset=["datetime"])
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def deeplog_df_transfer_Zookeeper(df, event_id_map):
    df["datetime"] = pd.to_datetime(
        df["Date"] + " " + df["Time"],
        format="%Y-%m-%d %H:%M:%S,%f",  # 注意 %f 解析毫秒
        errors="coerce"  # 无法解析的变为 NaT
    )
    df = df.dropna(subset=["datetime"])
    df = df[['datetime', 'EventId']]
    df['EventId'] = df['EventId'].apply(lambda e: event_id_map[e] if event_id_map.get(e) else -1)
    deeplog_df = df.set_index('datetime').resample('1min').apply(_custom_resampler).reset_index()
    return deeplog_df

def _custom_resampler(array_like):
    return list(array_like)


def deeplog_file_generator(filename, df):
    with open(filename, 'w') as f:
        for event_id_list in df['EventId']:
            for event_id in event_id_list:
                f.write(str(event_id) + ' ')
            f.write('\n')


if __name__ == '__main__':
    datasets = ['Chinese', 'English', 'French', 'Japanese', 'Korean']
    len_map = []

    for dataset in datasets:
        train_input = './data/Zookeeper/' + dataset + '/Zookeeper_' + dataset + '_train.log_structured.csv'
        test_input = './data/Zookeeper/' + dataset + '/Zookeeper_' + dataset + '_test.log_structured.csv'
        train_output = './data/Zookeeper/' + dataset + '/train'
        test_output = './data/Zookeeper/' + dataset + '/test'

        train_df = pd.read_csv(train_input)
        test_df = pd.read_csv(test_input)

        event_id_map = dict()
        for i, event_id in enumerate(train_df['EventId'].unique(), 1):
            event_id_map[event_id] = i

        logger.info(f'length of event_id_map: {len(event_id_map)}')
        len_map.append(len(event_id_map))

        deeplog_train = deeplog_df_transfer_Zookeeper(train_df, event_id_map)
        deeplog_file_generator(train_output, deeplog_train)

        deeplog_test = deeplog_df_transfer_Zookeeper(test_df, event_id_map)
        deeplog_file_generator(test_output, deeplog_test)

    print(len_map)

    # train_df = pd.read_csv(f'./data/OpenStack/French/OpenStack_French_train.log_structured.csv')
    # test_df = pd.read_csv(f'./data/OpenStack/French/OpenStack_French_test.log_structured.csv')
    #
    # event_id_map = dict()
    # for i, event_id in enumerate(train_df['EventId'].unique(), 1):
    #     event_id_map[event_id] = i
    #
    # logger.info(f'length of event_id_map: {len(event_id_map)}')
    #
    # deeplog_train = deeplog_df_transfer(train_df, event_id_map)
    # deeplog_file_generator('./data/OpenStack/French/train', deeplog_train)
    #
    # deeplog_test = deeplog_df_transfer(test_df, event_id_map)
    # deeplog_file_generator('./data/OpenStack/French/test', deeplog_test)
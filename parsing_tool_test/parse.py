# from logparser.Drain import LogParser
# from logparser.config.Drain_config import benchmark_settings

# from logparser.NuLog import LogParser
# from logparser.config.NuLog_config import benchmark_settings

# from logparser.LenMa.LenMa import LogParser
# from logparser.config.LenMa_config import benchmark_settings

# from logparser.IPLoM import LogParser
# from logparser.config.IPLoM_config import benchmark_settings

from logparser.Spell import LogParser
from logparser.config.Spell_config import benchmark_settings

datasets = ['Apache', 'BGL', 'Hadoop', 'HDFS', 'HealthApp', 'HPC', 'Linux', 'Mac', 'OpenSSH', 'OpenStack', 'Proxifier', 'Spark', 'Zookeeper']
# datasets = ['Apache', 'BGL', 'HDFS', 'HealthApp', 'HPC', 'Mac', 'OpenStack', 'Spark']

for dataset in datasets:
    print('Begin parsing ' + dataset)
    log_format = '<Content>'
    output_dir = 'parsing_result/Spell/French/' + dataset + '/'
    input_dir = 'tokenized_log/French/'
    # log_file = dataset + '.log'
    log_file = dataset + '_translated.log'
    # log_file = dataset + '_tokenized.log'

    """NuLog"""
    # filters = benchmark_settings[dataset]["filters"]
    # k = benchmark_settings[dataset]["k"]
    # nr_epochs = benchmark_settings[dataset]["nr_epochs"]
    # num_samples = benchmark_settings[dataset]["num_samples"]
    # parser = LogParser(log_format=log_format, indir=input_dir, outdir=output_dir, filters=filters, k=k)
    # parser.parse(log_file, nr_epochs=nr_epochs, num_samples=num_samples)

    """Drain"""
    # depth = benchmark_settings[dataset]['depth']
    # st = benchmark_settings[dataset]['st']
    # regex = benchmark_settings[dataset]['regex']
    # parser = LogParser(log_format, indir=input_dir, outdir=output_dir, depth=depth, st=st, rex=regex, keep_para=False)
    # parser.parse(log_file)

    """LenMa"""
    # threshold = benchmark_settings[dataset]['threshold']
    # regex = benchmark_settings[dataset]['regex']
    # parser = LogParser(input_dir, output_dir, log_format, threshold=threshold, rex=regex)
    # parser.parse(log_file)

    """IPLoM"""
    # CT = benchmark_settings[dataset]['CT']
    # lowerBound = benchmark_settings[dataset]['lowerBound']
    # regex = benchmark_settings[dataset]['regex']
    # parser = LogParser(log_format=log_format, indir=input_dir, outdir=output_dir,
    #                    CT=CT, lowerBound=lowerBound, rex=regex, keep_para=False)
    # parser.parse(log_file)

    """Spell"""
    tau = benchmark_settings[dataset]['tau']
    regex = benchmark_settings[dataset]['regex']

    parser = LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex, keep_para=False)
    parser.parse(log_file)

    print('Finished parsing')
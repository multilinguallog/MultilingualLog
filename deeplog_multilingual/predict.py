import sys
sys.path.append('../')
import json
import logging
import argparse
from deeplog.deeplog import model_fn, input_fn, predict_fn

import pickle

logging.basicConfig(level=logging.WARNING,
                    format='[%(asctime)s][%(levelname)s]: %(message)s')
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--threshold', type=int, default=23, metavar='N',
                        help='to determine the time series data is an anomaly or not.')
    args = parser.parse_args()

    ##############
    # Load Model #
    ##############
    model_dir = './model/Spark/Mix/'
    value_output = './result/Spark/Mix/value.pkl'
    anomaly_output = './result/Spark/Mix/decision.pkl'
    model_info = model_fn(model_dir)

    ###########
    # predict #
    ###########
    test_predict_list = []
    with open('test', 'r') as f:
        for line in f.readlines():
            line = list(map(lambda n: n - 1, map(int, line.strip().split())))
            request = json.dumps({'line': line})
            input_data = input_fn(request, 'application/json')
            response = predict_fn(input_data, model_info)
            test_predict_list.append(response)

    ##############
    # Evaluation #
    ##############
    thres = args.threshold
    predict_has_anomaly_value = [t['anomaly_cnt'] for t in test_predict_list]
    print(predict_has_anomaly_value)
    print(len(predict_has_anomaly_value))
    with open(value_output, "wb") as f:
        pickle.dump(predict_has_anomaly_value, f)
    predict_has_anomaly = [1 if t['anomaly_cnt'] > thres else 0 for t in test_predict_list]
    print(predict_has_anomaly)
    print(len(predict_has_anomaly))
    with open(anomaly_output, "wb") as f:
        pickle.dump(predict_has_anomaly, f)
    # print(len(predict_has_anomaly))
    # abnormal_cnt_anomaly = [t['anomaly_cnt'] for t in test_predict_list]
    # abnormal_predict = []
    # for test_predict in test_predict_list:
    #     abnormal_predict += test_predict_list['predict_list']
    # print(abnormal_predict)
import pickle

import numpy as np
from scipy.spatial.distance import jensenshannon
from scipy.stats import wasserstein_distance
from numpy.linalg import norm


def similarity(list1, list2, method="pearson", bins=10):
    list1, list2 = np.array(list1), np.array(list2)

    if method == "pearson":
        score = np.corrcoef(list1, list2)[0, 1]
        # Pearson 可能为负数，转换到 [0,1]
        score = (score + 1) / 2

    elif method == "cosine":
        score = np.dot(list1, list2) / (norm(list1) * norm(list2))

    elif method == "js":
        hist1, _ = np.histogram(list1, bins=bins, density=True)
        hist2, _ = np.histogram(list2, bins=bins, density=True)
        hist1 = np.where(hist1 == 0, 1e-10, hist1)
        hist2 = np.where(hist2 == 0, 1e-10, hist2)
        score = 1 - jensenshannon(hist1, hist2)

    elif method == "emd":
        dist = wasserstein_distance(list1, list2)
        score = 1 / (1 + dist)

    else:
        raise ValueError("Unknown method: choose from 'pearson', 'cosine', 'js', 'emd'")

    # 转换为百分比
    return round(score * 100, 2)


list_0 = pickle.load(open('./result/BGL/English/value.pkl', 'rb'))
list_1 = pickle.load(open('./result/BGL/Mix/value.pkl', 'rb')) + [0]*3538

print(len(list_0))
print(len(list_1))
# print(list_1)

print("Pearson:", similarity(list_0, list_1, method="pearson"), "%")
print("Cosine:", similarity(list_0, list_1, method="cosine"), "%")
print("JS:", similarity(list_0, list_1, method="js"), "%")
print("EMD:", similarity(list_0, list_1, method="emd"), "%")
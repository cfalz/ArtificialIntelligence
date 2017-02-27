import sys
import numpy as np
import matplotlib as plt
from scipy.spatial import distance
from sklearn import preprocessing
from FeatureSelection import *

PRINTDEBUG = 1

def process_data():
    data = []
    normalized_data = []
    filename = sys.argv[-1]
    f = open(filename, 'r')

    for line in f:
        data.append(line.split())

    for instance in data:
        classification = instance.pop(0)
        features = np.array(instance)
        """ Reshape because this is only a single sample """
        features = features.reshape(1,-1)
        features_normalized = preprocessing.normalize(features, norm='l1')
        features_normalized = features_normalized.tolist()
        features_normalized.insert(0,classification)
        normalized_data.append(features_normalized)
    return normalized_data


def main():
    data = process_data()
    feature_set = [1]
    fs = ForwardSelection(data)
    #fs.add_feature(feature_set)
    new = np.array([0.02])
    new = new.reshape(1,-1)
    new = preprocessing.normalize(new, norm='l1')
    print "[!] Classifing Unknown Instance: ", new
    print fs.nearest_neighbor(new, feature_set)




if __name__ == "__main__":
    main()

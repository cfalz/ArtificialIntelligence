import sys
import numpy as np
import matplotlib as plt
from scipy.spatial import distance
import warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing
from FeatureSelection import *

PRINTDEBUG = 1

def greeting():
    print " [+] Welcome To Cody Falzone's Feature Selection."
    print " [!] Type in the name of the file to test: \n"
    filename = raw_input()
    print " \n [!] Type the number of the algorithm you want to run. "
    print "    1) Forward Selection"  
    print "    2) Backward Elimination"  
    print "    3) Cody's Special Algorithm\n"  
    algorithm = raw_input()
    return filename, algorithm

def process_data(filename):
    data = []
    normalized_data = []
    instances = 0
    features = 0

    f = open(filename, 'r')

    print " [!] Please Wait While I Normalize The Data... "

    for line in f:
        data.append(line.split())
    for l in data:
        if instances == 0:
            features = len(data[0]) - 1
        floats = []
        for fp in l:
            floats.append(float(fp))
        normalized_data.append(floats)
        instances += 1

    print " [+] Done Normalizing Data. \n"
    print " [+] The Data Set Has " , features , " features (not including the class attribute), with ", instances , " instances."  

    return normalized_data

"""
    for instance in data:
        classification = instance.pop(0)
        features = np.array(instance)
        Reshape because this is only a single sample
        features = features.reshape(1,-1)
        features_normalized = preprocessing.normalize(features, norm='l1')
        features_normalized = features_normalized.tolist()
        features_normalized.insert(0,classification)
        normalized_data.append(features_normalized)
    return normalized_data
"""


def main():
    filename, algorithm = greeting()
    print "\n Using Filename: ", filename , ".\n"
    data = process_data(filename)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
    print " [!] Beginning Search. \n"
    fs = ForwardSelection(data)
    (best_set, accuracy) = fs.select()
    print "\n [+] The Best Set Is ", best_set, " With An Accuracy Of " , accuracy*100 , "% .\n"


if __name__ == "__main__":
    main()




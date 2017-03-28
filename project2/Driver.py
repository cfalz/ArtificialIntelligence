import sys
from math import *
import numpy as np
from time import time
import matplotlib as plt
from scipy.spatial import distance
from sklearn import preprocessing
from FeatureSearch import *
from Classifier import *
from Validator import *

PRINTDEBUG = 1
output = open('Large80_forward_output.txt', 'w')

def greeting():
    print >> output, " [+] Welcome To Cody Falzone's Feature Selection." 
    print >> output, " [!] Type in the name of the file to test: \n"
    filename = raw_input()
    print >> output, " \n [!] Type the number of the algorithm you want to run. "
    print >> output, "    1) Forward Selection"  
    print >> output, "    2) Backward Elimination"  
    print >> output, "    3) Cody's Special Algorithm\n"  
    algorithm = raw_input()
    return filename, algorithm


def process_data(filename):
    data = []
    new_data = []
    normalized_data = []
    instances = 0
    number_features = 0

    f = open(filename, 'r')

    print >> output, " [!] Please Wait While I Normalize The Data... "

    for line in f:
        data.append(line.split())
    for l in data:
        if instances == 0:
            number_features = len(data[0]) - 1
        floats = []
        for fp in l:
            floats.append(float(format(float(fp), '8f')))
        new_data.append(floats)
        instances += 1

    max_value = -1.0;
    min_value = float("inf")
    for instance in new_data:
        for value in instance:
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value
    denomanator = max_value - min_value

    for instance in new_data:
        classification = instance.pop(0)
        normalized = []
        for value in instance:
            new_value = (value - min_value)/denomanator 
            normalized.append(new_value)
        normalized.insert(0,classification)
        normalized_data.append(normalized)

    print >> output, " [+] Done Normalizing Data. \n"
    print >> output, " [+] The Data Set Has " , number_features , " features (not including the class attribute), with ", instances , " instances."  
    
    return normalized_data


def main():
    filename, algorithm = greeting()
    print >> output, "\n Using Filename: ", filename , ".\n"
    data = process_data(filename)
    classifier = NearestNeighbor(data)
    validator = LeaveOneOut(classifier)
    algorithm = int(algorithm)
    if algorithm not in range(1,3):
        print >> output, " [-] " , algorithm , "Is An Invalid Algorithm Option. "
        return -1
    if algorithm == 1:
        fs = ForwardSelection(validator)
        print >> output, " [!] Beginning Search Using Forward Selection Algorithm. \n"
    if algorithm == 2:
        fs = BackwardSelection(validator)
        print >> output, " [!] Beginning Search Using Backward Elimination Algorithm. \n"

    start = time()
    (best_set, accuracy) = fs.select()
    end = time() - start
    print >> output, "Elasped Time: ", end
    print >> output, "\n [+] The Best Set Is ", best_set, " With An Accuracy Of " , accuracy*100 , "% .\n"


if __name__ == "__main__":
    main()



#TEST HARNESS 2
import sys
from math import *
import numpy as np
import matplotlib as plt
from scipy.spatial import distance
from sklearn import preprocessing
from FeatureSearch import *
from Classifier import *
from Validator import *

PRINTDEBUG = 1

def process_data():
    data = []
    normalized_data = []
    filename = sys.argv[-1]
    data_file = open(filename, 'r')

    print " [!] Please Wait While I Normalize The Data... "
    for line in data_file:
        data.append(line.split())
    for l in data:
        print "The Line in the Data is: "
        print l
        floats = []
        for fp in l:
            floats.append(float(fp))
        normalized_data.append(floats)
    return normalized_data

def main():

    data = process_data()
    print "[+] Done. "
    print "[!] Beginning Search. \n"
    classifier = NearestNeighbor(data)
    validator = LeaveOneOut(classifier)
    fs = ForwardSelection(validator)
    (best_set, accuracy) = fs.select()
    print "\n  [+] The Best Set Is ", best_set, " With An Accuracy Of " , accuracy*100 , "% .\n"

if __name__ == "__main__":
    main()

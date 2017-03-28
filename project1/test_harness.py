import sys
from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from sklearn import preprocessing
from FeatureSelection import *

PRINTDEBUG = 1


def process_data(filename):
    data = []
    new_data = []
    normalized_data = []
    instances = 0
    number_features = 0

    f = open(filename, 'r')

    print " [!] Please Wait While I Normalize The Data... "

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

    print  " [+] Done Normalizing Data. \n"
    print  " [+] The Data Set Has " , number_features , " features (not including the class attribute), with ", instances , " instances."  
    
    return normalized_data

def plot(t,x_title, y_title, x1 , y1, x2, y2):
    plt.title(t)
    c1, = plt.plot(x1, y1, 'bs', label = 'Class 1')
    c2, = plt.plot(x2, y2, 'g^', label = 'Class 2')
    plt.legend(handles = [c1,c2], loc = 2)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()


def main():

    data = process_data('TrainingData/cs_170_large80.txt')
    print "[+] Done. "

    #Plotting Small44_Forward, Best Set is [5,8] accuracy 90%.
    #x = [ l[5] for l in data if l[0] == 2 ]
    #y = [ l[8] for l in data if l[0] == 1 ]
    x1 = []
    y1 = []
    x2 = []
    y2 = []

    for l in data:
        if l[0] == 1:
            x1.append(l[1])
            y1.append(l[27])
        if l[0] == 2:
            x2.append(l[1])
            y2.append(l[27])

    plot('Large80 Forward - Feature Set [1,27]', "Feature 1", "Feature 27", x1 , y1, x2, y2)
    #print "[!] Beginning Search. \n"
    #fs = ForwardSelection(data)
    #(best_set, accuracy) = fs.select()
    #print "\n  [+] The Best Set Is ", best_set, " With An Accuracy Of " , accuracy*100 , "% .\n"

if __name__ == "__main__":
    main()




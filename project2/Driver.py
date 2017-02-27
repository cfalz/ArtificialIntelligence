import sys
import numpy as np
import matplotlib as plt
from scipy.spatial import distance
from sklearn import preprocessing


filename = sys.argv[-1]

f = open(filename, 'r')

data = []
for line in f:
    data.append(line.split())


for item in data:
    print item


a = [1,2,3,4]
b = [1,3,5,7]

dist = distance.euclidean(a,b)

print dist

for instance in data:
    classification = instance.pop(0)
    print "Classification of Instance" , classification , ".\n"
    features = np.array(instance)
    """ Reshape because this is only a single sample """
    features = features.reshape(1,-1)
    features_normalized = preprocessing.normalize(features, norm='l1')
    print "Features Normalized"
    print features_normalized
    print "\n"




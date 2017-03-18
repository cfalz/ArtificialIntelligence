
"""
    Author: Cody Falzone
    SID: 860929046
    CS170 Winter 17
    Project 2 - Feature Selection With Nearest Neighbor

"""

############################################################################
#                                                                          #
#    Classes for a Feature Selection.                                      # 
#    Input: Training Data Set.                                             #
#                                                                          #
############################################################################

import numpy as np
import copy
import warnings
from scipy.spatial import distance
from sklearn import preprocessing
import bisect

PRINTDEBUG = 0

""" The Default Contstruction for the Feature Subset Search Algorithms. """
class FeatureSelection(object):

    def __init__( self, training_data ):
        self.data = training_data
        if(PRINTDEBUG):
            print " [+] Feature Selection initialized with data: "
            for instance in self.data:
                print instance
        #self.features = [instance.pop(1) for instance in copy.deepcopy(training_data)]
        self.number_of_features = len(training_data[0]) - 1
        self.classes = [instance.pop(0) for instance in copy.deepcopy(training_data)]

        if(PRINTDEBUG):
            print " [+] Feature Selection initialized with classes: "
            print self.classes
            print "\n"

    """ The Nearest Neighbor Classifier. """
    def nearest_neighbor(self, new_instance, known_instances, feature_set):
        classification = None
        min_distance = float("inf")
        if(PRINTDEBUG):
            print " [!] Feature Set: " , feature_set
            print "\n"
        for classified in known_instances:
            c = classified[0]
            #instance = [ copy.deepcopy(classified).pop(feature_number) for feature_number in feature_set ]
            instance = [ classified[feature_number] for feature_number in feature_set ]
            if(PRINTDEBUG):
                print " [!] Instance Features: " , instance  
            dist = distance.euclidean(instance, new_instance)

            #if(PRINTDEBUG):
            #    print " [!] Distance from new instance: " , dist  
             #   print "\n"
            if dist < min_distance:
                min_distance = dist
                classification = c
        return classification
                
    """ Evalution Function used for validation. Uses training data and the classifier. Gives the accuracy score. """
    def leave_one_out(self, set_of_features):
        correct = 0
        for i in range(0,len(self.classes)):
            unknown = self.data.pop(i)  
            known = self.data
            unknown_mod = [ unknown[feature_number] for feature_number in set_of_features ] 
            classification = self.nearest_neighbor(unknown_mod, known, set_of_features)
            if classification == unknown[0]:
                correct+=1
            self.data.insert(i,unknown)
        return float(correct)/float(len(self.classes))
        

    """ The Search Algorithm that will search for the best feature set. """
    def select(self):
        raise NotImplementedError


""" Feature Selection Search Using Forward Selection. """
class ForwardSelection(FeatureSelection):

    def __init__( self, training_data ):
        super(ForwardSelection, self).__init__(training_data)

    """ Returns a list of new feature sets after adding each possible new feature to the existing set """ 
    def add_feature(self, feature_set):
        new_feature_set = []
        feature_set_list = []
        for feature in range(1,self.number_of_features + 1):
            for s in feature_set:
                if feature not in s:
                    new_feature_set = copy.deepcopy(s)
                    bisect.insort(new_feature_set, feature)
                    if new_feature_set not in feature_set_list:
                        feature_set_list.append(new_feature_set)
        return feature_set_list

    """ The Search Algorithm that will search for the best feature set. """
    def select(self):
        max_score = -1;
        feature_sets = [[]]
        while ( True ):
            feature_sets = self.add_feature(feature_sets)
            if len(feature_sets) == 0:
                return best_set, max_score
            for feature_set in feature_sets:
                score = self.leave_one_out(feature_set)
                print "[!] Using Feature(s) ", feature_set, "Accuracy is ", score*100, "%."
                if score > max_score:
                    max_score = score
                    best_set = feature_set
            


""" Feature Selection Search Using Backward Elimination. """
class BackwardSelection(FeatureSelection):

    def __init__( self, training_data ):
        super(BackwardSelection, self).__init__(training_data)

    def remove_feature():
        pass

    """ The Search Algorithm that will search for the best feature set. """
    def select(self):
        raise NotImplementedError






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
from scipy.spatial import distance
from sklearn import preprocessing

PRINTDEBUG = 1

""" The Default Contstruction for the Feature Subset Search Algorithms. """
class FeatureSelection(object):

    def __init__( self, training_data ):
        self.data = training_data
        print " [+] Training data passed in: "
        for instance in training_data:
            print instance
        print "\n"
        self.features = [instance.pop(1) for instance in copy.deepcopy(training_data)]
        self.number_of_features = len(self.features[0])
        self.classes = [instance.pop(0) for instance in copy.deepcopy(training_data)]

        if(PRINTDEBUG):
            print " [+] Feature Selection initialized with data: "
            for instance in self.data:
                print instance
            print "\n"
            print " [+] Feature Selection initialized with features: "
            print self.features
            print "\n"
            print " [+] Feature Selection initialized with classes: "
            print self.classes
            print "\n"

    """ The Nearest Neighbor Classifier. """
    def nearest_neighbor(self, new_instance, feature_set):
        classification = None
        min_distance = float("inf")
        for classified in self.data:
            if(PRINTDEBUG):
                print " [!] Testing Distance Too Instance: " , classified  
            c = classified[0]
            instance = [classified[1].pop(feature_number-1) for feature_number in feature_set]
            if(PRINTDEBUG):
                print " [!] Instance Features: " , instance  
            dist = distance.euclidean(instance, new_instance)

            if(PRINTDEBUG):
                print " [!] Distance from new instance: " , dist  
            if dist < min_distance:
                min_distance = dist
                classification = c
        return classification
                
    """ Evalution Function used for validation. Uses training data and the classifier. Gives the accuracy score. """
    def leave_one_out(self, set_of_features):
        correct = 0
        for i in range(0,len(self.classes)):
            unknown = self.data[i] 
            unknown = [unknown[1].pop(feature_number-1) for feature_number in set_of_features] 
            classification = self.nearest_neighbor(unknown, set_of_features)
            if classification == self.data[i][0]:
                correct+=1
        return correct/len(self.classes)
        

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
            print feature
            new_feature_set = copy.deepcopy(feature_set)
            if feature not in feature_set:
                new_feature_set.append(feature)
                feature_set_list.append(new_feature_set)
        return feature_set_list

    """ The Search Algorithm that will search for the best feature set. """
    def select(self):
        feature_sets = []
        while ( True ):
            for feature_set in self.add_feature(feature_sets):
                score = self.leave_one_out(s)
                if score > max_score:
                    max_score = score
                if len(s) == len(self.classes):
                    return max_score


""" Feature Selection Search Using Backward Elimination. """
class BackwardSelection(FeatureSelection):

    def __init__( self, training_data ):
        super(BackwardSelection, self).__init__(training_data)

    def remove_feature():
        pass

    """ The Search Algorithm that will search for the best feature set. """
    def select(self):
        raise NotImplementedError





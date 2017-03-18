
############################################################################
#                                                                          #
#    Classes for a Feature Searching.                                      # 
#                                                                          #
############################################################################

import copy
import bisect
import itertools

output = open('small44_forward_output.txt', 'a')

class FeatureSelection(object):
    def __init__( self, validator ):
        self.validator = validator
        self.number_of_features = len(self.validator.classifier.data[0])

    def select(self):
        raise NotImplementedError


class ForwardSelection(FeatureSelection):

    def __init__( self, validator):
        super(ForwardSelection, self).__init__(validator)


    """ Returns a list of new feature sets after adding each possible new feature to the existing set """ 
    def add_feature(self, feature_set):
        new_feature_set = []
        feature_set_list = []
        for feature in range(1,self.number_of_features):
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
        local_score = -1;
        feature_sets = [[]]
        while ( True ):
            feature_sets = self.add_feature(feature_sets)
            if len(feature_sets) == 0:
                return best_set, max_score
            local_score = 0
            for feature_set in feature_sets:
                score = self.validator.validate(feature_set)
                print "[!] Using Feature(s) ", feature_set, "Accuracy is ", score*100, "%."
                print >> output, "[!] Using Feature(s) ", feature_set, "Accuracy is ", score*100, "%."
                if score > max_score:
                    max_score = score
                    best_set = feature_set
                if score > local_score:
                    local_score = score
                    feature_sets = [ feature_set ]
            print >> output, "\n"
            


""" Feature Selection Search Using Backward Elimination. """
class BackwardSelection(FeatureSelection):

    def __init__( self, validator ):
        super(BackwardSelection, self).__init__(validator )

    def remove_feature(self, feature_set):
        new_feature_set = []
        feature_sets = []
        for i in range(1, self.number_of_features + 1):
            for s in feature_set:
                if i in s:
                    new_feature_set = copy.deepcopy(s)
                    new_feature_set.remove(i)
                    if new_feature_set not in feature_sets and len(new_feature_set) > 0:
                        feature_sets.append( new_feature_set )
        return feature_sets
        
    """ The Search Algorithm that will search for the best feature set. """
    def select(self):
        max_score = -1;
        local_score = -1;
        feature_sets = [ [ i for i in range(1,self.number_of_features) ] ]
        while ( True ):
            if len(feature_sets) == 0:
                return best_set, max_score
            local_score = 0
            for feature_set in feature_sets:
                score = self.validator.validate(feature_set)
                print "[!] Using Feature(s) ", feature_set, "Accuracy is ", score*100, "%."
                print >> output, "[!] Using Feature(s) ", feature_set, "Accuracy is ", score*100, "%."
                if score > max_score:
                    max_score = score
                    best_set = feature_set
                if score > local_score:
                    local_score = score
                    feature_sets = [ feature_set ]
            feature_sets = self.remove_feature(feature_sets)
            print "\n"






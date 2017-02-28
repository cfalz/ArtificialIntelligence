
############################################################################
#                                                                          #
#    Classes for a Classifiers.                                            # 
#                                                                          #
############################################################################

from scipy.spatial import distance

PRINTDEBUG = 0

class Classifier(object):

    def __init__(self, training_data):
        self.data = training_data

    def classify(self):
        raise NotImplementedError

class NearestNeighbor(Classifier):

    def __init__( self, training_data ):
        super(NearestNeighbor, self).__init__(training_data)

    """ The Nearest Neighbor Classifier. """
    def classify(self, new_instance, known_instances, feature_set):
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

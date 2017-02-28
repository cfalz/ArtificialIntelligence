  
############################################################################
#                                                                          #
#    Classes for a Validators.                                             # 
#                                                                          #
############################################################################

class Validator(object):

    def __init__(self, classifier):
        self.classifier = classifier

    def validate(self, set_of_features):
        raise NotImplementedError



class LeaveOneOut(Validator): 
    def __init__( self , classifier ):
        super(LeaveOneOut, self).__init__(classifier)

    """ Evalution Function used for validation. Uses training data and the classifier. Gives the accuracy score. """
    def validate(self, set_of_features):
        correct = 0
        for i in range(0,len(self.classifier.data)):
            unknown = self.classifier.data.pop(i)  
            known = self.classifier.data
            unknown_mod = [ unknown[feature_number] for feature_number in set_of_features ] 
            classification = self.classifier.classify(unknown_mod, known, set_of_features)
            if classification == unknown[0]:
                correct+=1
            self.classifier.data.insert(i,unknown)
        return float(correct)/float(len(self.classifier.data))

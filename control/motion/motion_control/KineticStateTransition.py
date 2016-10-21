from abc import ABCMeta, abstractclassmethod

class KineticStateTransition(metaclass=ABCMeta):
    
    def __init__(self, kineticContext):
        self.kineticContext = kineticContext
    
    @abstractclassmethod
    def doTransition(self):
        pass
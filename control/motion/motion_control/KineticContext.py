

class KineticContext:
    """Encapsulates the current kinetic state
    """
    
    def __init__(self):
        self.kineticState = None
        
    def setState(self, newKineticState):
        self.kineticState = newKineticState

    def getState(self):
        return self.kineticState()
    
    def move(self):
        self.kineticState.move()
    

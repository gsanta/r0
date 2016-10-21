
class KineticState:
    
    def __init__(self, kineticCommand, stateTransition):
        self.kineticCommand = kineticCommand
        self.stateTransition = stateTransition
        
    def move(self):
        self.kineticCommand.execute()
        self.stateTransition.doTransition()
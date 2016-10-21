from KineticCommand import KineticCommand

class TurnLeftCommand(KineticCommand):
    
    def __init__(self):
        KineticCommand.__init__(self)
        
    def execute():
        self.motorControl.turnLeft()
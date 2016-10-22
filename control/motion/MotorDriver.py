

class MotorDriver:
    
    def __init__(self, scheduler, kineticContext, kineticStateFactory):
        self.scheduler = scheduler
        self.kineticContext = kineticContext
        self.kineticStateFactory = kineticStateFactory


    def forward(self):
        self.kineticKontext.setState(
            self.kineticStateFactory.getForwardMotionState(self.kineticContext)
        )
        
        
        
                    


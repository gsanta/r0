

class MotorDriverTask:

    def __init__(self, kineticContext, taskRunner):
        self.kineticContext = kineticContext
        self.taskRunner = taskRunner

    def execute(self):
        self.kineticContext.move()
        self.taskRunner.run()

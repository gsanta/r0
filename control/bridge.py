import zerorpc
import motor_control as motor


class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name

    def forward(self, tf):
        return motor.forward(tf)

    def reverse(self, tf):
        return motor.reverse(tf)

    def turn_left(self, tf):
        return motor.turn_left(tf)

    def turn_right(self, tf):
        return motor.turn_right(tf)

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()

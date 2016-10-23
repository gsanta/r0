from enum import Enum

class KineticCommandState(Enum):
    FORWARD = 1,
    REVERSE = 2,
    TURN_LEFT = 3,
    TURN_RIGHT = 4,
    STOP = 5


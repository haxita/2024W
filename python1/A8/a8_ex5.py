# a8_ex5.py

from a8_ex3 import Energy

class Power(Energy):
    def __init__(self, x: float, y: float, z: int, current: float, resistance: float):

        super().__init__(x, y, z, current, resistance, time=1)

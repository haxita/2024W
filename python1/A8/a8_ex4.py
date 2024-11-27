# a8_ex4.py

from a8_ex2 import Electric_Circuits

class Charge_Flow(Electric_Circuits):
    def __init__(self, x: float, y: float, z: int, current: float, time: int):
        """
        Initializes an instance of the Charge_Flow class, extending Electric_Circuits.

        :param x: The current in the base circuit (float)
        :param y: The resistance in the base circuit (float)
        :param z: The time in the base circuit (int)
        :param current: The current for charge flow calculation (float)
        :param time: The time for charge flow calculation (int)
        """
        super().__init__(x, y, z)
        self.current = current
        self.time = time

    def to_string(self) -> str:
        """
        Returns a string representation of the Charge_Flow instance.

        :return: A string of the form
                 "Charge_Flow: x=<x_value>, y=<y_value>, z=<z_value>, current=<current_value>, time=<time_value>"
        """
        base_str = super().to_string()
        return f"{base_str}, current={self.current}, time={self.time}"

    def measure(self) -> float:
        """
        Calculates and returns the charge flow measure.

        Charge Flow is calculated using the formula:
            Charge Flow = current * time

        :return: The calculated charge flow as a float.
        """
        charge_flow = self.current * self.time
        return charge_flow
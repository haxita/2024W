# a8_ex3.py

from a8_ex2 import Electric_Circuits

class Energy(Electric_Circuits):
    def __init__(self, x: float, y: float, z: int, current: float, resistance: float, time: int):
        """
        Initializes an instance of the Energy class, extending Electric_Circuits.

        :param x: The current in the base circuit (float)
        :param y: The resistance in the base circuit (float)
        :param z: The time in the base circuit (int)
        :param current: The current for energy calculation (float)
        :param resistance: The resistance for energy calculation (float)
        :param time: The time for energy calculation (int)
        """
        super().__init__(x, y, z)
        self.current = current
        self.resistance = resistance
        self.time = time

    def to_string(self) -> str:
        """
        Returns a string representation of the Energy instance.

        :return: A string of the form
                 "Energy: x=<x_value>, y=<y_value>, z=<z_value>, current=<current_value>,
                  resistance=<resistance_value>, time=<time_value>"
        """
        base_str = super().to_string()
        return f"{base_str}, current={self.current}, resistance={self.resistance}, time={self.time}"

    def measure(self) -> float:
        """
        Calculates and returns the energy measure.

        Energy is calculated using the formula:
            Energy = current^2 * resistance * time

        :return: The calculated energy as a float.
        """
        energy = (self.current ** 2) * self.resistance * self.time
        return energy
# a8_ex2.py

class Electric_Circuits:
    def __init__(self, x: float, y: float, z: int):
        """
        Initializes an instance of the Electric_Circuits class.

        :param x: The current in the circuit (float)
        :param y: The resistance in the circuit (float)
        :param z: The time in the circuit (int)
        """
        self.x = x
        self.y = y
        self.z = z

    def to_string(self) -> str:
        """
        Returns a string representation of the instance.

        :return: A string of the form "Electric_Circuits: x=<x_value>, y=<y_value>, z=<z_value>"
        """
        return f"{type(self).__name__}: x={self.x}, y={self.y}, z={self.z}"

    def measure(self) -> float:
        """
        Returns the measure of the electric circuit. Must be implemented by subclasses.

        :raise NotImplementedError: If called on the base class.
        """
        raise NotImplementedError("The measure method must be implemented by subclasses.")
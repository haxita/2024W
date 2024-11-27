class Voltage:
    def __init__(self, current: float, resistance: float):
        self.current = current
        self.resistance = resistance

    def print(self):
        sign = "+" if self.current >= 0 else "-"
        # Use absolute value for current to avoid double negative signs
        print(f"{sign}{abs(self.current):.1f} amps + {self.resistance:.1f} ohms")

    def volt(self) -> float:
        return self.current * self.resistance

    def increase_resistance(self, delta: float):
        if not isinstance(delta, (float, int)):
            raise TypeError(f"Please provide float value instead of {type(delta).__name__}")
        self.resistance += delta

    @staticmethod
    def add_all(volt_obj: "Voltage", *volt_objs: "Voltage") -> "Voltage":
        # Check if all objects are instances of Voltage
        all_objs = [volt_obj] + list(volt_objs)
        for obj in all_objs:
            if not isinstance(obj, Voltage):
                raise TypeError("Can only add objects of type 'Voltage'")

        # Check if all currents are equal
        first_current = volt_obj.current
        for obj in volt_objs:
            if obj.current != first_current:
                raise ValueError("The current must be equal")

        # Sum resistances
        total_resistance = sum(obj.resistance for obj in all_objs)
        return Voltage(first_current, total_resistance)


# Example program execution:

# First Example
print("First Example Output:")
c1 = Voltage(-5.0, 20)
c1.print()
c2 = Voltage(3.0, 4.0)
c2.print()
print(c2.volt())
print()

# Second Example
print("Second Example Output:")
c1 = Voltage(10.0, 2.0)
c1.print()
c2 = Voltage(10.0, 5.0)
c1.increase_resistance(5)
c1.print()
c_sum = Voltage.add_all(c1, c1, c2, Voltage(10.0, 5.0))
c_sum.print()
c1.print()

# Handling errors
print("\nError Handling Output:")
try:
    Voltage.add_all(100.0)
except TypeError as e:
    print(f"TypeError: {e}")

try:
    c1.increase_resistance('abc')
except TypeError as e:
    print(f"TypeError: {e}")

try:
    c3 = Voltage(15.0, 22.0)
    Voltage.add_all(c1, c3)
except ValueError as e:
    print(f"ValueError: {e}")
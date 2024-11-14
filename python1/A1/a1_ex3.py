# Write a program that computes and prints several metrics of a cylindrical tank given a user-specified
# radius and height (see the example input and output below for how it must look like). Both
# numbers have to be converted to float and are assumed to be meters. Take 3.14159 as the value for
# π. The metrics to compute are the following:
# • The surface area of the tank (float), which includes both the side and the top and bottom
# areas.
# • The volume of the tank (float)
# • The amount of water required to fill the tank, given that the tank needs to be filled up to 90%
# of its volume (float).
# • The amount of paint needed to paint the exterior surface of the tank (float). For every square
# meter of surface, 0.65 liters of paint are required.
# • The number of steel plates needed to construct the tank (int). Each steel plate covers 2square
# meters of surface. For example, a surface area of 85 square meters requires 43 plates.
# All float results must be printed with 2 decimal places.
# Example input and output:
# Radius (in metres): 2.4
# Height (in metres): 5.5
# Surface area of the tank: 119.13
# Volume of the tank: 99.53
# Amount of water needed: 89.57
# Litres of paint needed: 77.43
# Number of plates needed: 60

radius = float(input("Radius (in metres): "))
height = float(input("Height (in metres): "))

pi = 3.14159

Surface_Area = 2 * pi * radius * height + 2 * pi * (radius ** 2)
print(f"Surface area of the tank: {Surface_Area:.2f}")

Volume = pi * (radius ** 2) * height
print(f"Volume of the tank: {Volume:.2f}")

Water_Needed90 = 0.9 * Volume
print(f"Amount of water needed: {Water_Needed90:.2f}")

Paint_Needed65 = Surface_Area * 0.65
print(f"Litres of paint needed: {Paint_Needed65:.2f}")

Plates_Needed = int ( Surface_Area / 2 ) +1

print(f"Number of plates needed: {Plates_Needed}")


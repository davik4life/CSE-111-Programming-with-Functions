import math

width_of_tire = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio_of_tire = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_of_tire = float(input("Enter the diameter of the wheel in inches (ex 15): "))
piData = math.pi

volume = piData * width_of_tire ** 2 * aspect_ratio_of_tire * (width_of_tire * aspect_ratio_of_tire + 2540 * diameter_of_tire)/10000000000
print()
print(f"The approximate volume is {float(volume):.2f} liters")

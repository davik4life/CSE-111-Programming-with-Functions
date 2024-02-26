import math
from datetime import datetime

width_of_tire = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio_of_tire = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_of_tire = int(input("Enter the diameter of the wheel in inches (ex 15): "))
piData = math.pi

volume = piData * width_of_tire ** 2 * aspect_ratio_of_tire * (width_of_tire * aspect_ratio_of_tire + 2540 * diameter_of_tire)/10000000000
print()
print(f"The approximate volume is {float(volume):.2f} liters")


"""
The prove milestone required you to write a program named tire_volume.py 
that computes the approximate volume of air inside a tire. 

Add code near the end of that program that does the following:
"""
#Gets the current date and time from the computer's OS.
current_datetime = datetime.now()

# Exceeeding the requirements.

"""
    Tire Sizes: 
    225/40 R18 Price = $30. 
    225/45 R17 Price = $31.24. 
    195/65 R15 Price = $39.19. 
    215/55 R16 Price = $34.99
"""

price = ""

if width_of_tire  == 225 and (aspect_ratio_of_tire == 40 or diameter_of_tire == 18):
    price = "$30."
elif width_of_tire == 225 and (aspect_ratio_of_tire == 45 or diameter_of_tire == 17):
    price = "$31.24."
elif width_of_tire == 195 and (aspect_ratio_of_tire == 65 or diameter_of_tire == 15):
    price = "$39.19."
elif width_of_tire == 215 and (aspect_ratio_of_tire == 55 or diameter_of_tire == 16):
    price = "$34.99."
else:
    price = "$90"

# Add a line space.
print()

# Prints the Price of the specified diemension.
print(f"Price: {price}")

# Add a line space.
print()
buy_prompt = input(f"Do you want to buy tire with the following dimension: W: {width_of_tire}, A: {aspect_ratio_of_tire}, D: {diameter_of_tire}?")

#Append the Phone number to the volume.txt file.
with open("volumes.txt", "at") as volumes:
    print(f"{current_datetime:%Y-%m-%d}, {width_of_tire}, {aspect_ratio_of_tire}, {diameter_of_tire}, {volume:.2f}", file=volumes)
    if buy_prompt.lower() == "yes":
        name = input("Please enter your name: ")
        phone = int(input("Please enter your phone number: "))
        print(f"Name: {name}, Phone: {phone}", file=volumes)
        print()
        print("Thank you for your interest. Our Customer Service Rep would reach out to you shortly.")
    else:
        print()
        print("Thank you for your time.")
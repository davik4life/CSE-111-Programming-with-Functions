"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

#Ask for a persons age:

defaultNum = 220
age = input("Please enter your age: ")
heart_rate = int(defaultNum) - int(age)
min_rate = int(heart_rate * 65 / 100)
max_rate = int(heart_rate * 85 / 100)

# Display the solution

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {min_rate} and {max_rate} beats per minute.")



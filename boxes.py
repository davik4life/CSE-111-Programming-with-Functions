import math;
"""
    In our modern world economy, many items are manufactured 
    in large factories, then packed in boxes and shipped to 
    distribution centers and retail stores. A common question 
    for employees who pack items is “How many boxes do we need?”
"""

number_of_items = int(input("Enter the number of items: "))
number_of_items_per_box = int(input("Enter the number of items per box: "))
needed_boxes = math.ceil(number_of_items / number_of_items_per_box)
print()
print(f"For {number_of_items} items, packing {number_of_items_per_box} items in each box, you will need {needed_boxes} boxes.")
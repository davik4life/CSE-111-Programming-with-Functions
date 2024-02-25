from datetime import datetime

"""
Work as a team to write a Python program named discount.py
that gets a customer’s subtotal as input and gets the current
day of the week from your computer’s operating system. 

Your program must not ask the user to enter the day of 
the week. Instead, it must get the day of the week from your 
computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or 
Wednesday, your program must subtract 10% from the 
subtotal. Your program must then compute the total amount 
due by adding sales tax of 6% to the subtotal. 

Your program must print the discount amount if applicable, 
the sales tax amount, and the total amount due.
"""

# Get the current date and time

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

subtotal = float(input("Please enter the subtotal: "))
discount_amount = subtotal * 10 / 100
discounted_amount = subtotal * 90 / 100 
tax_amount = discounted_amount * 6 / 100
tax_amount_else = subtotal * 6 / 100
total =  round(discounted_amount + tax_amount, 2)
total_else =  round(subtotal + tax_amount_else, 2)
total_with_discount =  round(tax_amount, 2)

if  subtotal >= 50 and (day_of_week == 1 or day_of_week == 6):
    print(f"Discount amount: {round(discount_amount, 2)}")
    print(f"Sales tax amount: {round(tax_amount, 2)}")
    print(f"Total: {round(total, 2)}")
else:
    print(f"Sales tax amount: {round(tax_amount_else, 2)}")
    print(f"Total: {total_else}")
    
    
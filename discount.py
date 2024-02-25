from datetime import datetime

# Get the current date and time
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

reps = True

while reps:
    subtotal = float(input("Please enter the subtotal: "))
    # Check the value of subtotal before executing further.
    if subtotal == 0:
        break
    discount_amount = subtotal * 10 / 100
    discounted_amount = subtotal * 90 / 100 
    tax_amount = discounted_amount * 6 / 100
    tax_amount_else = subtotal * 6 / 100
    total =  round(discounted_amount + tax_amount, 2)
    total_else =  round(subtotal + tax_amount_else, 2)

    if  subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
        print(f"Discount amount: {round(discount_amount, 2)}")
        print(f"Sales tax amount: {round(tax_amount, 2)}")
        print(f"Total: {total}")
    elif subtotal < 50 and (day_of_week == 1 or day_of_week == 2):
        print(f"You are not purchasing enough to recieve a discount. you need {50 - subtotal} worth of purchase to qualify for a discount.")
        print(f"Sales tax amount: {round(tax_amount_else, 2)}")
        print(f"Total: {total_else}")
    else:
        print(f"Sales tax amount: {round(tax_amount_else, 2)}")
        print(f"Total: {total_else}")
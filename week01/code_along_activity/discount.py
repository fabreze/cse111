"""
Author: Fabrizio Caballero

Purpose: Calculate the customer discount on Tuesday and Wednesday for a retail store. 
"""
from datetime import datetime
TUESDAY = 1
WEDNESDAY = 2
MIN_SUBTOTAL_FOR_DISCOUNT = 50
DISCOUNT_RATE = .10
SALES_TAX_RATE = .06


# Ask user for the subtotal
subtotal = float(input("Please enter the subtotal: "))

# Get the day of the week
current_date_time = datetime.now()
weekday = current_date_time.weekday()

# Compute and print the discount amount
weekday = TUESDAY
if weekday == TUESDAY or weekday == WEDNESDAY:
    if subtotal >= MIN_SUBTOTAL_FOR_DISCOUNT:
        discount = subtotal * DISCOUNT_RATE
        subtotal -= discount
        print(f"\nDiscount Amount: -${discount:.2f}\n")
    else:
        amount_for_discount = MIN_SUBTOTAL_FOR_DISCOUNT - subtotal
        print(f"\nSpend ${amount_for_discount:.2f} more to receive a {DISCOUNT_RATE * 100:.0f}% discount!!!\n")

# Compute and print the sales tax amount
sales_tax = subtotal * SALES_TAX_RATE
print(f"Sales Tax Amount: ${sales_tax:.2f}\n")

# Compute and print the total amount due
total = subtotal + sales_tax
print(f"Total Amount: ${total:.2f}\n")
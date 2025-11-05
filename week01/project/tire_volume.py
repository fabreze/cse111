"""
Author: Fabrizio Caballero

Purpose: Write a program that will accept user input that describes a tire then calculate and display the tire's volume. Record the tire information in a log file.
Enhancements: I created three functions, one function is used to calculate the volume of the tire. 
The second function validates whether the input it recieves is an integer, if not it will keep asking the user for a 
valid whole number. The third function checks if the user wants to close the program, and validates if the user's response
is yes or no, otherwise it keeps looping. Finally, the program is put into a while loop, meaning that the user can keep
inputting tire volumes until they close the program.
"""
import math
from datetime import datetime

def calculate_volume(width, aspect_ratio, diameter):
    volume = float((math.pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter))/10000000000)
    return volume

def validate_integer(integer):
    is_valid_integer = False
    while not is_valid_integer:
        try:
            integer = int(integer)
            is_valid_integer = True
        except ValueError:
            integer = input("\nInput invalid! Please enter a whole number without any commas: ")
    return integer

def validate_close_action(action):
    is_valid_action = False
    while not is_valid_action:
        if action == "yes" or action == "no":
            is_valid_action = True
        else:
            action = input("\nError. Please respond with YES or NO: ").lower().strip()
    return action


current_date_time = datetime.now()
current_date = datetime.date(current_date_time)

is_open = True
print("Welcome to the tire volume calculation program! Get started by inputting the following values:")

while(is_open):
    width = validate_integer(input("\nEnter the width of the tire in milimeters (e.g. 205): "))
    aspect_ratio = validate_integer(input("\nEnter the aspect ratio of the tire (e.g. 60): "))
    diameter = validate_integer(input("\nEnter the diameter of the wheel in inches (e.g. 15): "))

    volume = calculate_volume(width, aspect_ratio, diameter)

    print(f"\nThe approximate volume is {volume:.2f} liters")

    with open("volumes.txt", mode="at") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")
    
    print("\nThis calculation has been recorded.")

    keep_open = validate_close_action(input("\nWould you like to calculate the volume of another tire? YES or NO? ").lower().strip())

    if(keep_open == "no"):
        is_open = False
        print("\nThank you for using this tire volume calculation program. Have a nice day!")
    else:
        print("\nPlease input the following values:")
    
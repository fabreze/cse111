"""
Author: Fabrizio Caballero

Purpose: Write a program that will accept user input that describes a tire then calculate and display the tire's volume. Record the tire information in a log file.
Enhancements: 
"""
import math

width = int(input("Enter the width of the tire in milimeters (e.g. 205): "))
aspect_ratio = int(input("\nEnter the aspect ratio of the tire (e.g. 60): "))
diameter = int(input("\nEnter the diameter of the wheel in inches (e.g. 15): "))

volume = float((math.pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2,540 * diameter))/10000000000)

print(f"\nThe approximate volume is {volume:.2f} liters")
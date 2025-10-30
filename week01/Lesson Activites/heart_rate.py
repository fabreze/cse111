# W01 Learning Activities: Python Review - Lesson Activity
import math

age = int(input("Please enter your age: "))

maximum_heart_rate = 220 - age
max_exercise_heart_rate = maximum_heart_rate * .85
min_exercise_heart_rate = maximum_heart_rate * .65

print(f"When you exercise to strengthen your heart, you should \n"
      f"keep your heart rate between {min_exercise_heart_rate:.0f} and {max_exercise_heart_rate:.0f} beats per minute.")

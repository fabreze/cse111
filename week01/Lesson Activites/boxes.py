# W01 Prepare 2: Calling Functions - Lesson Activity
import math

num_items = float(input("Enter the number of items: "))
num_items_per_box = float(input("Enter the number of items per box: "))
num_of_boxes = math.ceil(num_items / num_items_per_box)

print(f"For {num_items:.0f} items, packing {num_items_per_box:.0f} items in each box, you will need {num_of_boxes} boxes")
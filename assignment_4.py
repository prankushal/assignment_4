# Problem 1: Current Date and Time
# Write a Python program using the datetime module
# to display the current date and time.
#
# Example Output:
# Current Date and Time: 2026-09-26 11:30:45

from datetime import datetime

now = datetime.now()

print("Current Date and Time is:", now.strftime("%Y-%m-%d %H:%M:%S"))


# Problem 2: Dictionary to JSON
# Create a dictionary containing a student's
# name, age, and department.
# Convert the dictionary into a JSON string
# using the json module and print it.
#
# Input:
# student = {"name": "Rahim", "age": 20, "department": "CSE"}
#
# Expected Output:
# {"name": "Rahim", "age": 20, "department": "CSE"}

import json

student = {"Name": "Rahim", "Age": 20, "Department": "CSE"}

json_txt = json.dumps(student)

print(json_txt)
print(type(json_txt))  
print(type(student))  


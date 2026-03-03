import re

# Prompt user for employee ID
emp_id = input("Enter the employee id: ")

# Define the pattern for a valid employee ID
pattern = r"^(DH|DM)-\d{4}$"

# Check if the entered ID matches the pattern
if re.match(pattern, emp_id):
    print("The employee id is valid")
else:
    print("The employee id is invalid")

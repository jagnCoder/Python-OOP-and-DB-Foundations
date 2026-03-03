email_id = input("Enter the email id: ")

# Check for space or missing '@'
if ' ' in email_id or '@' not in email_id:
    print("Invalid email id")
else:
    # Extract the name part before the '@'
    name = email_id.split('@')[0]
    print("Name:", name.capitalize())

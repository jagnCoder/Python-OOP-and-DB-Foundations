def reverse_number(number):
    """Generator function to yield even digits from the number (reversed)."""
    num_str = str(number)  # Convert number to string
    for digit in reversed(num_str):  # Iterate from right to left
        if int(digit) % 2 == 0:  # Check if digit is even
            yield digit  # Yield the even digit

# Main program starts here
number = int(input("Enter a number: "))

# Validate the input
if number < 0 or number < 10 or number == 0:
    print("Invalid input")
else:
    # Collect yielded even digits
    yielded_digits = list(reverse_number(number))

    # Check if any even digits were yielded
    if not yielded_digits:
        print("Invalid input")
    else:
        # Combine yielded digits into a string
        combined_string = ''.join(yielded_digits)
        print("Your new password is:", combined_string)

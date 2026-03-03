# Mapping table for letters A-Z with corresponding numbers
mapping_table = {chr(i): i - 64 for i in range(65, 91)}  # A=1, B=2, ..., Z=26

def find_lucky_number(name, table):
    """Generator function to find the lucky number based on the name."""
    # Check if the name is fully uppercase
    if not name.isupper():
        yield 0
        yield "Invalid name"
        return

    lucky_sum = 0

    # Calculate the lucky number
    for character in name:
        if character.isalpha():  # Check if the character is an alphabet
            lucky_sum += table[character]  # Add corresponding value from table

    yield lucky_sum  # Yield the lucky sum

def main():
    # Get input from the user
    name = input("Enter your name in uppercase: ")
    
    # Call the generator function
    for value in find_lucky_number(name, mapping_table):
        print(value)

# Execute the main function
if __name__ == "__main__":
    main()

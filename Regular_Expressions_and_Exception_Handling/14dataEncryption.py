message = input("Actual message: ").lower()
encrypted_message = ""

# Loop through each character in the message
for char in message:
    # Encrypt alphabetic characters and digits
    if char.isalpha() or char.isdigit():
        encrypted_message += chr(ord(char) + 1)
    else:
        encrypted_message += char  # Keep non-alphanumeric characters unchanged

print("Encrypted message:", encrypted_message)

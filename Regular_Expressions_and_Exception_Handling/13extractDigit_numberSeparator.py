statement = input("Enter the statement: ")
result = []

# Split the input statement into words
words = statement.split()

# Loop through each word to check if it's a digit
for word in words:
    if word.isdigit():
        result.append(word)

# Print the result as a list of digits found
print(result)

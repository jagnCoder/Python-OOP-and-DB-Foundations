try:
    first_num = float(input("Enter the First Number: "))
    second_num = float(input("Enter the Second Number: "))
    operator = input("Enter the Operator (+ - * /): ")

    if operator == '+':
        result = first_num + second_num
        print("The answer is:", int(result) if result.is_integer() else result)

    elif operator == '-':
        result = first_num - second_num
        print("The answer is:", int(result) if result.is_integer() else result)

    elif operator == '*':
        result = first_num * second_num
        print("The answer is:", int(result) if result.is_integer() else result)

    elif operator == '/':
        if second_num == 0:
            raise ZeroDivisionError
        result = first_num / second_num
        print("The answer is:", int(result) if result.is_integer() else result)

    else:
        print("Sorry. You have entered an invalid operator.")

except ValueError:
    print("Sorry. You have entered an invalid number.")

except ZeroDivisionError:
    print("Sorry! Division by zero is not possible.")

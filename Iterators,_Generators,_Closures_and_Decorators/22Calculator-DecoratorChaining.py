def argument_count(func):
    """Decorator to count the number of arguments passed to the function."""
    def inner(*args):
        print("No. of arguments passed:", len(args))
        result = func(*args)  # Call the original function with arguments
        return result
    return inner

def print_function_name(func):
    """Decorator to print the name of the function being executed."""
    def inner(*args):
        print("Doing", func.__name__)
        result = func(*args)  # Call the original function with arguments
        return result
    return inner

@argument_count
@print_function_name
def addition(*args):
    total = 0
    for value in args:
        total += value  # Accumulate the total
    print("result =", total)

@argument_count
@print_function_name
def subtraction(*args):
    result = args[0]  # Initialize with the first argument
    for argument in args[1:]:
        result -= argument  # Subtract subsequent arguments
    print("result =", result)

@argument_count
@print_function_name
def multiplication(*args):
    result = 1
    for argument in args:
        result *= argument  # Multiply all arguments
    print("result =", result)

@argument_count
@print_function_name
def division(*args):
    result = args[0]  # Initialize with the first argument
    for argument in args[1:]:
        if argument == 0:  # Prevent division by zero
            print("Error: Division by zero")
            return
        result /= argument  # Divide by subsequent arguments
    print("result =", result)

# Example usage of the calculator functions
addition(5, 10, 15)
subtraction(20, 5, 2)
multiplication(4, 5, 2)
division(40, 5, 2)
division(10, 0)  # Testing division by zero

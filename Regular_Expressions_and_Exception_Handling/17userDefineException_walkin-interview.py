class AgeException(Exception):
    pass

class SalaryException(Exception):
    pass

try:
    name = input("Enter the Name:")
    age = int(input("Enter the Age:"))

    # Age validation
    if age < 18 or age > 50:
        raise AgeException("Registration Failed. Age should be greater than 18 and less than 50")

    salary = float(input("Enter the Salary:"))

    # Salary validation
    if salary <= 0:
        raise SalaryException("Registration Failed. Salary cannot be a negative number or zero")

    gender = input("Enter the Gender(f/m):")

    print("Registration Successful")

except AgeException as ae:
    print(ae)

except SalaryException as se:
    print(se)

finally:
    print("Best Wishes")

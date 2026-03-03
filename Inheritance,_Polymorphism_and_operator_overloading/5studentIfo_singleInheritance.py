class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, regno, percentage):
        super().__init__(name, age)
        self.regno = regno
        self.percentage = percentage

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.regno)
        print("Percentage:", self.percentage)


# MAIN PROGRAM
name = input("Enter name: ")
age = int(input("Enter age: "))
regno = input("Enter registration number: ")
percentage = float(input("Enter percentage: "))

student_obj = Student(name, age, regno, percentage)
student_obj.display()

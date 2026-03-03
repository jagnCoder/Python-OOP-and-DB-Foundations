# 18ProjectAllocation.py

# Input number of employees
number_of_employees = int(input("Enter the number of employees: "))

# Initialize empty list for employee scores
employee_score_list = []

# Collect employee scores
for employee in range(1, number_of_employees + 1):
    employee_id = input(f"Enter employee ID for employee {employee}: ")
    assessment_scores = input("Enter assessment scores as comma-separated values: ")
    scores = list(map(int, assessment_scores.split(",")))  # Convert scores to integers
    employee_score_list.append([employee_id] + scores)  # Create a list with employee_id and scores

class ProjectAllocation:
    def __init__(self, score_list):
        self.score_list = score_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.score_list):
            raise StopIteration

        # Fetch current employee data using index
        current_employee_data = self.score_list[self.index]
        employee_id = current_employee_data[0]
        scores = current_employee_data[1:]  # Extract scores
        average_score = sum(scores) / len(scores)  # Calculate average score

        self.index += 1  # Increment index
        return {employee_id: average_score}  # Return as dictionary

# Create ProjectAllocation object using employee_score_list
project_allocation = ProjectAllocation(employee_score_list)

# Print employees' average scores
print("Employees' average scores:")
for item in project_allocation:
    print(item)

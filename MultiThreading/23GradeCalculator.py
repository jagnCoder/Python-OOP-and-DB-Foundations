import threading

class GradeCalculator(threading.Thread):
    def __init__(self, name, marks_list):
        super().__init__()
        self.candidate_name = name
        self.scores = marks_list
        self.grade = ""

    def run(self):
        total_score = sum(self.scores)
        average = total_score / len(self.scores)

        if 80 <= average <= 100:
            self.grade = 'A'
        elif 60 <= average < 80:
            self.grade = 'B'
        elif 40 <= average < 60:
            self.grade = 'C'
        else:
            self.grade = 'E'

        print(f"{self.candidate_name}: {self.grade}")

def main():
    number_of_candidates = int(input("Enter the number of candidates: "))

    thread_list = []

    for _ in range(number_of_candidates):
        candidate_string = input("Enter candidate details in format 'Name:score1:score2:score3:score4:score5': ")
        parts = candidate_string.split(':')
        name = parts[0]
        scores = list(map(int, parts[1:]))

        # Create a GradeCalculator object and add it to the thread list
        grade_calculator = GradeCalculator(name, scores)
        thread_list.append(grade_calculator)

    # Start all threads
    for thread in thread_list:
        thread.start()

    # Wait for all threads to finish
    for thread in thread_list:
        thread.join()

# Run the main function
if __name__ == "__main__":
    main()

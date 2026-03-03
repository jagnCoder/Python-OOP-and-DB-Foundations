import threading

class Operations:
    def bubble_sort(self, number_list):
        for i in range(len(number_list) - 1):
            for j in range(len(number_list) - i - 1):
                if number_list[j] > number_list[j + 1]:
                    # Swap the numbers
                    number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
        
        print("The sorted list is:")
        print(number_list)
        return number_list


class SortThread(threading.Thread):
    def __init__(self, list_of_numbers):
        super().__init__()
        self.list_of_numbers = list_of_numbers
        self.sorted_list = []

    def run(self):
        operations = Operations()
        self.sorted_list = operations.bubble_sort(self.list_of_numbers)


class SearchThread(threading.Thread):
    def __init__(self, sorted_list, search_key):
        super().__init__()
        self.sorted_list = sorted_list
        self.search_key = search_key

    def run(self):
        operations = Operations()
        for index in range(len(self.sorted_list)):
            if self.sorted_list[index] == self.search_key:
                print(f"Searched element is present at position {index + 1}")
                return
        print("Searched element is not present in the list.")


def main():
    number_of_elements = int(input("Enter number of elements: "))
    numbers = []

    for i in range(number_of_elements):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    search_element = int(input("Enter the element you want to search: "))

    sort_thread = SortThread(numbers)
    search_thread = SearchThread([], search_element)

    sort_thread.start()  # Start the sorting thread
    sort_thread.join()   # Wait for sort_thread to finish

    search_thread.sorted_list = sort_thread.sorted_list
    search_thread.start()  # Start the search thread

    search_thread.join()   # Wait for search_thread to finish


if __name__ == "__main__":
    main()

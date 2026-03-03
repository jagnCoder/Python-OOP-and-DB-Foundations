import threading

class MultithreadingDemo(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = None

    def set_name(self, name):
        """Set the name of the thread."""
        self.name = name

    def get_name(self):
        """Get the name of the thread."""
        return self.name

    def run(self):
        """Run method for the thread execution."""
        # Set the thread name using the current thread's name
        self.set_name(threading.current_thread().name)
        print(f"{self.get_name()} is running\n")  # Print the thread name

class Multithread:
    def main(self):
        number_of_threads = int(input("Enter the number of threads: "))

        for i in range(number_of_threads):
            thread = MultithreadingDemo()  # Create an object of MultithreadingDemo
            name="Thread "+str(i+1)
            thread.set_name(name)
            thread.start()  # Start the thread

# Execute the main function
multithread = Multithread()
multithread.main()

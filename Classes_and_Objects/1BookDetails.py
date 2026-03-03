class Book:
    def __init__(self, book_name, book_price, author_name):
        self.__book_name = book_name
        self.__book_price = book_price
        self.__author_name = author_name

    # Getter methods
    def get_book_name(self):
        return self.__book_name

    def get_book_price(self):
        return self.__book_price

    def get_author_name(self):
        return self.__author_name

    # Setter method for price
    def set_book_price(self, new_price):
        self.__book_price = new_price


# Taking user inputs
book_name = input("Enter the book name: ")
book_price = float(input("Enter the price: "))
author_name = input("Enter the author name: ")

# Creating object
book_obj = Book(book_name, book_price, author_name)

# Printing details before price update
print("\nBook details before price renewal:")
print("Book Name:", book_obj.get_book_name())
print("Book Price:", book_obj.get_book_price())
print("Author Name:", book_obj.get_author_name())

# New price input
new_price = float(input("\nEnter the new price: "))

# Update price
book_obj.set_book_price(new_price)

# Printing details after price update
print("\nBook details after price renewal:")
print("Book Name:", book_obj.get_book_name())
print("Book Price:", book_obj.get_book_price())
print("Author Name:", book_obj.get_author_name())

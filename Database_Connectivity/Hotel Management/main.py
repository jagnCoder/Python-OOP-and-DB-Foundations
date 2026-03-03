from hotel_management_system import HotelManagementSystem

def main():
    db_config = {
        'user': 'root',
        'password': 'jaganMysql@123',
        'host': 'localhost',
        'database': 'accenturepydb'
    }

    # Prompt user to enter address
    address = input("Enter the address: ").strip()

    # Establish database connection
    hotel_system = HotelManagementSystem(db_config)

    # Retrieve customer details
    customer_list = hotel_system.retrieve_customer_details(address)

    if not customer_list:
        print("Invalid Address")
    else:
        counter = 1
        for hotel_object in customer_list:
            print("="*30)
            print(f"~~~Customer details {counter}~~~")
            print("-"*30)
            print("Room Number:", hotel_object.get_room_no())
            print("Customer Name:", hotel_object.get_cust_name())
            print("Phone Number:", hotel_object.get_phone_number())
            no_of_days = hotel_object.get_no_of_days()
            print("Number of Days:", no_of_days)
            print("="*30)
            counter += 1

    hotel_system.close()

if __name__ == "__main__":
    main()

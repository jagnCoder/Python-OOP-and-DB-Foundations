import mysql.connector
from hotel import Hotel
from datetime import datetime

class HotelManagementSystem:
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)

    def retrieve_customer_details(self, input_address):
        result_list = []
        cursor = self.conn.cursor()

        query = """
        SELECT room_no, cust_name, phone_number, from_date, to_date
        FROM hotel
        WHERE address = %s AND DATEDIFF(to_date, from_date) > 3
        """
        
        cursor.execute(query, (input_address,))
        records = cursor.fetchall()

        if not records:
            return result_list

        for record in records:
            room_no, cust_name, phone_number, from_date, to_date = record
            #from_date = datetime.strptime(from_date, '%Y-%m-%d')  to Adjust date format if necessary
            #to_date = datetime.strptime(to_date, '%Y-%m-%d')
            hotel = Hotel(room_no, cust_name, phone_number, from_date, to_date)
            result_list.append(hotel)

        return result_list

    def close(self):
        self.conn.close()

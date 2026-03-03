class Hotel:
    def __init__(self, room_no, cust_name, phone_number, from_date, to_date):
        self.room_no = room_no
        self.cust_name = cust_name
        self.phone_number = phone_number
        self.from_date = from_date
        self.to_date = to_date

    def get_room_no(self):
        return self.room_no

    def get_cust_name(self):
        return self.cust_name

    def get_phone_number(self):
        return self.phone_number

    def get_no_of_days(self):
        return (self.to_date - self.from_date).days

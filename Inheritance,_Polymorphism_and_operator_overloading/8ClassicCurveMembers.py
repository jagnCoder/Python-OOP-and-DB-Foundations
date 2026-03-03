class Member:
    def __init__(self, customer_id, customer_name, email_id):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email_id = email_id


class GoldMember(Member):
    def __init__(self, customer_id, customer_name, email_id):
        super().__init__(customer_id, customer_name, email_id)
        self.discount_amount = 0

    def calculate_discount(self, purchase_amount):
        discount = 0.10 * purchase_amount
        self.discount_amount = purchase_amount - discount


class DiamondMember(Member):
    def __init__(self, customer_id, customer_name, email_id):
        super().__init__(customer_id, customer_name, email_id)
        self.discount_amount = 0

    def calculate_balance(self, purchase_amount):
        discount = 0.20 * purchase_amount
        self.discount_amount = purchase_amount - discount


# MAIN PROGRAM
print("1. Gold Membership")
print("2. Diamond Membership")

choice = int(input("Enter your choice (1 or 2): "))

customer_id = input("Enter customer ID: ")
customer_name = input("Enter customer name: ")
email_id = input("Enter email ID: ")
purchase_amount = float(input("Enter purchase amount: "))

if choice == 1:
    g_account_obj = GoldMember(customer_id, customer_name, email_id)
    g_account_obj.calculate_discount(purchase_amount)

    print("Member Details")
    print(g_account_obj.customer_id, g_account_obj.customer_name,
          g_account_obj.email_id, g_account_obj.discount_amount)

elif choice == 2:
    d_account_obj = DiamondMember(customer_id, customer_name, email_id)
    d_account_obj.calculate_balance(purchase_amount)

    print("Member Details")
    print(d_account_obj.customer_id, d_account_obj.customer_name,
          d_account_obj.email_id, d_account_obj.discount_amount)

class MonthlyExpense:
    def __init__(self):
        self.household_exp = 0.0
        self.medical_exp = 0.0

    def set_household_exp(self, value):
        self.household_exp = value

    def set_medical_exp(self, value):
        self.medical_exp = value

    def get_household_exp(self):
        return self.household_exp

    def get_medical_exp(self):
        return self.medical_exp

    def calculate_november_month_expense(self):
        return self.household_exp + self.medical_exp

    def calculate_december_month_expense(self):
        return self.household_exp + self.medical_exp

    def __add__(self, exp_obj):
        result = MonthlyExpense()
        result.household_exp = self.household_exp + exp_obj.household_exp
        result.medical_exp = self.medical_exp + exp_obj.medical_exp
        return result

    def calculate_total_expense(self):
        return self.household_exp + self.medical_exp


# MAIN PROGRAM
nov_obj = MonthlyExpense()
nov_household = float(input("Enter November household expenses: "))
nov_medical = float(input("Enter November medical expenses: "))
nov_obj.set_household_exp(nov_household)
nov_obj.set_medical_exp(nov_medical)
nov_total = nov_obj.calculate_november_month_expense()

dec_obj = MonthlyExpense()
dec_household = float(input("Enter December household expenses: "))
dec_medical = float(input("Enter December medical expenses: "))
dec_obj.set_household_exp(dec_household)
dec_obj.set_medical_exp(dec_medical)
dec_total = dec_obj.calculate_december_month_expense()

print("November Expenses (in $):", nov_total)
print("December Expenses (in $):", dec_total)

total_obj = nov_obj + dec_obj
total_expense = total_obj.calculate_total_expense()

print("Total Expenses for the month of Nov and Dec (in $):", total_expense)

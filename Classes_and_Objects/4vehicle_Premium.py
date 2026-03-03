class Vehicle:
    def __init__(self, cost, vehicle_type):
        self.cost = cost
        self.type = vehicle_type
        self.premium = None

    def calculate_premium(self):
        if self.type == 1:
            self.premium = 0.02 * self.cost
        elif self.type == 2:
            self.premium = 0.06 * self.cost
        elif self.type == 3:
            self.premium = 0.08 * self.cost

    def get_premium(self):
        return self.premium


# MAIN PROGRAM
vehicle_cost = float(input("Enter vehicle cost: "))
vehicle_type = int(input("Enter vehicle type (1, 2, or 3): "))

vehicle_obj = Vehicle(vehicle_cost, vehicle_type)
vehicle_obj.calculate_premium()

print("The premium amount is:", vehicle_obj.get_premium())

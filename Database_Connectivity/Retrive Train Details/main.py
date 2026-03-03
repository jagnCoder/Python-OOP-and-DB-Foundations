from train_management_system import TrainManagementSystem

def main():
    db_config = {
        'user': 'root',
        'password': 'jaganMysql@123',
        'host': 'localhost',
        'database': 'accenturepydb'
    }
    
    tms = TrainManagementSystem(db_config)

    source = input("Enter the source: ").strip()
    destination = input("Enter the destination: ").strip()
    coach_type = input("Enter the coach type (AC1, AC2, AC3, Sleeper, Seater): ").strip().upper()

    valid_coach_types = {"AC1", "AC2", "AC3", "SLEEPER", "SEATER"}
    
    if coach_type not in valid_coach_types:
        print("Invalid Coach Type")
    else:
        trains = tms.retrieve_train_details(coach_type, source, destination)
        if trains:
            for train in trains:
                print(train.get_train_number(), train.get_train_name())
        else:
            print("No trains found")
    
    tms.close()

if __name__ == "__main__":
    main()

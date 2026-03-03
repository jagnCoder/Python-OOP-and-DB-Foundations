def validate(func):
    """Decorator to validate participants.jmf:12:jmf@mail"""
    def inner(participants_list):
        valid_participants = []
        for participant in participants_list:
            name, age, email = participant
            # Check if the email contains '@' and '.'
            if '@' in email and '.' in email:
                valid_participants.append(participant)
            else: print("~~~INVALID EMAIL ID by~~~",name)
        
        # Call the segregate function with valid participants
        return func(valid_participants)
    
    return inner

@validate
def segregate(participants_list):
    under_10 = 0
    under_15 = 0
    under_20 = 0

    for participant in participants_list:
        name, age, email = participant
        age = int(age)  # Convert age to an integer

        if 5 <= age < 10:
            under_10 += 1
        elif 10 <= age < 15:
            under_15 += 1
        elif 15 <= age < 20:
            under_20 += 1

    return under_10, under_15, under_20

def main():
    participants_list = []

    while True:
        # Input candidate details
        candidate_details = input("Enter candidate details as 'name:age:email': ")
        participant = candidate_details.split(':')
        participants_list.append(participant)

        # Ask user if they want to continue
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont != 'y':
            break

    # Call segregate function which is decorated by validate
    under_10, under_15, under_20 = segregate(participants_list)

    # Display results
    print("No. of participants under 10:", under_10)
    print("No. of participants under 15:", under_15)
    print("No. of participants under 20:", under_20)

# Run the main function
if __name__ == "__main__":
    main()

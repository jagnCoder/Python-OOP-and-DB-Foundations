class Train:
    def __init__(self, train_number, train_name, source, destination, ac1, ac2, ac3, sleeper, seater):
        self.__train_number = train_number
        self.__train_name = train_name
        self.__source = source
        self.__destination = destination
        self.__ac1 = ac1
        self.__ac2 = ac2
        self.__ac3 = ac3
        self.__sleeper = sleeper
        self.__seater = seater

    # Getter methods
    def get_train_number(self):
        return self.__train_number

    def get_train_name(self):
        return self.__train_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination
    
    def has_coach(self, coach_type):
        if coach_type == "AC1":
            return self.__ac1 > 0
        elif coach_type == "AC2":
            return self.__ac2 > 0
        elif coach_type == "AC3":
            return self.__ac3 > 0
        elif coach_type == "Sleeper":
            return self.__sleeper > 0
        elif coach_type == "Seater":
            return self.__seater > 0
        return False

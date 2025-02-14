
class Carriage:


    def __init__(self, new_identifier, number_of_seats):
        """Initializes the current object."""
        self.__id = new_identifier
        self.__max_number_of_seats = number_of_seats
        self.__seats = []
        self.reset_seats()

    def reserve(self, free_seat_number):
        """Precondition: is_free(free_seat_number) 
                         and is_legal(free_seat_number) """
        self.__seats[free_seat_number] = 1


    def make_free(self, reserved_seat_number):
        """Precondition: not is_free(reserved_seat_number) 
                         and is_legal(reserved_seat_number) """
        self.__seats[reserved_seat_number] = 0


    def count_reserved(self):
        """Precondition: True """
        i = 1
        result = 0
        while (i < len(self.__seats)):
            if (self.__seats[i] != 0):
                result = result + 1
            i = i + 1
        return result


    def is_free(self, free_seat_number):
        """Precondition: True
                         and is_legal(free_seat_number)"""
        return self.__seats[free_seat_number] == 0

    def is_legal(self, seat_number):
        """Precondition: True """
        return 1 <= seat_number <= self.__max_number_of_seats   

    def max_seats(self):
        """Precondition: True """
        return self.__max_number_of_seats

    def is_full(self):
        """Precondition: True """
        return self.count_reserved() >= self.max_seats()

    def reset_seats(self):
        self.__seats = []
        i = 0
        while (i <= self.__max_number_of_seats):
            self.__seats.append(0)
            i = i + 1


    def reserved_seats_as_list(self):
        result = []
        i = 1
        while (i < len(self.__seats)):
            if (not self.is_free(i)):
                result.append(i)
            i = i + 1
        return result


    def __str__(self):
        result = ""
        result = result + self.__id + ": "
        result = result + str(self.__seats[1:len(self.__seats)])
        return result

class Train:
    def __init__(self, train_id, departure, destination, carriages):
        """
        Initializes a Train with a unique identifier, departure and destination locations, 
        and at least one Carriage.

        :param train_id: Unique identifier for the train
        :param departure: Departure location
        :param destination: Destination location
        :param carriages: A list containing at least one Carriage object

        Preconditions:
        - train_id must be a string.
        - departure and destination must be strings.
        - carriages must be a non-empty list containing only Carriage objects.
        """
        if not isinstance(train_id, str) or not isinstance(departure, str) or not isinstance(destination, str):
            raise ValueError("Train ID, departure, and destination must be strings.")

        if not isinstance(carriages, list) or len(carriages) == 0 or not all(isinstance(c, Carriage) for c in carriages):
            raise ValueError("Train must have at least one valid Carriage in a list.")

        self.__train_id = train_id
        self.__departure = departure
        self.__destination = destination
        self.__carriages = carriages  # List of Carriage objects, order is important

    def add_carriage(self, carriage):
        """
        Adds a Carriage to the train while maintaining order.

        :param carriage: A Carriage object to be added.
        
        Preconditions:
        - carriage must be an instance of Carriage.
        """
        if not isinstance(carriage, Carriage):
            raise ValueError("Only a Carriage object can be added.")

        self.__carriages.append(carriage)

    def remove_carriage(self, carriage_id):
        """
        Removes a Carriage from the train by its unique identifier.

        :param carriage_id: The identifier of the Carriage to be removed.
        
        Preconditions:
        - carriage_id must be a string.
        """
        if not isinstance(carriage_id, str):
            raise ValueError("Carriage ID must be a string.")

        self.__carriages = [c for c in self.__carriages if c._Carriage__id != carriage_id]

        if len(self.__carriages) == 0:
            raise ValueError("A train must have at least one carriage. Removal failed.")

    def reserve_seat(self):
        """
        Reserves a seat from the first available Carriage in the train.
        If all carriages are full, it returns a message.

        :return: Message indicating the reserved seat and carriage, or that no seats are available.
        """
        for carriage in self.__carriages:
            for seat_num in range(1, carriage.max_seats() + 1):
                if carriage.is_free(seat_num):
                    carriage.reserve(seat_num)
                    return f"Seat {seat_num} reserved in Carriage {carriage._Carriage__id}."
        return "No available seats in the train."

    def show_seat_map(self):
        """
        Displays a text-based visualization of reserved and free seats in the train.
        """
        print(f"\nSeat Map for Train {self.__train_id} ({self.__departure} -> {self.__destination}):")
        for carriage in self.__carriages:
            print(carriage)

    def get_train_info(self):
        """
        Returns all information about the train, including ID, locations, and carriages.

        :return: A formatted string with train details.
        """
        return (f"Train {self.__train_id} from {self.__departure} to {self.__destination}.\n"
                f"Carriages: {[c._Carriage__id for c in self.__carriages]}")

    def __str__(self):
        """
        Returns a string representation of the train.
        """
        return self.get_train_info()
      


def test_train():
    # Create carriages
    c1 = Carriage("Carr01", 10)
    c2 = Carriage("Carr02", 15)

    # Initialize the Train with two Carriages
    train = Train("Train001", "Helsinki", "Tampere", [c1, c2])

    # Display Train Info
    print(train)

    # Add a new Carriage
    c3 = Carriage("Carr03", 20)
    train.add_carriage(c3)
    print("\nAfter adding a carriage:")
    print(train)

    # Reserve seats
    print("\nReserving seats...")
    print(train.reserve_seat())  # Should reserve a seat in the first available Carriage
    print(train.reserve_seat())

    # Show seat map
    train.show_seat_map()

    # Remove a Carriage
    print("\nRemoving Carriage 'Carr02'...")
    train.remove_carriage("Carr02")
    print(train)
    
    # Show updated seat map
    train.show_seat_map()

test_train()


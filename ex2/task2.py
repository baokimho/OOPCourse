class TrainCarriage:
    def __init__(self, identifier: str, total_seats: int):
        self.identifier = identifier
        self.total_seats = total_seats
        self.reserved_seats = set()
    
    def add_reservation(self, seat_number: int) -> bool:
        """Adds a reservation if the seat is available."""
        if seat_number < 1 or seat_number > self.total_seats:
            raise ValueError("Invalid seat number.")
        
        if seat_number in self.reserved_seats:
            return False  # Seat already reserved
        
        self.reserved_seats.add(seat_number)
        return True
    
    def remove_reservation(self, seat_number: int) -> bool:
        """Removes a reservation if the seat is currently reserved."""
        if seat_number in self.reserved_seats:
            self.reserved_seats.remove(seat_number)
            return True
        return False  # Seat was not reserved
    
    def reset_reservations(self):
        """Resets all reservations."""
        self.reserved_seats.clear()
    
    def is_full(self) -> bool:
        """Returns True if all seats are reserved, False otherwise."""
        return len(self.reserved_seats) == self.total_seats
    
    def get_reservation_report(self) -> str:
        """Returns a report of reserved and unreserve seats."""
        reserved_list = sorted(self.reserved_seats)
        unreserved_list = [seat for seat in range(1, self.total_seats + 1) if seat not in self.reserved_seats]
        
        return (f"Train Carriage {self.identifier} Reservation Status:\n"
                f"Total Seats: {self.total_seats}\n"
                f"Reserved Seats: {reserved_list}\n"
                f"Unreserved Seats: {unreserved_list}\n"
                f"Full: {'Yes' if self.is_full() else 'No'}")

carriage = TrainCarriage("A1", 10)
carriage.add_reservation(3)
carriage.add_reservation(5)
carriage.add_reservation(7)
print(carriage.get_reservation_report())

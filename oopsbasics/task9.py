# create a flight class with seat booking functionality 

class Flight:

    def __init__(self, flight_name):
        self.flight_name = flight_name
        self.seat_booked = False

    def book_seat(self):
        if self.seat_booked == False:
            self.seat_booked = True
            print("Seat booked successfully")
        else:
            print("Seat is already booked")


flight1 = Flight("Air India")

print("Flight:", flight1.flight_name)
flight1.book_seat()
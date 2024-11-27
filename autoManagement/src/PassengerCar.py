from src.Auto import Auto


class PassengerCar(Auto):
    def __init__(self, number_plate, type, rental_price, number_of_doors):
        super().__init__(number_plate, type, rental_price)
        self.number_of_doors = number_of_doors

    def __str__(self):
        return f"Passenger car: \nNumber plate: {self.number_plate}\nType: {self.type}\nRental price: {self.rental_price}\nNumber of doors: {self.number_of_doors}"
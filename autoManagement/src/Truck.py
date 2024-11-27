from src.Auto import Auto


class Truck(Auto):
    def __init__(self, number_plate, type, rental_price, payload_capacity):
        super().__init__(number_plate, type, rental_price)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return f"Truck: \nNumber plate: {self.number_plate}\nType: {self.type}\nRental price: {self.rental_price}\nPayload capacity: {self.payload_capacity}"
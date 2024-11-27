from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, number_plate, type, rental_price):
        self.number_plate = number_plate
        self.type = type
        self.rental_price = rental_price

    @abstractmethod
    def __str__(self):
        pass
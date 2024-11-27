from datetime import date

class Rent:
    def __init__(self, auto, date):
        self.auto = auto
        self.date = date

    def __str__(self):
        return f"Rent - Auto: {self.auto.number_plate}, Date: {self.date}"
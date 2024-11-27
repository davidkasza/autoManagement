from src.Rent import Rent

class AutoManagement:
    def __init__(self, name):
        self.name = name
        self.autos = []
        self.rents = []

    def add_auto(self, auto):
        self.autos.append(auto)

    def list_autos(self):
        return [str(auto) for auto in self.autos]

    def rent_auto(self, number_plate, date):
        for rent in self.rents:
            if rent.auto.number_plate == number_plate and rent.date == date:
                return f"The car with plate number {number_plate} is already rented on {date}"

        auto_to_rent = next((auto for auto in self.autos if auto.number_plate == number_plate), None)
        if auto_to_rent:
            new_rent = Rent(auto_to_rent, date)
            self.rents.append(new_rent)
            return f"Car with plate number {number_plate} successfully rented on {date}.\n\n"
        return f"Car with plate number {number_plate} not found."

    def cancel_rent_auto(self, number_plate, date):
        for rent in self.rents:
            if rent.auto.number_plate == number_plate and rent.date == date:
                self.rents.remove(rent)
                return "Rent cancelled successfully!"
        return "Rent not found!"

    def list_rents(self):
        return [str(rent) for rent in self.rents]

    def list_available_autos(self, date):
        rented_autos = {rent.auto.number_plate for rent in self.rents if rent.date == date}
        available_autos = [auto for auto in self.autos if auto.number_plate not in rented_autos]

        return available_autos
from src.AutoManagement import AutoManagement
from src.PassengerCar import PassengerCar
from src.Truck import Truck

from datetime import date, datetime


def initialize_autos(auto_management : AutoManagement):
    autos = [
        PassengerCar("ADS-123", "Toyota", 10000, 4),
        PassengerCar("ASD-123", "Audi", 10000, 4),
        PassengerCar("DAS-123", "Audi", 10000, 4),
        Truck("DSA-123", "Mercedes Benz", 25000, 500),
        Truck("SAD-123", "Volvo", 25000, 500),
        Truck("SDA-123", "Volvo", 25000, 500)
    ]

    for auto in autos:
        auto_management.add_auto(auto)

    rentals = [
        ("ADS-123", date(2024, 11, 20)),
        ("ASD-123", date(2024, 11, 20)),
        ("DSA-123", date(2024, 11, 20)),
        ("SAD-123", date(2024, 11, 20))
    ]

    for number_plate, rent_date in rentals:
        auto_management.rent_auto(number_plate, rent_date)

def get_date_input():
    date_input = input("Enter date: (YYYY-MM-DD): ")
    try:
        entered_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        if entered_date < date.today():
            print("The date cannot be in the past. Please enter a valid date!")
            return None
        return entered_date
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")
        return None

def get_available_autos(auto_management, date):
    available_autos = auto_management.list_available_autos(date)
    if not available_autos:
        print("No autos available for the selected date")
        return False

    else:
        print("\n\nAvailable autos:")
        for auto in available_autos:
            print(f"{auto.number_plate}: {auto.type} - {auto.rental_price} Ft")
        return True

def main():
    auto_management = AutoManagement("Best Autos Kft.")

    initialize_autos(auto_management)

    while True:
        print("\n1. Rent auto\n2. Cancel rent\n3. List rents\nPress 'q' to quit")
        answer = input("Choice: ")

        if answer == "1":
            chosen_date = get_date_input()
            if chosen_date:
                available_autos = get_available_autos(auto_management, chosen_date)
                if available_autos:
                    number_plate = input("Enter the plate number to rent: ")
                    print(auto_management.rent_auto(number_plate, chosen_date))

        elif answer == "2":
            number_plate = input("Number plate: ")
            chosen_date = get_date_input()
            if chosen_date:
                print(auto_management.cancel_rent_auto(number_plate, chosen_date))

        elif answer == "3":
            for rent in auto_management.list_rents():
                print(rent)

        elif answer == "q":
            break

        else:
            print("Invalid input")
            continue

if __name__ == "__main__":
    main()
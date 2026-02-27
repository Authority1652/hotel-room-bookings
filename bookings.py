# this is a program for booking a room in a hotel
import json
from datetime import datetime

# room services and their charges
room_types = {
    "standard": 35,
    "deluxe": 50,
    "suite": 75 
}

# extra services and their charges

extras_prices = {
    "breakfast": 10,
    "massage": 15,
    "airport_pickup": 30
}

# store all bookings
bookings = []

# function to claculate ( number of nights)
def cal_no_night(check_in, check_out):
    date_format = "%Y-%m-%d"
    start = datetime.strptime(check_in, date_format)
    end = datetime.strptime(check_out, date_format)
    return (end - start).days

# function to calculate the cost
# def cal_total_cost(room_type, extras, nights):
#     base_price = room_types[room_type] * nights
#     extras_price = sum(extras_prices[extra] * nights for extra in extras)
#     return base_price + extras_price
def cal_total_cost(room_type, extras, nights):
    base_price = room_types[room_type] * nights
    print(f"Calculating cost: extras = {extras}, nights = {nights}")
    extras_price = sum(extras_prices[extra] * nights for extra in extras)
    return base_price + extras_price

# function to check availability(basic- always available)
def is_available_room(room_type, check_in, check_out):
    return True

# function to show available rooms
def show_available_rooms():
    print("*" * 20)
    print("Available Room Types:")
    print("📍" * 20)
    for room, price in room_types.items():
        print(f"- {room}: ${price}/night")

# main function for booking the rooms
def book_room():
    print("Welcome To Authority's Hotel Room Booking Service")
    name = input("Enter Your Full Name: ")
    show_available_rooms()
    room_type = input("Choose a room type: ")
    if room_type not in room_types:
        print("The room type you selected is invalid")
        return
    
    check_in = input("Enter check in date (YYYY-MM-DD): ")
    check_out = input("Enter check out date (YYYY-MM-DD): ")

    if not is_available_room(room_type, check_in, check_out):
        print("There's no available room for those dates.")
        return
    
    # choose extras
    extras = []
    for extra in extras_prices:
        response = input(f"would you want {extra}? (yes/no): ").lower()
        if response == "yes":
            extras.append(extra)
    
    nights = cal_no_night(check_in, check_out)
    total_cost = cal_total_cost(room_type, extras, nights)

    print("📍" * 20)
    print(f"Booking Summary:")
    print(f"Name: {name}")
    print(f"Room Type: {room_type}")
    print(f"Check-in: {check_in}")
    print(f"Check-out: {check_out}")
    print(f"Nights: {nights}")
    print(f"Extras: {', '.join(extras) if extras else 'None'}")
    print(f"Total Cost: ${total_cost}")
    print("📍" * 20)

    confirm = input("Do you want to confirm this bookings (yes/no)?: ").lower()
    if confirm == "yes":
        booking = {
            "name": name,
            "room_type": room_type,
            "check_in": check_in,
            "check_out": check_out,
            "extras": extras,
            "total_cost": total_cost
        }
        bookings.append(booking)
        save_bookings()
        print("Bookings confirmed and saved")
    else:
        print("Bookings cancelled")

# save_bookings to a file
def save_bookings():
    with open("Hotel_bookings.json", "w") as p:
        json.dump(bookings, p, indent=4)

# load existing bookings (if file exist)
def load_bookings():
    try:
        with open("Hotel_bookings.json", "r") as p:
            return json.load(p)
    except FileNotFoundError:
        return []
    
# run the program
if __name__ == "__main__":
    bookings = load_bookings()

    while True:
        book_room()
        again = input("Do you want to make another booking (yes/no)?: ").lower()
        if again != "yes":
            print("Thank You For Using Authority's Hotel Service")
            print("📍" * 20)
            break
                  
print("The Authority.")




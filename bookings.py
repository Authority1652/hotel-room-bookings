# # this is a program for booking a room in a hotel
# import json
# from datetime import datetime

# # room services and their charges
# room_types = {
#     "standard": 35,
#     "deluxe": 50,
#     "suite": 75 
# }

# # extra services and their charges

# extras_prices = {
#     "breakfast": 10,
#     "massage": 15,
#     "airport_pickup": 30
# }

# # store all bookings
# bookings = []

# # function to claculate ( number of nights)
# def cal_no_night(check_in, check_out):
#     date_format = "%Y-%m-%d"
#     start = datetime.strptime(check_in, date_format)
#     end = datetime.strptime(check_out, date_format)
#     return (end - start).days

# # function to calculate the cost
# # def cal_total_cost(room_type, extras, nights):
# #     base_price = room_types[room_type] * nights
# #     extras_price = sum(extras_prices[extra] * nights for extra in extras)
# #     return base_price + extras_price
# def cal_total_cost(room_type, extras, nights):
#     base_price = room_types[room_type] * nights
#     print(f"Calculating cost: extras = {extras}, nights = {nights}")
#     extras_price = sum(extras_prices[extra] * nights for extra in extras)
#     return base_price + extras_price

# # function to check availability(basic- always available)
# def is_available_room(room_type, check_in, check_out):
#     return True

# # function to show available rooms
# def show_available_rooms():
#     print("*" * 20)
#     print("Available Room Types:")
#     print("📍" * 20)
#     for room, price in room_types.items():
#         print(f"- {room}: ${price}/night")

# # main function for booking the rooms
# def book_room():
#     print("Welcome To Authority's Hotel Room Booking Service")
#     name = input("Enter Your Full Name: ")
#     show_available_rooms()
#     room_type = input("Choose a room type: ")
#     if room_type not in room_types:
#         print("The room type you selected is invalid")
#         return
    
#     check_in = input("Enter check in date (YYYY-MM-DD): ")
#     check_out = input("Enter check out date (YYYY-MM-DD): ")

#     if not is_available_room(room_type, check_in, check_out):
#         print("There's no available room for those dates.")
#         return
    
#     # choose extras
#     extras = []
#     for extra in extras_prices:
#         response = input(f"would you want {extra}? (yes/no): ").lower()
#         if response == "yes":
#             extras.append(extra)
    
#     nights = cal_no_night(check_in, check_out)
#     total_cost = cal_total_cost(room_type, extras, nights)

#     print("📍" * 20)
#     print(f"Booking Summary:")
#     print(f"Name: {name}")
#     print(f"Room Type: {room_type}")
#     print(f"Check-in: {check_in}")
#     print(f"Check-out: {check_out}")
#     print(f"Nights: {nights}")
#     print(f"Extras: {', '.join(extras) if extras else 'None'}")
#     print(f"Total Cost: ${total_cost}")
#     print("📍" * 20)

#     confirm = input("Do you want to confirm this bookings (yes/no)?: ").lower()
#     if confirm == "yes":
#         booking = {
#             "name": name,
#             "room_type": room_type,
#             "check_in": check_in,
#             "check_out": check_out,
#             "extras": extras,
#             "total_cost": total_cost
#         }
#         bookings.append(booking)
#         save_bookings()
#         print("Bookings confirmed and saved")
#     else:
#         print("Bookings cancelled")

# # save_bookings to a file
# def save_bookings():
#     with open("Hotel_bookings.json", "w") as p:
#         json.dump(bookings, p, indent=4)

# # load existing bookings (if file exist)
# def load_bookings():
#     try:
#         with open("Hotel_bookings.json", "r") as p:
#             return json.load(p)
#     except FileNotFoundError:
#         return []
    
# # run the program
# if __name__ == "__main__":
#     bookings = load_bookings()

#     while True:
#         book_room()
#         again = input("Do you want to make another booking (yes/no)?: ").lower()
#         if again != "yes":
#             print("Thank You For Using Authority's Hotel Service")
#             print("📍" * 20)
#             break
                  
# print("The Authority.")

import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

# ---------------- DATA ---------------- #

room_types = {
    "Standard": 35,
    "Deluxe": 50,
    "Suite": 75
}

extras_prices = {
    "Breakfast": 10,
    "Massage": 15,
    "Airport Pickup": 30
}

# ---------------- FUNCTIONS ---------------- #

def cal_no_night(check_in, check_out):
    date_format = "%Y-%m-%d"
    start = datetime.strptime(check_in, date_format)
    end = datetime.strptime(check_out, date_format)
    return (end - start).days


def cal_total_cost(room_type, extras, nights):
    base_price = room_types[room_type] * nights
    extras_price = sum(extras_prices[extra] * nights for extra in extras)
    return base_price + extras_price


def save_bookings():
    with open("Hotel_bookings.json", "w") as file:
        json.dump(bookings, file, indent=4)


def load_bookings():
    try:
        with open("Hotel_bookings.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def book_room():
    name = name_entry.get().strip()
    room_type = room_var.get()
    check_in = checkin_entry.get()
    check_out = checkout_entry.get()

    if not name:
        messagebox.showerror("Error", "Please enter your full name.")
        return

    try:
        nights = cal_no_night(check_in, check_out)
        if nights <= 0:
            messagebox.showerror("Error", "Check-out must be after check-in.")
            return
    except:
        messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    selected_extras = [extra for extra, var in extras_vars.items() if var.get() == 1]

    total_cost = cal_total_cost(room_type, selected_extras, nights)

    booking = {
        "name": name,
        "room_type": room_type,
        "check_in": check_in,
        "check_out": check_out,
        "extras": selected_extras,
        "total_cost": total_cost
    }

    bookings.append(booking)
    save_bookings()

    summary_text.set(
        f"Booking Confirmed!\n\n"
        f"Name: {name}\n"
        f"Room: {room_type}\n"
        f"Nights: {nights}\n"
        f"Extras: {', '.join(selected_extras) if selected_extras else 'None'}\n"
        f"Total Cost: ${total_cost}"
    )

    messagebox.showinfo("Success", "Booking saved successfully!")


# ---------------- UI DESIGN ---------------- #

bookings = load_bookings()

root = tk.Tk()
root.title("Authority Hotel Booking System")
root.geometry("600x600")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="🏨 Authority Hotel Booking",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=15)

main_frame = tk.Frame(root, bg="#2a2a40", padx=20, pady=20)
main_frame.pack(pady=10)

# Name
tk.Label(main_frame, text="Full Name:", bg="#2a2a40", fg="white").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(main_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Room Type
tk.Label(main_frame, text="Room Type:", bg="#2a2a40", fg="white").grid(row=1, column=0, sticky="w")
room_var = tk.StringVar(value="Standard")
room_menu = ttk.Combobox(main_frame, textvariable=room_var, values=list(room_types.keys()), state="readonly")
room_menu.grid(row=1, column=1, pady=5)

# Check-in
tk.Label(main_frame, text="Check-in (YYYY-MM-DD):", bg="#2a2a40", fg="white").grid(row=2, column=0, sticky="w")
checkin_entry = tk.Entry(main_frame)
checkin_entry.grid(row=2, column=1, pady=5)

# Check-out
tk.Label(main_frame, text="Check-out (YYYY-MM-DD):", bg="#2a2a40", fg="white").grid(row=3, column=0, sticky="w")
checkout_entry = tk.Entry(main_frame)
checkout_entry.grid(row=3, column=1, pady=5)

# Extras
tk.Label(main_frame, text="Extras:", bg="#2a2a40", fg="white").grid(row=4, column=0, sticky="w")

extras_vars = {}
row_num = 5
for extra in extras_prices:
    var = tk.IntVar()
    chk = tk.Checkbutton(
        main_frame,
        text=f"{extra} (${extras_prices[extra]}/night)",
        variable=var,
        bg="#2a2a40",
        fg="white",
        selectcolor="#444"
    )
    chk.grid(row=row_num, column=0, columnspan=2, sticky="w")
    extras_vars[extra] = var
    row_num += 1

# Book Button
book_button = tk.Button(
    root,
    text="Confirm Booking",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=book_room
)
book_button.pack(pady=15)

# Summary Display
summary_text = tk.StringVar()
summary_label = tk.Label(
    root,
    textvariable=summary_text,
    bg="#1e1e2f",
    fg="white",
    font=("Helvetica", 12),
    justify="left"
)
summary_label.pack(pady=10)

root.mainloop()
import os

# Global variables definition
bookings = []

def clear_console():
    #Clears the console according to the operating system.
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    #Displays the restaurant's main menu.
    print("--- Welcome to the Restaurant ---")
    print("1. Request table")
    print("2. Make a reservation")
    print("3. View bookings")
    print("4. Exit")

def request_table():
    #Handles the logic for requesting a table without a reservation, where the meal will be on the same day.
    clear_console()
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    num_people = int(input("For how many people will the table be?: "))
    table_number = len(bookings) + 1
    bookings.append({
        "name": name,
        "age": age,
        "num_people": num_people,
        "date": None,
        "start_time": None,
        "end_time": None,
        "table_number": table_number
    })
    print(f"Table requested for {name}. Assigned table number: {table_number}")

def make_reservation():
    #Handles the logic for making a reservation with detailed information.
    clear_console()
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    date = input("Enter the reservation date (DD-MM-YYYY): ")

    start_time = input("Enter the start time of the reservation (HH:MM AM/PM): ")
    duration_hours = int(input("How many hours will you stay? (Enter only the number): "))
    end_time = calculate_end_time(start_time, duration_hours)

    # Check if the time slot is available
    for booking in bookings:
        if booking["date"] == date:
            if (start_time >= booking["start_time"] and start_time < booking["end_time"]) or \
               (end_time > booking["start_time"] and end_time <= booking["end_time"]):
                print("Sorry, that time slot is already booked. Please try another time.")
                return

    num_people = int(input("How many people will attend?: "))
    contact = input("Enter your contact number: ")
    identification = input("Enter your identification: ")

    table_number = len(bookings) + 1
    bookings.append({
        "name": name,
        "age": age,
        "gender": gender,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "num_people": num_people,
        "contact": contact,
        "identification": identification,
        "table_number": table_number
    })
    print(f"Reservation made for {name}. Registered date: {date}, Time: {start_time} to {end_time}. Assigned table number: {table_number}")

def calculate_end_time(start_time, duration_hours):
    #Calculates the end time based on the start time and duration in hours.
    from datetime import datetime, timedelta
    start_datetime = datetime.strptime(start_time, "%I:%M %p")
    end_datetime = start_datetime + timedelta(hours=duration_hours)
    return end_datetime.strftime("%I:%M %p")

def view_bookings():
    #Displays all bookings made using the make_reservation function.
    clear_console()
    if not any(booking["date"] for booking in bookings):
        print("No bookings made.")
    else:
        print("\n--- Bookings Made ---")
        for booking in bookings:
            if booking["date"] is not None:
                print(f"Name: {booking['name']}, Age: {booking['age']}, Gender: {booking['gender']}, Date: {booking['date']}, Time: {booking['start_time']} to {booking['end_time']}, Table: {booking['table_number']}, People: {booking['num_people']}, Contact: {booking['contact']}, ID: {booking['identification']}")

def main():
    #Main function to run the restaurant's booking system.
    clear_console()
    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            request_table()
        elif option == "2":
            make_reservation()
        elif option == "3":
            view_bookings()
        elif option == "4":
            print("Thank you for visiting us! Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        input("\nPress Enter to continue...")
        clear_console()

if __name__ == "__main__":
    main()
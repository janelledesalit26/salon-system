from booking_functions import (
    add_booking,
    check_schedule_conflict,
    cancel_booking,
)
from sales_functions import log_service, apply_discount
from price_management import (
    SERVICE_CATALOG,
    get_service_price,
    display_price_list,
)
from staff_management import assign_staff
from search_functions import search_bookings, search_transactions


bookings = []
transactions = []
price_list = SERVICE_CATALOG.copy()
staff_list = ["Cecil De Jose", "Adela Rubio", "Cyrene Lorenzo", "Gie Taytayon", "Michelle Borres","Ronna Andrada","Ghie Bacas"]


def select_service():
    """Display services and let the user select one by number."""
    while True:
        services = list(price_list.items())

        if not services:
            print("No services available.")
            return None

        print("\n--- AVAILABLE SALON SERVICES ---")
        for number, (name, price) in enumerate(services, start=1):
            print(f"{number}. {name} - PHP {price:.2f}")

        print("0. Cancel")

        try:
            choice = int(input("Choose a service number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            return None

        if 1 <= choice <= len(services):
            name, price = services[choice - 1]
            print(f"Selected: {name} - PHP {price:.2f}")
            return name

        print("Invalid choice. Please select from the list.")


def main_menu():
    while True:
        print("\n" + "=" * 45)
        print("MODISH NAILS and HAIR SALON")
        print("=" * 45)
        print("1. BOOKINGS")
        print("2. SALES & DAILY SUMMARY")
        print("3. PRICE LIST")
        print("4. STAFFS LIST")
        print("5. SEARCH RECORDS")
        print("6. EXIT")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            booking_menu()
        elif choice == "2":
            sales_menu()
        elif choice == "3":
            price_menu()
        elif choice == "4":
            staff_menu()
        elif choice == "5":
            search_menu()
        elif choice == "6":
            print("Thank you for using Modish Salon System!")
            break
        else:
            print("Invalid choice. Please try again.")


def booking_menu():
    while True:
        print("\n--- CLIENT BOOKING ---")
        print("1. Add New Booking")
        print("2. Check Schedule Conflict")
        print("3. Cancel Booking")
        print("4. View All Bookings")
        print("5. Back to Main Menu")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            print("\n--- ADD NEW BOOKING ---")
            client_name = input("Client name: ").strip()
            contact = input("Contact number: ").strip()

            if not client_name:
                print("Client name is required.")
                continue

            service = select_service()
            if service is None:
                print("Booking cancelled; no service selected.")
                continue

            date = input("Date (YYYY-MM-DD): ").strip()
            time = input("Time (HH:MM): ").strip()

            booking = {
                "client": client_name,
                "contact": contact,
                "service": service,
                "date": date,
                "time": time,
            }

            if check_schedule_conflict(bookings, date, time):
                print("That time slot is already booked.")
                print("Please choose another date or time.")
            else:
                add_booking(bookings, booking)
                print("Booking added successfully!")
                print(f"Client: {client_name}")
                print(f"Service: {service}")
                print(f"Date: {date} at {time}")
                print(
                    "Listed service price: PHP "
                    f"{get_service_price(price_list, service):.2f}"
                )

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ").strip()
            time = input("Enter time (HH:MM): ").strip()

            if check_schedule_conflict(bookings, date, time):
                print("Conflict found. This time slot is unavailable.")
            else:
                print("Time slot is available.")

        elif choice == "3":
            client_name = input("Client name to cancel: ").strip()
            cancel_booking(bookings, client_name)

        elif choice == "4":
            if not bookings:
                print("No bookings yet.")
            else:
                print("\n--- ALL BOOKINGS ---")
                for number, booking in enumerate(bookings, start=1):
                    print(
                        f"{number}. {booking['client']} - "
                        f"{booking['service']} on "
                        f"{booking['date']} at {booking['time']}"
                    )

        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def sales_menu():
    while True:
        print("\n--- SALES & DAILY SUMMARY ---")
        print("1. Log New Service/Transaction")
        print("2. Apply Discount")
        print("3. View Daily Sales")
        print("4. Back to Main Menu")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            print("\n--- NEW SALES TRANSACTION ---")
            client_name = input("Client name: ").strip()

            if not client_name:
                print("Client name is required.")
                continue

            selected_services = []

            while True:
                service = select_service()
                if service is None:
                    break

                selected_services.append(service)
                more = input(
                    "Would you like to add another service? (yes/no): "
                ).strip().lower()

                if more != "yes":
                    break

            if not selected_services:
                print("No services selected. Transaction cancelled.")
                continue

            subtotal = sum(
                get_service_price(price_list, name)
                for name in selected_services
            )

            is_senior = (
                input("Senior citizen? (yes/no): ").strip().lower()
                == "yes"
            )

            if is_senior:
                total = apply_discount(subtotal, 0.10)
            else:
                total = subtotal

            staff = assign_staff(staff_list)

            transaction = {
                "client": client_name,
                "services": ", ".join(selected_services),
                "subtotal": subtotal,
                "total": total,
                "staff": staff,
                "senior": is_senior,
            }

            log_service(transactions, transaction)

            print("\n--- TRANSACTION SUMMARY ---")
            print(f"Client: {client_name}")
            print(f"Services: {', '.join(selected_services)}")
            print(f"Subtotal: PHP {subtotal:.2f}")

            if is_senior:
                print(
                    f"Senior discount (10%): "
                    f"PHP {subtotal * 0.10:.2f}"
                )

            print(f"Total: PHP {total:.2f}")
            print(f"Assigned staff: {staff}")
            print("Transaction saved successfully!")

        elif choice == "2":
            try:
                subtotal = float(input("Enter subtotal: PHP "))
                discount_pct = float(input("Enter discount percentage: "))

                if subtotal < 0 or not 0 <= discount_pct <= 100:
                    print("Enter a non-negative subtotal and a discount from 0 to 100.")
                    continue

                total = apply_discount(subtotal, discount_pct / 100)
                print(f"Total after discount: PHP {total:.2f}")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            if not transactions:
                print("No sales recorded yet.")
            else:
                print("\n--- SALES SUMMARY ---")
                total_sales = 0

                for number, transaction in enumerate(transactions, start=1):
                    print(
                        f"{number}. {transaction['client']} - "
                        f"PHP {transaction['total']:.2f} "
                        f"(Staff: {transaction['staff']})"
                    )
                    total_sales += transaction["total"]

                print(f"TOTAL SALES: PHP {total_sales:.2f}")

        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def price_menu():
    while True:
        print("\n--- PRICE LIST ---")
        print("1. View Price List")
        print("2. Add Service")
        print("3. Update Price")
        print("4. Back to Main Menu")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            display_price_list(price_list)

        elif choice == "2":
            service_name = input("New service name: ").strip()

            if not service_name:
                print("Service name is required.")
                continue

            if service_name in price_list:
                print("That service already exists.")
                continue

            try:
                price = float(input("Price in PHP: "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue

                price_list[service_name] = price
                print("Service added successfully.")

            except ValueError:
                print("Please enter a valid price.")

        elif choice == "3":
            service_name = input("Service name to update: ").strip()

            if service_name not in price_list:
                print("Service not found. Use the exact service name.")
                continue

            try:
                new_price = float(input("New price in PHP: "))
                if new_price < 0:
                    print("Price cannot be negative.")
                    continue

                price_list[service_name] = new_price
                print("Price updated successfully.")

            except ValueError:
                print("Please enter a valid price.")

        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def staff_menu():
    while True:
        print("\n--- STAFF LIST ---")
        print("1. View Staff")
        print("2. Add Staff Member")
        print("3. Remove Staff Member")
        print("4. Back to Main Menu")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            if staff_list:
                for number, staff in enumerate(staff_list, start=1):
                    print(f"{number}. {staff}")
            else:
                print("No staff members listed.")

        elif choice == "2":
            name = input("Staff name to add: ").strip()

            if name and name not in staff_list:
                staff_list.append(name)
                print(f"{name} added successfully.")
            else:
                print("Name is empty or staff member already exists.")

        elif choice == "3":
            name = input("Staff name to remove: ").strip()

            if name in staff_list:
                staff_list.remove(name)
                print(f"{name} removed successfully.")
            else:
                print("Staff member not found.")

        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def search_menu():
    while True:
        print("\n--- SEARCH RECORDS ---")
        print("1. Search Bookings by Client Name")
        print("2. Search Bookings by Date")
        print("3. Search Transactions by Client")
        print("4. Back to Main Menu")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            name = input("Client name to search: ").strip()
            results = search_bookings(bookings, "client", name)

            if results:
                for booking in results:
                    print(
                        f"{booking['client']} - {booking['service']} "
                        f"on {booking['date']} at {booking['time']}"
                    )
            else:
                print("No bookings found.")

        elif choice == "2":
            date = input("Date to search (YYYY-MM-DD): ").strip()
            results = search_bookings(bookings, "date", date)

            if results:
                for booking in results:
                    print(
                        f"{booking['client']} - {booking['service']} "
                        f"at {booking['time']}"
                    )
            else:
                print("No bookings found for that date.")

        elif choice == "3":
            name = input("Client name to search: ").strip()
            results = search_transactions(transactions, "client", name)

            if results:
                for transaction in results:
                    print(
                        f"{transaction['client']} - "
                        f"PHP {transaction['total']:.2f} - "
                        f"{transaction['services']}"
                    )
            else:
                print("No transactions found.")

        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()


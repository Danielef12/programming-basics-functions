def show_menu():
    """Function to display menu"""
    print("--- Simple Time Display ---")
    print("1. Display time with additional date information")
    print("2. Time zone conversion")
    print("3. Set a countdown")
    print("4. World clock collection")
    print("5. Exit")


def choose_menu():
    """function to select in menu"""
    choice = input("Select an option: ").strip()
    return choice


def elaborate_choice(choice):
    """function to elaborate choice"""
    while choice in ["1", "2", "3", "4", "5"]:
        if choice == "1":
            from current_time import show_date_time

            show_date_time()
        elif choice == "2":
            from timezone_conversion import show_timezone_converted

            show_timezone_converted()
        elif choice == "3":
            from countdown_display import start_timer

            start_timer()
        elif choice == "4":
            from world_clock import world_clock

            world_clock()
        elif choice == "5":
            print("Thank you for using this program!")
            exit()
    else:
        print("Invalid selection.")


def main():
    """Main function"""
    while True:
        show_menu()
        choice = choose_menu()
        elaborate_choice(choice)

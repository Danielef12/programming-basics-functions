""" With this tool you can display the date and time in different formats, display the same time in different time zones and create a timer """

from datetime import datetime
from zoneinfo import ZoneInfo
import time
import threading

def currentTime():
    now = datetime.now()
    date_time = now.strftime('%d/%b/%Y - %H:%M:%S')

    # Day off the week
    day_of_week = now.strftime('%A')

    # Day of year
    day_of_year = now.strftime('%j')

    # Week number
    week_number = now.strftime('%W')

    print("--- DATA AND TIME INFORMATION ---")
    print(f"\nDate and time: {date_time}")
    print(f"Day of the week: {day_of_week}")
    print(f"Day of the year: {day_of_year}")
    print(f"Week number: {week_number}")


    

def time_zone():
    time_zones = input("Insert the time zone in format (Zone/Country): ")
    try:

        fuse = datetime.now(ZoneInfo(time_zones))
        print(fuse.strftime('%d/%b/%Y - %H:%M:%S'))
    except Exception as e:
        print(f"Error: {e}")


def timer():
    t = input("enter time in seconds: ")
    try:
        t = int(t)
    except ValueError:
        print("Invalid input. Please enter a number")
        return

    # Control Events of threading
    pause = threading.Event()
    stop = threading.Event()
    reset = threading.Event()

    timer_data = {'time': t, 'format': 1}

    
    print("Choose format time:")
    print("1. Complete (DD:HH:MM:SS)")
    print("2. Hour:Minute:Seconds")
    print("3. Minute:Seconds")
    print("4. Seconds")

    try:
        select = int(input("Format select: "))
        if select not in [1, 2, 3, 4]:
            print("Invalid selection")
            select = 1
    except ValueError:
        print("Invalid input")
        select = 1

    timer_data["format"] = select

    def countdown():
        while not stop.is_set():
            current_time = timer_data['time']

            if current_time < 0:
                print("\nTime's up!")
                break

            if pause.is_set():
                time.sleep(0.1)
                continue

            if reset.is_set():
                reset.clear()
                continue

            mins, secs = divmod(current_time, 60)
            hours, mins = divmod(mins, 60)
            days, hours = divmod(hours, 24)

            if timer_data['format'] == 1:
                timer_display = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs)
            elif timer_data['format'] == 2:
                total_hours = days * 24 + hours
                timer_display = '{:02d}:{:02d}:{:02d}'.format(total_hours, mins, secs)
            elif timer_data['format'] == 3:
                total_mins = (days * 24 * 60) + (hours * 60) + mins
                timer_display = '{:02d}:{:02d}'.format(total_mins, secs)
            elif timer_data['format'] == 4:
                total_secs = current_time
                timer_display = '{:03d}'.format(total_secs)

            print(f"\r{timer_display}    ", end='', flush=True)
            time.sleep(1)
            timer_data['time'] -= 1

    timer_thread = threading.Thread(target=countdown)
    timer_thread.daemon = True
    timer_thread.start()

    try:
        while True:
            print("\nCommand: pause, start, reset, stop")
            command = input(">>> ").strip().lower()
            if command == "pause":
                pause.set()
                print("Timer paused")
            elif command == "start" or command == "resume":
                pause.clear()
                print("Timer resumed")
            elif command == "reset":
                timer()
            elif command == "stop":
                stop.set()
                print("Timer stopped")
                break
            else:
                print("Invalid command")
    except KeyboardInterrupt:
        stop.set()
        print("\nTimer interrupted")
    timer_thread.join(timeout=2)
    print("Timer finished")


def world_clock():
    clocks = [] # List of saved Time zone

    timezones_list = {
        '1': ('Europe/Rome', 'Rome, Italy'),
        '2': ('Europe/London', 'London, United Kingdom'),
        '3': ('America/New_York', 'New York, USA'),
        '4': ('America/Los_Angeles', 'Los Angeles, USA'),
        '5': ('Asia/Tokyo', 'Tokyo, Japan'),
        '6': ('Asia/Shanghai', 'Shanghai, Cina'),
        '7': ('Australia/Sydney', 'Sydney, Australia'),
        '8': ('Europe/Paris', 'Parigi, France'),
        '9': ('Asia/Dubai', 'Dubai, UAE'),
        '10': ('America/Sao_Paulo', 'San Paolo, Brazil')
    }

    def display_clocks():
        if not clocks:
            print("No clocks are append")
            return
        
        print("\n--- WORLD CLOCKS ---")

        current_time = datetime.now()

        for i, (timezone, city_name) in enumerate(clocks, 1):
            
                tz_time = current_time.astimezone(ZoneInfo(timezone))
                time_str = tz_time.strftime('%H:%M:%S')
                date_str = tz_time.strftime('%d/%m/%Y')
                day_str = tz_time.strftime('%A')

                local_time = current_time.astimezone()
                time_diff = (tz_time.utcoffset() - local_time.utcoffset()).total_seconds() / 3600
                diff_str = f"(UTC{time_diff:+.0f})" if time_diff != 0 else "(UTC)"

                print(f"{i:2d}. {city_name:<25} | {time_str} | {day_str:<5} | {date_str} | {diff_str}")
            
        
        print("\n")
    
    def add_timezone():
        print("\nADD NEW TIMEZONE")
        print("Choose from the list of available timezone\n")

        for key, (tz,name) in timezones_list.items():
            print(f"{key:2s}. {name}")

        selection = input("\nChoose (1-10): ").strip()
        if selection in timezones_list:
            timezone, city_name = timezones_list[selection]
            clocks.append((timezone, city_name))
        else:
            print("Invalid Selection.")
    
    def remove_timezone():
        if not clocks:
            print("No clocks to remove")
            return

        display_clocks()
        try:
            index = int(input(f"\nClock to remove? (1-{len(clocks)}): ")) -1
            if 0 <= index < len(clocks):
                removed = clocks.pop(index)
                print(f"Removed: {removed[1]}")
            else:
                print("Invalid Select")
        except ValueError:
            print("Insert a valid number")
    
    while True:
        print("\nWORLD CLOCKS")
        print("1. Show all clocks")
        print("2. Add new clock")
        print("3. Remove clock")
        print("4. Back to main menù")

        choice = input("\nWhat do you do? ").strip()

        if choice == '1':
            display_clocks()
        elif choice =="2":
            add_timezone()
        elif choice == "3":
            remove_timezone()
        elif choice == "4":
            break
        else:
            print("Invalid Selection.")

        
def main():
    
    while True:
        print("\n==== Simple Time Display ====")
        print("1. For time visualization")
        print("2. For visualize the time in other time zone")
        print("3. For set a countdown timer")
        print("4. For show world clock")
        print("0. For exit.")
        select = int(input("Select mode: "))
        if select == 1:
            currentTime()
        elif select == 2:
            time_zone()
        elif select == 3:
            timer()
        elif select == 4:
            world_clock()
        elif select == 0:
            print("Thank's for using. See you soon")
            break


if __name__ == "__main__":
    main()
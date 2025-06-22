from datetime import datetime
from zoneinfo import ZoneInfo


def timezone_list():
    """Function that returns a list of all timezone names."""
    return {
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


def display_available_timezones():
    print('Available timezones:')
    for key, (tz, label) in timezone_list().items():
        print(f'{key}: {label}')


def select_timezone():
    timezones = timezone_list()
    selection = input(f"Which timezone would you like to select (1: {len(timezones)})? ").strip()
    if selection in timezones:
        return timezones[selection]

    else:
        print("That's not a valid timezone!")
        return None


def add_clock(clocks):
    """Function that adds a clock to the clocks list."""
    timezone = select_timezone()
    if timezone and timezone not in clocks:
        clocks.append(timezone)
        print(f'Added {timezone[1]}')
    elif timezone:
        print(f'Timezone {timezone[1]} already exists')
    return clocks


def get_clock_to_remove(clocks):
    """Function that returns the timezone name to remove."""
    while True:
        try:
            index = int(input(f"Which timezone would you like to remove (1: {len(clocks)})? "))
            if 0 <= index < len(clocks):
                return index
            else:
                print("That's not a valid timezone!")
        except ValueError:
            print("That's not a valid timezone!")


def remove_clock(clocks):
    """Function that removes a clock from the clocks list."""
    if not clocks:
        print("No clocks to remove")
        return

    print("--- REMOVE CLOCK ---")
    display_world_clocks(clocks)

    index = get_clock_to_remove(clocks)
    removed = clocks.pop(index-1)
    print(f'Removed {removed[1]}')




def display_world_clocks(clocks):
    """Function that displays the clocks list."""
    print("\n--- WORLD CLOCK ---")
    for tz_str, label in clocks:
        now = datetime.now(ZoneInfo(tz_str))
        print(f'{label:25s}: {now.strftime("%Y-%m-%d %H:%M:%S")}')
    print("============")

def world_clock():
    """Function that displays the world clock."""
    clocks = []
    while True:
        print("\nMenu:")
        print("1. Show timezone clocks")
        print("2. Add timezone clocks")
        print("3. Remove timezone clocks")
        print("4. Exit")
        choiche = input("Select an option: ").strip()
        if choiche == '1':
            if clocks:
                display_world_clocks(clocks)
            else:
                print("No clocks added yet")

        elif choiche == '2':
            display_available_timezones()
            add_clock(clocks)

        elif choiche == '3':
            remove_clock(clocks)

        elif choiche == '4':
            print("Quitting")
            break
        else:
            print("That's not a valid option!")


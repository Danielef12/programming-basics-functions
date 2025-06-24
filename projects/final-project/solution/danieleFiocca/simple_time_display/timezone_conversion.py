from datetime import datetime
from zoneinfo import ZoneInfo


def get_timezones_available():
    """Function for retrieving available timezones."""
    return {
        "1": ("Europe/Rome", "Rome, Italy"),
        "2": ("Europe/London", "London, United Kingdom"),
        "3": ("America/New_York", "New York, USA"),
        "4": ("America/Los_Angeles", "Los Angeles, USA"),
        "5": ("Asia/Tokyo", "Tokyo, Japan"),
        "6": ("Asia/Shanghai", "Shanghai, China"),
        "7": ("Australia/Sydney", "Sydney, Australia"),
        "8": ("Europe/Paris", "Paris, France"),
        "9": ("Asia/Dubai", "Dubai, UAE"),
        "10": ("America/Sao_Paulo", "São Paulo, Brazil"),
    }


def show_timezones():
    """function to display available timezones."""
    time_zones = get_timezones_available()
    for timezone, (tz, names) in time_zones.items():
        print(f"{timezone:2s}: {names}")


def get_timezone_selection():
    """Function for to select available timezones."""
    timezones = get_timezones_available()
    while True:
        selection = input(
            f"\nChoose a timezone to convert (1:{len(timezones)}): "
        ).strip()
        if selection in timezones:
            return timezones[selection]
        else:
            print("Invalid selection")


def show_timezone_converted():
    """Function that displays the timezone selected by user"""
    print("\n--- Time Zone Conversion ---")
    print("\nSelect a time zone to see the current time in that part of the world")
    print("\nAvailable timezones:")
    show_timezones()
    time_zone = get_timezone_selection()
    display_time = datetime.now(ZoneInfo(time_zone[0]))
    print(f"\nCurrent time in {time_zone[1]}: {display_time.strftime('%H:%M:%S')}")

import threading
import time


def set_timer():
    """Setting the timer in seconds"""
    while (timer := int(input("Enter time in seconds: "))) <= 0:
        print("Invalid time. Time must be greater than 0.")
    return timer


def get_format_input():
    """Setting the format for display countdown"""
    print("\nChoose time format:")
    print("1. Complete (DD:HH:MM:SS)")
    print("2. Hour:Minute:Seconds")
    print("3. Minute:Seconds")
    print("4. Seconds")

    while True:
        format_select = int(input("\nEnter a time format: "))
        if format_select in [1, 2, 3, 4]:
            return format_select
        else:
            print("Selection must be 1 to 4.")


def format_display_timer(seconds, format_selected):
    """Formatting the display countdown"""
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    if format_selected == 1:
        return "{:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds)
    if format_selected == 2:
        total_hours = days * 24 + hours
        return "{:02d}:{:02d}:{:02d}".format(total_hours, minutes, seconds)
    if format_selected == 3:
        total_minutes = (days * 24 * 60) + (hours * 60) + minutes
        return "{:02d}:{:02d}".format(total_minutes, seconds)
    if format_selected == 4:
        return "{:04d}".format(seconds)


def countdown_logic(
    initial_seconds, format_selected, pause_event, stop_event, reset_event
):
    """Countdown logic"""
    seconds = initial_seconds
    while seconds >= 0:
        if stop_event.is_set():

            return

        if reset_event.is_set():
            seconds = initial_seconds
            reset_event.clear()
            print(f"\nReset to: {format_display_timer(seconds, format_selected)}")

        if not pause_event.is_set():
            print(
                f"\r{format_display_timer(seconds, format_selected)} ",
                end="",
                flush=True,
            )
            time.sleep(1)
            seconds -= 1
        else:
            time.sleep(0.1)  # While paused
    if not stop_event.is_set():
        print("\nTimer finished.")


def handle_commands(pause, stop, reset):
    """Logic for threading commands"""
    print("Command available: start, pause, stop, reset")

    while not stop.is_set():
        command = input("\n>>>").strip().lower()
        match command:
            case "start":
                pause.clear()
                print("time started")
            case "pause":
                pause.set()
                print("time paused")
            case "reset":
                reset.set()
                print("time reset")
            case "stop":
                stop.set()
                print("time stopped")

            case _:
                print("Invalid command")
        """if command == "start":
            pause.clear()
            print("Timer started")
        elif command == "pause":
            pause.set()
            print("Timer paused")
        elif command == "reset":
            reset.set()
            print("Timer reset")
        elif command == "stop":
            stop.set()
            print("Timer stopped")
            break
        else:
            print("Command not available")"""


def start_timer():
    """Function to start the timer"""
    seconds = set_timer()
    format_selected = get_format_input()

    pause = threading.Event()
    stop = threading.Event()
    reset = threading.Event()

    timer_thread = threading.Thread(
        target=countdown_logic, args=(seconds, format_selected, pause, stop, reset)
    )
    timer_thread.start()

    handle_commands(pause, stop, reset)

    timer_thread.join()
    print("\nTimer finished.")

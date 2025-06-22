from datetime import datetime


def current_date_time():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


def day_of_the_week():
    return datetime.now().strftime('%A')


def day_of_the_year():
    return datetime.now().strftime('%j')


def week_number():
    return datetime.now().strftime('%W')


def show_date_time():
    print("--- DATA AND TIME INFORMATION ---")
    print(f"\nDate and time: {current_date_time()}")
    print(f"Day of the week: {day_of_the_week()}")
    print(f"Day of the year: {day_of_the_year()}")
    print(f"Week number: {week_number()}\n")

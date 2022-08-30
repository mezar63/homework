from exchanger.utils.consts import CURRENCIES
from typing import List
from datetime import datetime


def choice_of_command():
    return print(f"Choice of COMMAND: 1.'COURSE USD'; 2. 'COURSE UAH'; 3. 'EXCHANGE USD'; 4. 'EXCHANGE UAH'; 5. 'STOP'")


def greetings():
    return print(f"Exchange launched!")


def date_and_time():
    return print(datetime.today().strftime('%d/%m/%Y %H:%M'))


def is_valid_command(command_list: List, limit: int = 1) -> bool:
    if len(command_list) <= limit:
        print(f"INVALID COMMAND")
        return False
    return True


def is_valid_currency(currency: str) -> bool:
    if currency not in list(CURRENCIES.values()):
        print(f"INVALID CURRENCY {currency}")
        return False
    return True


def is_valid_course(course: float) -> bool:
    if course == 0.0:
        print("API ERROR")
        return False
    return True


def is_float(params: str) -> bool:
    try:
        float(params)
        return True
    except ValueError:
        print("CURRENCY VALUE ERROR")
        return False
from exchanger.utils import helpers
from exchanger.objects.exchanger import Exchanger
#from exchanger.utils.helpers import date_and_time, greetings


class UserStory:
    def __init__(self):
        self.exchanger = Exchanger()

    def start(self):
        helpers.greetings()
        while True:
            helpers.choice_of_command()
            command_list = input("COMMAND?\n").strip().upper().split(" ")
            command = command_list[0]

            match command:
                case 'COURSE':
                    if not helpers.is_valid_command(command_list):
                        continue

                    currency = command_list[1]
                    if not helpers.is_valid_currency(currency):
                        continue

                    course = self.exchanger.get_current_course(currency)
                    if not helpers.is_valid_course(course):
                        continue

                    limit = self.exchanger.get_current_limit(currency)
                    helpers.date_and_time()
                    print(f"RATE {course}, AVAILABLE {limit}")

                case 'EXCHANGE':
                    if not helpers.is_valid_command(command_list, limit=2):
                        continue

                    currency = command_list[1]
                    if not helpers.is_valid_currency(currency):
                        continue

                    currency_value = command_list[2]
                    if not helpers.is_float(currency_value):
                        continue

                    helpers.date_and_time()
                    self.exchanger.exchange(currency, float(currency_value))

                case 'STOP':
                    print("SERVICE STOPPED")
                    break

                case _:
                    print("INVALID COMMAND")
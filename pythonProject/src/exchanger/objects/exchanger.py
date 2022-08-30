from typing import Dict, Tuple
from exchanger.objects.course_api import CourseAPI
from exchanger.objects.file_controller import FileController
from exchanger.utils.consts import FILE_DATA, CURRENCIES


class Exchanger:
    def __init__(self):
        self.file_controller = FileController()
        self.file_controller.write_file(FILE_DATA)
        self.course_api = CourseAPI()

    def __get_file_data(self) -> Dict:
        return self.file_controller.read_file()

    @staticmethod
    def __create_actual_state(file_data: Dict, config: Dict) -> Dict:
        file_data[config["currency"]] += config["currency_value"]
        file_data[config["current_currency"]] -= config["current_money"]
        return file_data

    @staticmethod
    def __is_we_have_money(file_data: Dict, money: float, current_currency: str) -> Tuple[bool, float]:
        money_we_have = file_data[current_currency]
        return money_we_have >= money, money_we_have

    def __currency_calculation_to_change(self, currency: str, currency_value: float, current_course: float) -> \
            Tuple[float, str]:
        if self.course_api.base_currency == currency:
            return current_course * currency_value, CURRENCIES["to"]
        return currency_value / current_course, self.course_api.base_currency

    def get_current_limit(self, currency: str = "USD") -> float:
        return self.__get_file_data()[currency]

    def get_current_course(self, currency: str, api_type: str = "show"):
        return self.course_api.get_course(currency, api_type)

    def exchange(self, currency: str = "USD", currency_value: float = 0.0):
        file_data = self.__get_file_data()
        current_course = self.get_current_course(currency, "exchange")
        current_money, current_currency = self.__currency_calculation_to_change(
            currency, currency_value, current_course
        )

        is_we_have, money_we_have = self.__is_we_have_money(file_data, current_money, current_currency)
        if is_we_have:
            exchange_config = {
                "currency": currency,
                "currency_value": currency_value,
                "current_currency": current_currency,
                "current_money": current_money
            }
            actual_config = self.__create_actual_state(file_data, exchange_config)
            self.file_controller.write_file(actual_config)
            print(f"{current_currency} {current_money}, RATE {current_course}")
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE {current_currency} {current_money}, AVAILABLE {money_we_have} ")
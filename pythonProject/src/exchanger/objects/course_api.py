from typing import Dict, Union
import requests


class CourseAPI:
    def __init__(self, base_currency: str = "USD"):
        self.url = "https://api.privatbank.ua/p24api/pubinfo"
        self.base_currency = base_currency

    def __send_request(self) -> Dict:
        response = requests.get(self.url, params={
            'json': '', 'exchange': '', 'coursid': 5
        })
        if response.status_code == 200:
            return response.json()
        return {}

    def __get_base_currency_course(self, response: Dict) -> Union[Dict, None]:
        for item in response:
            if item["ccy"] == self.base_currency:
                return {"buy": float(item["buy"]), "sale": float(item["sale"])}
            return None

    def get_course(self, currency: str = "USD", reason: str = "Show") -> float:
        response = self.__send_request()
        if bool(response):
            price = self.__get_base_currency_course(response)
            if price is not None:
                if reason == "show":
                    return price["sale"] \
                        if currency == self.base_currency else price["buy"]
                else:
                    return price["buy"] \
                        if currency == self.base_currency else price["sale"]
        return 0.0
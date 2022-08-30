from pizzastore.objects.pizza import Pizza
from pizzastore.objects.receipt import Receipt
import csv
import os


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PizzaStore(metaclass=SingletonMeta):

    def __init__(self):
        file_path = os.getcwd() + "\\constants\\pizzeria_menu.csv"
        self.pizzas = self.get_pizzas_from_file(file_path)
        self.receipts = []

    @staticmethod
    def get_pizzas_from_file(filename):
        pizza_list = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                pizza_list.append(Pizza(row['idx'], row['name'], int(row['price']), row['description']))
        return pizza_list

    def filter_1(self, x):
        return list(filter(lambda item: item.price <= x, self.pizzas))

    def new_receipt(self):
        r = Receipt()
        return r

    def print_menu(self):
        for item in self.pizzas:
            print(item)

    def print_pizzas(self, print_menu):
        for item in print_menu:
            print(item)

    def print_revers_price(self):
        for item in sorted(self.pizzas, key=lambda item: item.price, reverse=True):
            price_reverse = f'Pizza: {item.idx:2}. {item.name:<15} {item.price:>.2f} uah.: {item.description:<20}'
            print(price_reverse)

import random
from datetime import datetime
from pizzastore.objects.receiptline import ReceiptLine


class Receipt:
    n_receipt = 1

    def __init__(self):
        self.datetime = datetime.today().strftime('%d/%m/%Y %H:%M')
        self.lines = []
        self.number = Receipt.n_receipt
        Receipt.n_receipt += 1

    def random_check_list(self, pizzas):
        random_number = random.randrange(3, 7)
        order_list = random.sample(pizzas, random_number)
        for item in order_list:
            self.lines.append(ReceiptLine(item, random.randrange(1, 5)))

    def __str__(self):
        return f'Receipt:{self.number}\n{self.datetime}\nPosition:\n' + '\n'.join([str(line) for line in self.lines])

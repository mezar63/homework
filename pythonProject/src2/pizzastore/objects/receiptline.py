from pizzastore.objects.pizza import Pizza


class ReceiptLine:

    def __init__(self, pizza: Pizza, num: int):
        self.pizza = pizza
        self.num = num

    def __str__(self):
        return f'Pizza {self.pizza.name:<15} {self.pizza.price:>.2f} uah. {self.num} - {self.pizza.price*self.num} uah.'

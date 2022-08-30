class Pizza:

    def __init__(self, idx, name, price, description):
        self.idx = idx
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'Pizza: {self.idx:2}. {self.name:<15} {self.price:>.2f} uah.: {self.description:<20}'

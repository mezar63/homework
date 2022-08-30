from pizzastore.objects.pizza_store import PizzaStore
from pizzastore.objects.helpers import greetings


def main(pizzastore):
    while True:
        greetings()
        choice = input()
        match choice:
            case '0':
                break
            case '1':
                pizzastore.print_menu()
            case '2':
                r = pizzastore.new_receipt()
                r.random_check_list(pizzastore.pizzas)
                pizzastore.receipts.append(r)
                print(r)
            case '3':
                filtered = pizzastore.filter_1(140)
                pizzastore.print_pizzas(filtered)
            case '4':
                pizzastore.print_revers_price()
            case _:
                print(f'{"Wrong choice"}')


if __name__ == '__main__':
    pizzastore = PizzaStore()
    main(pizzastore)

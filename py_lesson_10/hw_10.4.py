class PizzaError(Exception):
    pass


class ToMuchCheese(PizzaError):
    pass


class Pizza:
    list = ['test', 'simple']

    def __init__(self) -> None:
        pass

    def add_pizza(self, pizza):
        if pizza not in self.list:
            self.list.append(pizza)
            print(pizza, 'successfully added!')
        else:
            print(pizza, 'already exist!')
        print('Pizza list:', self.list)

    def remove_pizza(self, pizza):
        if pizza in self.list:
            self.list.remove(pizza)
            print(pizza, 'successfully removed!')
        else:
            print(pizza, 'no exist in pizza list!')
        print('Pizza list:', self.list)


class Order(Pizza):
    def __init__(self) -> None:
        super().__init__()
        self.orders = {}
        self.counter = 0
        self.message = None

    def make_pizza(self, pizza, cheese):
        if pizza not in Pizza.list:
            raise PizzaError()

        if cheese > 110:
            raise ToMuchCheese()

        self.__pizza = pizza
        self.__cheese = cheese
        self.counter += 0

        if self.__pizza not in self.orders.keys():
            self.orders[self.__pizza] = 1
        else:
            self.orders[self.__pizza] += 1

        print('Pizza ' + self.__pizza + ' successfully created!')
        print('Orders', self.orders)

    def create_orders_file(self):
        self.__fs = open('pizza_orders.txt', 'w+')
        for key in self.orders.keys():
            self.__fs.write('Pizza -> ' + key + ' : ' +
                            str(self.orders[key]) + '\n')
        self.__fs.close()
        print('File with orders successfully saved!')


pizzeria = Order()
pizzeria.add_pizza('test1')
pizzeria.remove_pizza('tes')
pizzeria.make_pizza('test', 100)
pizzeria.make_pizza('test', 100)
pizzeria.make_pizza('test', 100)
pizzeria.make_pizza('simple', 100)
pizzeria.make_pizza('test1', 20)
try:
    pizzeria.create_orders_file()
except:
    print('Sorry, but there some file operation error')

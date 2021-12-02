class Pizza:
    def __init__(self):
        self.__pizza_list = ['simple', 'american']

    def make(self, pizzaName, cheese):
        if pizzaName not in self.__pizza_list:
            raise PizzaError('No such pizza was find!')
        elif cheese > 110:
            raise TooManyCheesePizzaError('Too many cheese bro, stop it!')
        else:
            print('Here is your pizza')


class PizzaError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class TooManyCheesePizzaError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


pizza_object = Pizza()

for (pizza, cheese) in [('simple', 100), ('e', 100), ('simple', 115)]:
    try:
        pizza_object.make(pizza, cheese)
    except PizzaError:
        print('Pizza error')
    except TooManyCheesePizzaError:
        print('Cheese error')
    except:
        print('What happened?')

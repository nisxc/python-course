# class TheSimpleClass:
#     pass


# obj = TheSimpleClass()

# stack example procedure way

# stack = []


# def push(val):
#     stack.append(val)


# def pop():
#     tmp = stack[-1]
#     del stack[-1]
#     return tmp


# push(3)

# print(pop())

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        tmp = self.__stack_list[-1]
        del self.__stack_list[-1]
        return tmp


class AdditionalStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        self.sum = 'f'

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        tmp = Stack.pop(self)
        self.__sum -= 1
        return tmp


stack_obj = AdditionalStack()
# print(stack_obj.__dict__)
stack_obj.push(1)
# if hasattr(stack_obj, '_AdditionalStack__sum'):
#     print('e')
# for name in stack_obj.__dict__.keys():
#     print(name)
#     if name == 'sum':
#         val = getattr(stack_obj, name)
#         if isinstance(val, str):
#             print(val)
# print(Stack.__base__)
# print(Stack.__dict__)
# print(stack_obj.__dict__)
# print(stack_obj.pop())
# print(stack_obj.get_sum())

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        tmp = self.__stack_list[-1]
        del self.__stack_list[-1]
        return tmp


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__poped_list = []

    def get_counter(self):
        return len(self.__poped_list)

    def pop(self):
        tmp = Stack.pop(self)
        self.__poped_list.append(tmp)
        return tmp


obj = CountingStack()

for i in range(100):
    obj.push(i)
    obj.pop()
print(obj.get_counter())

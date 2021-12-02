# class SampleClass:
#     def __init__(self, val):
#         self.val = val


# obj1 = SampleClass(1)
# obj2 = SampleClass(2)
# obj3 = obj2
# obj3.val += 1

# print(obj1 is obj2)
# print(obj2 is obj3)

# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return 'My name is ' + self.name + '.'


# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)


# object = Sub('Andy')

# print(object)

# class Super:
#     def __init__(self):
#         self.supVar = 11


# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12


# object = Sub()
# print(object.supVar)
# print(object.subVar)


# class Level1:
#     value_1 = 10

#     def __init__(self) -> None:
#         self.val_1 = 11

#     def func_1(self):
#         return 12


# class Level2(Level1):
#     value_2 = 20

#     def __init__(self) -> None:
#         self.val_2 = 21
#         super().__init__()

#     def func_2(self):
#         return 22


# class Level3(Level2):
#     value_3 = 30

#     def __init__(self) -> None:
#         self.val_3 = 31
#         super().__init__()

#     def func_3(self):
#         return 32


# obj = Level3()

# print(obj.value_1, obj.val_1, obj.func_1())
# print(obj.value_2, obj.val_2, obj.func_2())
# print(obj.value_3, obj.val_3, obj.func_3())

# class SupA:
#     def __init__(self) -> None:
#         self.a = 'a'

#     def __str__(self) -> str:
#         return 'Hello A'


# class SupB:
#     def __init__(self) -> None:
#         self.b = 'b'

#     def __str__(self) -> str:
#         return 'Hello B'


# class Sub(SupA, SupB):
#     def __init__(self) -> None:
#         self.b = 'b'


# object = Sub()

# print(object)


# class A:
#     val_2 = 0


# class B(A):
#     val_2 = 0


# class C(B, A):
#     pass


# obj = C()
# print(obj.val_2)

class O:
    val_2 = 0


class A:
    val_2 = 0


class B(A):
    val_2 = 0


class C(A):
    pass


class D(B, C):
    pass


# obj = C()
# obj1 = O()
# print(issubclass(D, A))
# print(isinstance(obj1, O))
# print(obj is obj1)

def print_exception_tree(excClass, nest=0):
    print(excClass.__name__)
    if nest > 1:
        print(' |' * (nest - 1), end='')
    if nest > 0:
        print(' +----', end='')
    for sub in excClass.__subclasses__():
        print_exception_tree(sub, nest+1)


print_exception_tree(BaseException)

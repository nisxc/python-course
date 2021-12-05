# class Fib:
#     def __init__(self, n):
#         self.__i = 0
#         self.__n = n
#         self.__p1 = self.__p2 = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.__i += 1
#         if self.__i > self.__n:
#             raise StopIteration
#         if self.__i in [1, 2]:
#             return 1
#         result = self.__p1 + self.__p2
#         self.__p1, self.__p2 = self.__p2, result
#         return result


# class Gen:
#     def __init__(self, n) -> None:
#         self.__iter = Fib(n)

#     def __iter__(self):
#         return self.__iter


# for i in Gen(10):
#     print(i)

# def gen(n):
#     for i in range(n):
#         yield i


# for i in gen(5):
#     print(i)


# def pow_of_two(n):
#     pow = 1
#     for i in range(n):
#         yield pow
#         pow *= 2


# print([x for x in pow_of_two(5)])
# print(list(pow_of_two(5)))

# for i in range(20):
#     if i not in pow_of_two(5):
#         print(i)

# def fib(n):
#     n1 = n2 = 1
#     for i in range(n):
#         if i in [0, 1]:
#             yield 1
#         else:
#             n = n1 + n2
#             n1, n2 = n2, n
#             yield n


# print(list(fib(5)))

# list_1 = []
# for ex in range(10):
#     list_1.append(10 ** ex)

# list_2 = [10 ** ex for ex in range(10)]

# print(list_1)
# print(list_2)

# the_list = []
# for x in range(10):
#     the_list.append(1 if x % 2 == 0 else 0)

# print(the_list)

# print([1 if x % 2 == 0 else 0 for x in range(5)])

# lam = lambda x: x + 1

# print(lam(1))


# def print_func(args, func):
#     for i in args:
#         print('f(', i, ')=', func(i), sep='')


# def poly(x):
#     return 2 * x ** 2 - 4 * x + 2


# print_func([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)

# list_1 = [x for x in range(5)]
# print(list(map(lambda y: y * 3, list_1)))

# list_1 = [x for x in range(5)]
# print(list(filter(lambda y: y > 3, list_1)))

# def outer(par):
#     loc = par

#     def inner():
#         return loc
#     return inner


# result = outer(5)
# print(result())
# print(result())
# result = outer(2)
# print(result())

# def make_closure(x):
#     tmp = x

#     def inner(y):
#         return y ** tmp
#     return inner


# mc = make_closure(1)
# mc1 = make_closure(2)

# call = mc(3)
# call1 = mc1(2)

# print(call)
# print(call1)

# from os import strerror

# import errno
# try:
#     stream = open("test.txt", 'w+')
#     stream.close()
# except IOError as Ex:
#     print('Can\'t open file', strerror(Ex.errno), errno.EACCES)

# try:
#     rc = cc = 0
#     stream = open('test.txt', 'r')
#     # cr = stream.read()
#     # row = stream.readline()
#     # row = stream.readlines(1)
#     # while len(row):
#     #     rc += 1
#     #     for cr in row[0]:
#     #         cc += 1
#     #     row = stream.readlines(1)
#     # while row:
#     #     rc += 1
#     # for cr in row:
#     #     cc += 1
#     # row = stream.readline()
#     # print(row)
#     # count = 0
#     # for c in cr:
#     #     count += 1
#     #     print(c, end='')
#     stream.close()
#     print(row)
#     print(rc)
#     print(cc)
# except:
#     print('F')


# try:
#     row_count = cr_count = 0
#     for row in open('test.txt', 'rt'):
#         row_count += 1
#         for cr in row:
#             cr_count += 1
#     print(row_count)
#     print(cr_count)
# except:
#     print('Sorry')

# try:
#     s = open('t1et.txt', 'wt')
#     for i in range(5):
#         s.write('Line -> ' + str(i) + '\n')
#     s.close()
# except:
#     print('F')


# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 - i

# # for j in data:
# #     print(hex(j))

# try:
#     s = open('bytes.txt', 'wb')
#     s.write(data)
#     s.close()
# except:
#     print('Holly')

# try:
#     b = open('bytes.txt', 'rb')
#     data = bytearray(b.read())
#     b.close()

#     for i in data:
#         print(hex(i))
# except:
#     print('Holly')

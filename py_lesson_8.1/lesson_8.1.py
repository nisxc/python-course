# try:
#     print('ap'[1/0])
# except ZeroDivisionError:
#     print('zero')
# except IndexError:
#     print('index')
# except:
#     print('some')

# try:
#     y = 1 / 0
# except ArithmeticError:
#     print('arith')
# except ZeroDivisionError:
#     print('zero')
# except:
#     print('some')

# def zero_exc_raise():
#     try:
#         return 1 / 0
#     except:
#         print('zero')
# return 1 / 0


# zero_exc_raise()

# try:
#     zero_exc_raise()
# except:
#     print('zero')

# def bad_def():
#     raise KeyError


# try:
#     bad_def()
# except KeyError:
#     print('Da key yare yare daze')
# except:
#     print('aaaaæ')


# def bad_def():
#     assert 1 < 0


# try:
#     bad_def()
# except AssertionError:
#     print('f')
# except KeyError:
#     print('Da key yare yare daze')
# except:
#     print('aaaaæ')

# from time import sleep

# seconds = 0

# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print('Heeeell noo')

# no memory || overflow example - sorry

# try:
#     import math
#     import aaaaa
# except:
#     print('SOrry')

import json
# import socket

# server_addr = input('What server do you want to connect to? ')
# try:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect((server_addr, 80))
#     sock.send(b"GET / HTTP/1.1\r\nHost: " + bytes(server_addr,
#                                                   "utf8") + b"\r\nConnection: close\r\n\r\n")
#     reply = sock.recv(10000)
#     sock.shutdown(socket.SHUT_RDWR)
#     sock.close()
#     print(repr(reply))
# except socket.gaierror:
#     print('Sorry, there some problems with address that you entered!')


# num = 1.231213213e10-10
# str = 'Hello json from python'
# lt = [False, True, 20, 'fh']
# print(json.dumps(lt))

# class Who:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age


# class MyEncoder(json.JSONEncoder):
#     def default(self, w):
#         if isinstance(w, Who):
#             return w.__dict__
#         else:
#             return super().default(w)


# def encode_who(w):
#     if isinstance(w, Who):
#         return w.__dict__
#     else:
#         raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


# some_man = Who('John Doe', 42)

# print(json.dumps(some_man, cls=MyEncoder))

# json_num = '123123123'
# result = json.load(json_num)

class Who:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(w)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)
print(type(new_man))
print(new_man.__dict__)

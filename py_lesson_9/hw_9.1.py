class QueueError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return 'There are no elements exist'


class Queue:
    def __init__(self) -> None:
        self.__initial_list = []

    def __str__(self) -> str:
        return 'There are left: ' + str(self.__initial_list)

    def put(self, element):
        self.__initial_list.insert(0, element)

    def get(self):
        if not len(self.__initial_list):
            raise QueueError()
        tmp = self.__initial_list[-1]
        self.__initial_list.pop()
        return tmp


fifo = Queue()

try:
    # fifo.put(1)
    # fifo.put(2)
    # fifo.put(3)
    print(fifo.get())
except QueueError:
    print('Queue error')

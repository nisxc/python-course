class Timer:
    def __init__(self, hr=0, min=0, sec=0):
        self.__hr = hr
        self.__min = min
        self.__sec = sec

    def make_digit(self, val):
        if len(str(val)) == 1:
            return '0'+str(val)
        else:
            return str(val)

    def __str__(self):
        __result = ''
        __grouped_list = [self.__hr, self.__min, self.__sec]
        for i in range(len(__grouped_list)):
            if not i:
                __result += self.make_digit(__grouped_list[i])
            else:
                __result += ':'+self.make_digit(__grouped_list[i])
        return __result

    def next_second(self):
        if self.__sec >= 59:
            self.__sec = 0
            self.next_minute()
        else:
            self.__sec += 1

    def prev_second(self):
        if self.__sec == 0:
            self.__sec = 59
            self.prev_minute()
        else:
            self.__sec -= 1

    def next_minute(self):
        if self.__min >= 59:
            self.__min = 0
            self.next_hour()
        else:
            self.__min += 1

    def prev_minute(self):
        if self.__min == 0:
            self.__min = 59
            self.prev_hour()
        else:
            self.__min -= 1

    def next_hour(self):
        if self.__hr >= 23:
            self.__hr = 0
        else:
            self.__hr += 1

    def prev_hour(self):
        if self.__hr == 0:
            self.__hr = 23
        else:
            self.__hr -= 1


timer_obj = Timer(23, 59, 58)
timer_obj.prev_second()
print(timer_obj)
timer_obj.next_second()
print(timer_obj)
timer_obj.next_second()
print(timer_obj)
timer_obj.next_second()
print(timer_obj)

class WeekError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class Weeker:
    def __init__(self) -> None:
        self.__week_days = ['Mon', 'Tue', 'Wed', 'Fri', 'Sat', 'Sun']
        self.__settedDay = 0

    def __str__(self) -> str:
        return 'Current day is ' + str(self.__week_days[self.__settedDay])

    def add_days(self, n):
        if not type(n) == int:
            raise WeekError('Noooo, you can\'t just use sting here')
        self.__settedDay = n % 7
        self.__week_days[self.__settedDay]

    def subtract_days(self, n):
        if not type(n) == int:
            raise WeekError('Noooo, you can\'t just use sting here')
        self.__settedDay -= n % 7
        self.__week_days[self.__settedDay]


week_obj = Weeker()
try:
    week_obj.add_days('a')
    print(week_obj)
    week_obj.subtract_days(3)
    print(week_obj)
except WeekError:
    print('Something wrong, see you next time!')

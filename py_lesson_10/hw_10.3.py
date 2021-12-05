class StudentDataException(Exception):
    pass


class BadLine(StudentDataException):
    pass


class FileEmpty(StudentDataException):
    pass


def student_diary():
    try:
        student = {}
        filename = input('Enter student data file name: ')
        stream = open(filename, 'rt')
        turns = stream.readlines()
        r_c = 0
        if not turns:
            raise FileEmpty()

        for row in turns:
            r_c += 1
            if row == '\n':
                raise BadLine(r_c)
            result = row.split(' ')
            student[result[0] + ' ' + result[1]
                    ] = ''.join(list(filter(lambda x: x != '\n', result[2])))

        for stud in sorted(student.items(), key=lambda x: x[1]):
            print(stud[0], ':', stud[1])
    except FileEmpty:
        print('[Error] - Empty file')
    except BadLine as BLE:
        print('[Error] - Bad line', BLE.args[0])
    except:
        print('[Error] - No such file')


student_diary()

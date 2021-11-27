from platform import python_version, processor, machine, system
from json import dumps, load
from os.path import exists

isEnd = False
u_conf = {
    "python_version": python_version(),
    "processor": processor(),
    "machine": machine(),
    "system": system()
}
FILE_NAME = u_conf["system"] + '_config-file.json'

if not exists(FILE_NAME):
    conf_file = open(FILE_NAME, 'w')
    conf_file.writelines(dumps(u_conf))
    conf_file.close()

while not isEnd:
    file = open(FILE_NAME)
    dict = load(file)

    if dict['system'] == 'Darwin':
        print('Hello macos!')
    elif dict['system'] == 'Linux':
        print('Wow, you makin\' a hacker!')
    else:
        print('Maybe linux better?')

    print('User system spec:', dict)
    userChoose = input('Are you want to exit, enter Exit key word: ')
    if userChoose in ['Exit']:
        isEnd = True

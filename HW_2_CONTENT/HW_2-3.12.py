EXIT_WORD = "exit"


def calculator(fn, sn, op):
    SUM = '+'
    MIN = '-'
    DEL = '/'
    MOD = '%'

    if(op == SUM):
        print(fn, sn, op)
    elif(op == MIN):
        print('Min result:', fn - sn)
    elif(op == DEL and sn > 0):
        print('Del result:', fn / sn)
    elif(op == MOD and sn > 0):
        print('Mod result:', fn % sn)
    else:
        print('Sorry but we still in progress to add new operation')


fn = input('Enter first number: ')
sn = input('Enter second number: ')
op = input('Enter operation (ex. /,+,%,-) or exit if you wanna quit: ')

if fn and sn and op and op.lower() != EXIT_WORD:
    calculator(int(fn), int(sn), op)
else:
    print('See you next time')

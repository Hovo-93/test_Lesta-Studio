from timeit import timeit

my_isEven = '''
def isEven(value):
    return value & 1
'''

isEven = '''
def isEven2(value):
    return value%2==0
'''
repeat = 10000000


def time_of_function():
    my = timeit(my_isEven, number=repeat, globals=globals())
    is_even = timeit(isEven, number=repeat, globals=globals())

    if my > is_even:
        print(f'{my} время выполнения my_isEven')
        result = my - is_even
        print(f'my_isEven работает {result} секунд быстрее чем isEven')

    else:
        print(f'{is_even} время выполнения isEven')

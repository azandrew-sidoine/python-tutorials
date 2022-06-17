
def main():
    str_val = "Hello World"
    str_val2 = ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
    list = range(1, 10)

    print(str_val2[:3])
    print(str_val[0:3])
    print(str_val2[-3])

    print(' '.join(map(str, list)))
    list2 = list[3:8]
    print(' '.join(map(str, list2)))

    # tuple
    list3 = (1,3,5)

    # for num in list3:
    #     print(num)

    print(' '.join(map(str, list3)))

    print_var_fn("Hello", "world", "Welcome!")


    print_var_named_func("Hello", "world", "Welcome!", name="Dhiki", lastname="Kafechina")

    fn = lambda x, inc: x + inc

    print('Result Incr: {}'.format(incr(2, 1)))
    print('Result Incr Lambda: {}'.format(fn(2, 1)))

    increment_by_10 = create_inc_fn(10)

    print(f'Type of fn2: {type(increment_by_10)}, {increment_by_10}')

    print(f'Result of incrementation by 10 on 3 = {increment_by_10(3)}')
    print(f'Result of incrementation by 10 on 5 = {increment_by_10(5)}')

    increment_by_creator = create_inc_creator()


    print(f'Result of incrementation by 12 on 5 = {increment_by_creator(12)(5)}')

# Expression lambda avec function de rappel
def create_inc_fn(inc: int):
    return lambda x: x + inc

# Expression lambda avec function de rappel
def create_inc_creator():
    return lambda inc: lambda x: x + inc


def incr(num, inc):
    return num + inc


def print_var_fn(*args):
    for item in args:
        print(item)

def print_var_named_func(*args, **kwargs):
    for item in args:
        print([item])
    print('l36: {}, {}'.format(kwargs, type(kwargs)))
    for [key, value] in kwargs.items():
        print([key, value])



def print_var(arg2, arg1=''):
    pass



if __name__ == "__main__":
    main()

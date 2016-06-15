#!/usr/local/bin/python3


# functions
def test_func(num, another=None, one_more=75, *args):
    if another is None:
        another = 112
    print('This is a test function', num, another, one_more)
    print('*args:', args)
    print()


def another_test_func(**kwargs):
    print('This is another test function', kwargs)
    print()


def one_more_test_function():
    return range(25)


def inclusive_range_generator(start, stop, step=1):
    i = start
    while i <= stop:
        yield i
        i += step


def inclusive_range_generator_flex(*args):
    num_args = len(args)
    if num_args < 1:
        raise TypeError('requires at least one argument')
    elif num_args == 1:
        start = 0
        step = 1
        # stop = args[0]
        (stop,) = args
    elif num_args == 2:
        # start = args[0]
        # stop = args[1]
        step = 1
        (start, stop) = args
    elif num_args == 3:
        # start = args[0]
        # step = args[2]
        # stop = args[1]
        (start, stop, step) = args
    else:
        raise TypeError('inclusive_range_generator expect at most 3 arguments, got {}'.format(num_args))
    i = start
    while i <= stop:
        yield i
        i += step


def main():
    test_func(42, one_more=24)
    test_func(42, 24)
    test_func(1, 2, 3, 4, 5, 6, 7, 8)

    another_test_func(one=1, two=2, three=3)
    another_test_func(two=2, one=1, three=3)

    for i in inclusive_range_generator(0, 25, 1):
        print(i, end=' ')
    print()
    for i in inclusive_range_generator_flex(5):
        print(i, end=' ')
    print()
    for i in inclusive_range_generator_flex(6, 10):
        print(i, end=' ')
    print()
    for i in inclusive_range_generator_flex(10, 19, 2):
        print(i, end=' ')
    print()


if __name__ == '__main__':  # some comments in source code
    main()

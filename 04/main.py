#!/usr/local/bin/python3
class Egg:
    def __init__(self, kind='fried'):
        self.kind = kind

    def what_kind(self):
        return self.kind


def main():
    func(3)
    func()
    print('This is the main.py file.')  # comments in instructions
    egg()
    a, b = 0, 1
    if a < b:
        print('a is less than b')
    if b < a:
        print('b is less than a')
    else:
        print('b is not less that a')
    s = "Less than" if a < b else "not less than"
    print(s)

    fried = Egg()
    new_agg = Egg('cool')
    print(fried.what_kind())
    print(newAgg.what_kind())


def egg(): print('egg 2')


def func(a=0):
    for i in range(a, 10):
        print(i, end=' ')
    print()

if __name__ == '__main__':  # some comments in source code
    main()

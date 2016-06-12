#!/usr/local/bin/python3


def b(n):
    print('{:08b}'.format(n))


# operators
def main():
    print(5 / 3)
    print(5 // 3)
    print(5 % 3)
    print(divmod(5, 3))
    print()

    print(0b101)
    b(5)
    x, y = 0x55, 0xaa
    b(x)
    b(y)
    b(x | y)
    b(x & y)
    b(x ^ y)
    b(x ^ 0)
    b(x ^ 0xff)
    b(x << 4)
    b(x >> 4)
    b(~ x)
    print()

    print(type(True))
    print(True and False)
    print(True or False)
    print(True & True)
    a1, b1 = 0, 1
    x1, y1 = 'zero', 'one'
    print(x1 < y1)
    print(a1 < b1)
    s = 'yes' if a1 < b1 and x1 < y1 else 'no'
    print(s)
    print()

    list2 = []
    list1 = [1, 2, 3, 4, 5]
    print(list1[0])
    print(list1[0:2])
    range_ = range(0, 5)
    print(range_)
    list2[:] = range(7)
    print(list2)
    print(list2[0:3])
    print(list2[0:3:-1])

if __name__ == '__main__':  # some comments in source code
    main()

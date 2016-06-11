#!/usr/local/bin/python3
import os

current_directory = os.path.dirname(os.path.realpath(__file__))


# loops
def main():
    a, b = 0, 1
    while b < 50:
        print(b, end=' ')
        a, b = b, a + b
    print()

    fh = open(os.path.join(current_directory, 'main.py'))
    for line in fh.readlines():
        print(line, end='')
    print()
    for num in [1, 2, 3, 4]:
        print(num, end=' ')
    print()
    for ch in "some string":
        print(ch, end=' ')
    print()

    fh = open(os.path.join(current_directory, 'main.py'))
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')
    for index, ch in enumerate("some string"):
        if ch == 's':
            print('index {} is "s"'.format(index))
    print()

    s = 'this is a string'
    for c in s:
        if c == 's':
            continue
        elif c == 'a':
            break
        print(c, end='')

if __name__ == '__main__':  # some comments in source code
    main()

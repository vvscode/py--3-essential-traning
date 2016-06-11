#!/usr/local/bin/python3
def main():
    a, b = 0, 1
    if a < b:
        print('a < b')
    else:
        print('a not less than b')

    v = 'one'
    if v == 'one':
        print('v is one')
    elif v == 'two':
        print('v is two')
    elif v == 'three':
        print('v is three')
    else:
        print('v is some other thing')

    choices = dict(
        one='first',
        two='second',
        three='third',
        four='fourth',
        five='fifth'
    )
    v = 'seven'
    print(choices.get(v))
    print(choices.get(v, 'others'))

    v = 'a > b' if a > b else 'a <= b'
    print(v)


if __name__ == '__main__':  # some comments in source code
    main()

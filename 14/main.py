#!/usr/local/bin/python3
import os

current_directory = os.path.dirname(os.path.realpath(__file__))


# containers
def main():
    t = (1, 2, 3, 4, 5)
    print(len(t))
    print(min(t))
    print(max(t))
    print((1), type((1)), (1,), type((1,)))
    print()

    l = [1, 2, 3, 4, 5]
    print(len(l))
    print(min(l))
    print(max(l))
    print()

    print(t[1])
    l.append(6)
    l.extend(range(7, 20))
    print(l)
    print()

    d = {'one': 1, 'two': 2}
    print(d)
    d = dict(one=1, two=2, three=3)
    print(d)
    print(d.items())
    print(d.keys())
    print(d.values())
    del d['one']
    print(d)
    print()

    fin = open(os.path.join(current_directory, 'utf8.txt'), 'r', encoding='utf_8')
    f_out = open(os.path.join(current_directory, 'utf8.html'), 'w')
    out_bytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127:
                out_bytes += bytes('&#{:04d};'.format(ord(c)), encoding='utf_8')
            else:
                out_bytes.append(ord(c))
    out_str = str(out_bytes, encoding='utf_8')
    print(out_str, file=f_out)
    print(out_str)
    print('Done')


if __name__ == '__main__':  # some comments in source code
    main()

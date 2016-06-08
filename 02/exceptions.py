#!/usr/local/bin/python3

try:
    fh = open('x_lines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("something went wrong ({})".format(e))

print('After all')

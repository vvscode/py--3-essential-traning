#!/usr/local/bin/python3


# exceptions

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename nust end with .txt')


def main():
    try:
        fh = open('filename')
    except IOError as e:
        print('IOError', e)
    else:
        # no error
        for line in fh:
            print(line)
    print()

    try:
        for line in readfile('some_file'):
            print(line)
    except IOError as e:
        print('IOError', e)
    except ValueError as e:
        print('Custom error', e)
    else:
        # no error
        for line in fh:
            print(line)

if __name__ == '__main__':  # some comments in source code
    main()

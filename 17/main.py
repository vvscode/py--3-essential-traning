#!/usr/local/bin/python3
import os
import sys

current_directory = os.path.dirname(os.path.realpath(__file__))


# modules
def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    print()

    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())

    # import urllib.request
    # page = urllib.request.urlopen('http://app.collectriumdev.com')
    # for line in page:
    #     print(str(line, encoding='utf_8'), end='')
    # print()

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day)
    print()

    # run `pip3 install bitstring` in cmd
    import bitstring
    a = bitstring.BitString(bin='01010101')
    print(a.hex, a.bin, a.uint)

    import time, SayTime
    t = time.localtime()
    print("Content-type: text/html\n")
    print(
        "In Phoenix, Arizona, it is now " +
        SayTime.SayTimeT(t).words() +
        time.strftime(', on %A, %d %B %Y.')
    )


if __name__ == '__main__':  # some comments in source code
    main()

#!/usr/local/bin/python3


# strings
def main():
    print("this is a string".upper())
    print("this is a string %d" % 42)
    print("this is a string {}".format(42))
    print()

    s = "This is a string"
    print(s.capitalize())
    print(s.lower())
    print(s.find('is'))
    print(s.replace('This', 'That'))
    print('123412'.isdigit(), "asd1324".isdigit())
    print()

    s2 = '0:{} 1:{}'
    print(s2.format(1, 2))
    print('0:{1} 1:{0} 2:{0}'.format(1, 2))
    d = dict(bob='Bob', fred='Fred')
    print("this is {bob} and that is {fred}".format(**d))
    print()

    s3 = 'this is a string'
    print(s3.split())
    print(s3.split('is'))
    print('_'.join(s3.split()))
    print()

    print("this is a string".center(80, '_'))


if __name__ == '__main__':  # some comments in source code
    main()

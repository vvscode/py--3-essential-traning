#!/usr/local/bin/python3


class Duck:
    def quack(self):
        print('Duck->quack()')

    def walk(self):
        print('Duck->walk()')


# classes
def main():
    donald = Duck()
    print(donald)
    donald.quack()
    donald.walk()

# classes
if __name__ == '__main__':  # some comments in source code
    main()

#!/usr/local/bin/python3


class Animal:
    def talk(self):
        print('Animal -> talk()')

    def walk(self):
        print('Animal -> walk()')

    def clothes(self):
        print('Animal -> clothes')


class Duck(Animal):
    def __init__(self, name=''):
        # __ makes member private
        self.__name = name

    def quack(self):
        print('Duck "{}" -> quack()'.format(self.__name))

    def walk(self):
        super().walk()
        print('Duck "{}" -> walk()'.format(self.__name))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Dog(Animal):
    pass


# classes
def main():
    donald = Duck('Donald')
    print(donald)
    donald.set_name('DonDonald')
    donald.quack()
    donald.walk()
    donald.talk()

    fido = Dog()
    fido.walk()

# classes
if __name__ == '__main__':  # some comments in source code
    main()

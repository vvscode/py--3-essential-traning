#!/usr/local/bin/python3


class Animal:
    def talk(self):
        print('Animal -> talk()')

    def walk(self):
        print('Animal -> walk()')

    def clothes(self):
        print('Animal -> clothes')


class Duck(Animal):
    def __init__(self, name='', age=23):
        # __ makes member private
        self.__name = name
        self.age = age

    def quack(self):
        print('Duck "{}" -> quack()'.format(self.__name))

    def walk(self):
        super().walk()
        print('Duck "{}" -> walk()'.format(self.__name))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # there is also
    # @name.deleter decorator


class Dog(Animal):
    pass


class InclusiveRange:
    def __init__(self, *args):
        num_args = len(args)
        if num_args < 1:
            raise TypeError('requires at least one argument')
        elif num_args == 1:
            self.start = 0
            self.step = 1
            (self.stop,) = args
        elif num_args == 2:
            self.step = 1
            (self.start, self.stop) = args
        elif num_args == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('inclusive_range_generator expect at most 3 arguments, got {}'.format(num_args))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


# classes
def main():
    donald = Duck('Donald')
    print(donald)
    print(donald.name)  # it's private, but work via decorator
    print(donald.age)
    donald.name = 'DonDonald'  # it's private, but work via decorator
    donald.quack()
    donald.walk()
    donald.talk()
    print()

    fido = Dog()
    fido.walk()
    print()

    for i in InclusiveRange(5, 19, 3):
        print('{} in inclusiveRange'.format(i))

# classes
if __name__ == '__main__':  # some comments in source code
    main()

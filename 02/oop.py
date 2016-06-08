#!/usr/local/bin/python3


class Fibonacci:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield self.b
            self.a, self.b = self.b, self.b + self.a

f = Fibonacci(0, 1)
for r in f.series():
    if r > 100:
        break
    print(r, end=' ')


class AnimalActions:
    def quack(self): return self.strings['quack']

    def feathers(self): return self.strings['feathers']

    def bark(self): return self.strings['bark']

    def fur(self): return self.strings['fur']


class Duck(AnimalActions):
    strings = dict(
        quack='Quaaaak!',
        feathers='The duck has gray and white feathers.',
        bark='The duck cannot bark',
        fur='The duck has no fur'
    )


class Person(AnimalActions):
    strings = dict(
        quack='The person imitates a duck!',
        feathers='The person takes a feather from the ground and shows it',
        bark='The person says woof!',
        fur='The person puts on a fur coat'
    )


class Dog(AnimalActions):
    strings = dict(
        quack='Woof!',
        feathers='Dog\'s feather',
        bark='Dog\'s bark',
        fur='Dog fur'
    )


def in_this_doghouse(dog):
    print(dog.bark())
    print(dog.fur())


def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())


def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print('-- In the forest:')
    for o in (donald, john, fido):
        in_the_forest(o)

    print('-- In the doghouse:')
    for o in (donald, john, fido):
        in_this_doghouse(o)

if __name__ == '__main__':
    main()

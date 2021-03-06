import sys
import time

__version__ = "1.1.0"


class NumWords:
    """
        return a number as words,
        e.g., 42 becomes "forty-two"
    """
    _words = {
        'ones': (
            'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ), 'tens': (
            '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ), 'teens': (
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
        ), 'quarters': (
            'o\'clock', 'quarter', 'half'
        ), 'range': {
            'hundred': 'hundred'
        }, 'misc': {
            'minus': 'minus'
        }
    }
    _oor = 'OOR'  # Out Of Range

    def __init__(self, n):
        self.__number = n

    def num_words(self, num=None):
        """Return the number as words"""
        n = self.__number if num is None else num
        s = ''
        if n < 0:  # negative numbers
            s += self._words['misc']['minus'] + ' '
            n = abs(n)
        if n < 10:  # single-digit numbers
            s += self._words['ones'][n]
        elif n < 20:  # teens
            s += self._words['teens'][n - 10]
        elif n < 100:  # tens
            m = n % 10
            t = n // 10
            s += self._words['tens'][t]
            if m:
                s += '-' + NumWords(m).num_words()  # recurse for remainder
        elif n < 1000:  # hundreds
            m = n % 100
            t = n // 100
            s += self._words['ones'][t] + ' ' + self._words['range']['hundred']
            if m:
                s += ' ' + NumWords(m).num_words()  # recurse for remainder
        else:
            s += self._oor
        return s

    def number(self):
        """Return the number as a number"""
        return str(self.__number);


class SayTime(NumWords):
    """
        return the time (from two parameters) as words,
        e.g., fourteen til noon, quarter past one, etc.
    """

    _specials = {
        'noon': 'noon',
        'midnight': 'midnight',
        'til': 'til',
        'past': 'past'
    }

    def __init__(self, h, m):
        self._hour = abs(int(h))
        self._min = abs(int(m))

    def words(self):
        h = self._hour
        m = self._min

        if h > 23:
            return self._oor  # OOR errors
        if m > 59:
            return self._oor

        sign = self._specials['past']
        if self._min > 30:
            sign = self._specials['til']
            h += 1
            m = 60 - m
        if h > 23:
            h -= 24
        elif h > 12:
            h -= 12

        # h_word is the hours word)
        if h is 0:
            h_word = self._specials['midnight']
        elif h is 12:
            h_word = self._specials['noon']
        else:
            h_word = self.num_words(h)

        if m is 0:
            if h in (0, 12):
                return h_word  # for noon and midnight
            else:
                return "{} {}".format(self.num_words(h), self._words['quarters'][m])
        if m % 15 is 0:
            return "{} {} {}".format(self._words['quarters'][m // 15], sign, h_word)
        return "{} {} {}".format(self.num_words(m), sign, h_word)

    def digits(self):
        """return the traditional time, e.g., 13:42"""""
        return "{:02}:{:02}".format(self._hour, self._min)


class SayTimeT(SayTime):  # wrapper for SayTime to use time object
    """
        return the time (from a time object) as words
        e.g., fourteen til noon
    """

    def __init__(self, t):
        self._hour = t.tm_hour
        self._min = t.tm_min


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test()
        else:
            try:
                print(SayTime(*(sys.argv[1].split(':'))).words())
            except TypeError:
                print("Invalid time ({})".format(sys.argv[1]))
    else:
        print(SayTimeT(time.localtime()).words())


def test():
    print("\nnumbers test:")
    list_ = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30,
        50, 51, 52, 55, 59, 99, 100, 101, 112, 900, 999, 1000
    )
    for l in list_:
        print(l, NumWords(l).num_words())

    print("\ntime test:")
    list_ = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15),
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for l in list_:
        print(SayTime(*l).digits(), SayTime(*l).words())

    print("\nlocal time is " + SayTimeT(time.localtime()).words())


if __name__ == "__main__":
    main()

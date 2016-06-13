#!/usr/local/bin/python3
import re
import os

current_directory = os.path.dirname(os.path.realpath(__file__))


# regexps
def main():
    fh = open(os.path.join(current_directory, 'raven.txt'))
    pattern = re.compile('\s(\w*ave\w*)\W', re.IGNORECASE)
    for index, line in enumerate(fh):
        # search
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group(1), ' -> ', match.group(), '|', line.replace(match.group(), '***'), end='')

        match2 = re.search(pattern, line)
        if match2:
            print(match2.group(1).upper())

        # replace
        print(index, re.sub('said', '###', pattern.sub('***', line)), end='')


if __name__ == '__main__':  # some comments in source code
    main()

#!/usr/local/bin/python3
import os

current_directory = os.path.dirname(os.path.realpath(__file__))


# files
def main():
    f = open(os.path.join(current_directory, 'lines.txt'))
    for line in f:
        print(line, end='')
    print()

    infile = open(os.path.join(current_directory, 'bigfile.txt'))
    outfile1 = open(os.path.join(current_directory, 'bigfile.new1.txt'), 'w')
    for line in infile:
        print(line, file=outfile1, end='')
    print('Copy with read line done')
    print()

    buffer_size = 50000
    infile.seek(0)  # reset pointer
    outfile2 = open(os.path.join(current_directory, 'bigfile.new2.txt'), 'w')
    buffer = infile.read(buffer_size)
    while len(buffer):
        outfile2.write(buffer)
        buffer = infile.read(buffer_size)
    print('Cope via buffer done')
    print()

    buffer_size = 50000
    in_bin_file = open(os.path.join(current_directory, 'olives.jpg'), 'rb')
    out_bin_file = open(os.path.join(current_directory, 'olives.new.jpg'), 'wb')
    buffer = in_bin_file.read(buffer_size)
    while len(buffer):
        out_bin_file.write(buffer)
        buffer = in_bin_file.read(buffer_size)
    print('Copy binary via buffer done')

if __name__ == '__main__':  # some comments in source code
    main()

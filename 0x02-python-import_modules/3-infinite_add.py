#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    ad = 0
    for i in range(1, len(argv)):
        ad += int(argv[i])
    print(ad)

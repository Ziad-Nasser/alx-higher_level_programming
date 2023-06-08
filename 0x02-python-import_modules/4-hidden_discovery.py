#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    n = dir(hidden_4)
    for name in n:
        if name[:2] != "__":
            print(name)

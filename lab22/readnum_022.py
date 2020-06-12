#!/usr/bin/env python3

import sys

def main():
    try:
        for line in sys.stdin:
            line = (line.strip())
            if not line.isdigit():
                print(line + " is not a number")
            else:
                s = int("string")

    except ValueError:
        print('Thank you for {}'.format(line))

if __name__ == '__main__':
    main()

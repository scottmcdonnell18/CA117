#!/usr/bin/env python3

import sys

'''capitalize first and last char'''

def cap(s):
    start = s[0]
    end = s[-1]
    return start.capitalize() + s[1:-1] + end.capitalize()

def main():
    for line in sys.stdin:
        s = line.strip()
        if len(s) > 1:
            capitalized = cap(s)
            print(capitalized)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

'''remove first and last chars from a string'''

import sys

def chop(s):
    return(s[1:len(s) - 1])

def main():
    for line in sys.stdin:
        s = line.strip()
        chopped = chop(s)
        if len(chopped) > 0:
            print(chopped)

if __name__ == '__main__':
    main()

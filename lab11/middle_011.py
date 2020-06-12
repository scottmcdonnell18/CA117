#!/usr/bin/env python3

'''returns middle char'''

import sys

def middle(s):
    if (len(s) % 2) == 0:
        return("No middle character!")
    return(s[len(s) // 2])

def main():
    for line in sys.stdin:
        s = (line.strip())
        mid = middle(s)
        print(mid)


if __name__ == '__main__':
    main()

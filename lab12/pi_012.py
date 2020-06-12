#!/usr/bin/env python3

import sys
import math

def pie(n):
    print('{:.{:d}f}'.format(math.pi, n))

def main():
    n = sys.argv[1]
    n = int(n)
    pie(n)

if __name__ == '__main__':
    main()

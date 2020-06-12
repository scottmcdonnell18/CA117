#!/usr/bin/env python3

import sys

def main():
    longest = 0
    poem = []
    for line in sys.stdin:
        l = line.strip()
        poem.append(l)
        if len(l) > longest:
            longest = len(l)

    for l in poem:
        print('{:^{}}'.format(l, int(longest)))


if __name__ == '__main__':
    main()

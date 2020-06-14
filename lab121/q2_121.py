#!/usr/bin/env python3

import sys

def main():
    l = []
    input = sys.stdin.read()
    tokens = input.split('\n')
    line0 = tokens[0].split()
    line1 = tokens[1].split()
    i = 0
    while i < len(line0) and i < len(line1):
        if line0[i] == line1[i]:
            l.append(i)
        i += 1
    print(l)

if __name__ == '__main__':
    main()

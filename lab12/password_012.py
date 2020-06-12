#!/usr/bin/env python3

import sys

def password(s):
    l = [0, 0, 0, 0]
    for char in s:
        if char.isdigit():
            l[0] = 1
            #print(l)
        if char.islower():
            l[1] = 1
            #print(l)
        if char.isupper():
            l[2] = 1
            #print(l)
        if not char.isalnum():
            l[3] = 1
            #print(l)
    return(sum(l))

def main():
    for line in sys.stdin:
        s = (line.strip())
        result = password(s)
        print(result)

if __name__ == '__main__':
    main()

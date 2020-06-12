#!/usr/bin/env python3

import sys

def anagram(s1, s2):
    if len(s1) == len(s2):
        for c in s1:
            if c in s2:
                s2 = s2.replace(c, "", 1)
            else:
                return False
        if s2 == "":
            return True
        else:
            return False
    else:
        return False

def main():
    for line in sys.stdin:
        s1, s2 = line.strip().split()
        print(anagram(s1, s2))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import string
import sys

def palindrome(s):
    j = len(s) - 1
    for i in range(0, len(s) // 2, 1):
        if s[i] != s[j]:
            return False
        else:
            j = j - 1
    return True

def main():
    for line in sys.stdin:
        nl = []
        l = line.strip().split()
        for word in l:
            word = word.strip(string.punctuation).lower()
            nl.append(word)
        s = "".join(nl)
        print(palindrome(s))

if __name__ == '__main__':
    main()

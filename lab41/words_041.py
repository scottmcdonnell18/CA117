#!/usr/bin/env python3

import sys
import string

def main():
    d = {}
    for line in sys.stdin:
        words = line.lower().strip().split()
        for word in words:
            word = word.strip(string.punctuation)
            if word not in d:
                d[word] = 1
            elif word in d:
                d[word] += 1

    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()

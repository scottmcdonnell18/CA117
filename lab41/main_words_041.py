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
        if len(k) > 3 and v >= 3:
            max_k_width = len(max(d.keys(), key=len))
            #max_v_width = len(str(max(d.values())))
            print('{:>{:d}s} : {:{:d}d}'.format(k, max_k_width, v, 2))

if __name__ == '__main__':
    main()

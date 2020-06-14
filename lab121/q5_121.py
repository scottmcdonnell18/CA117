#!/usr/bin/env python3

import sys

def main():
    d = {}
    for line in sys.stdin:
        l = []
        name, scores = (line.strip().split(':'))
        scores = (scores.split(','))
        for score in scores:
            try:
                l.append(int(score))
            except ValueError:
                l.append(0)
        d[name] = sum(l) / len(l)
    for (k, v) in sorted(d.items(), key=sorter, reverse=True):
        print('{:s}: {:.1f}'.format(k, v))

def sorter(t):
    return t[1]

if __name__ == '__main__':
    main()

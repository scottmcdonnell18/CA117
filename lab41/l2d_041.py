#!/usr/bin/env python3

import sys

def main():
    d = l2d(sys.stdin)
    for (k, v) in sorted(d.items()):
        print('{} : {}'.format(k, v))

def l2d(lines):
    d = {}
    lines = lines.readlines()
    keys = lines[0]
    values = lines[1]
    keys, values = (keys.split(), values.split())
    i = 0
    for key in keys:
        d[key] = values[i]
        i += 1
    return(d)

if __name__ == '__main__':
    main()

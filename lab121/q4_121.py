#!/usr/bin/env python3

import sys
import re

def main():
    for line in sys.stdin:
        s = (line.strip())
        words = (re.findall('[A-Z][^A-Z]*', s))
        newwords = [word.lower() for word in words]
        string = (' '.join(newwords))
        print(string.capitalize())

if __name__ == '__main__':
    main()

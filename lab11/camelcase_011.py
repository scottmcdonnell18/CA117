#!/usr/bin/env python3

import sys

def camel(s):
    capitalized = []
    words = s.split(' ')
    for word in words:
        capitalized.append(word.capitalize())
    return ' '.join(capitalized)

def main():
    for line in sys.stdin:
        s = line.strip()
        camelcase = camel(s)
        print(camelcase)

if __name__ == '__main__':
    main()

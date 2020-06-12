#!/usr/bin/env python3

'''capitalizes last letter in each word'''

import sys

def camel(s):
    capitalized = []
    words = s.split(' ')
    for word in words:
        capitalized.append(word[0:-1] + word.upper()[-1])
    return ' '.join(capitalized)

def main():
    for line in sys.stdin:
        s = line.strip()
        camelcase = camel(s)
        print(camelcase)

if __name__ == '__main__':
    main()

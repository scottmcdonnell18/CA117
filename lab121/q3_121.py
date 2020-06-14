#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = (line.strip())
        words = [letter.lower() for letter in line if letter.lower() in 'aeiou']
        if words == list('aeiou'):
            print(line)

if __name__ == '__main__':
    main()

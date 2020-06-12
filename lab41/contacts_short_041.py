#!/usr/bin/env python3

import sys

def main():
    d = {}
    with open(sys.argv[1], 'r') as f:
        for contact in f:
            name, number = (contact.strip().split())
            d[name] = number

    for line in sys.stdin:
        name = (line.strip())
        if name in d:
            print('Name: {}'.format(name))
            print('Phone: {}'.format(d[name]))
        else:
            print('Name: {}'.format(name))
            print('No such contact')

if __name__ == '__main__':
    main()

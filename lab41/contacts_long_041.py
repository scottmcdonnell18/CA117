#!/usr/bin/env python3

import sys

def main():
    d = {}
    with open(sys.argv[1], 'r') as f:
        for contact in f:
            name, number, email = (contact.strip().split())
            d[name] = number, email

    for line in sys.stdin:
        name = (line.strip())
        if name in d:
            print('Name: {}'.format(name))
            print('Phone: {}'.format(d[name][0]))
            print('Email: {}'.format(d[name][1]))
        else:
            print('Name: {}'.format(name))
            print('No such contact')

if __name__ == '__main__':
    main()

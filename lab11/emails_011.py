#!/usr/bin/env python3

import sys

def email(s):
    names = s.split('@')[0]
    firstname = names.split('.')[0]
    surname = names.split('.')[1]
    fullname = firstname.capitalize(), surname.capitalize()
    name = (' '.join(fullname))
    cleaned = name[0:-2]
    return(cleaned)

def main():
    for line in sys.stdin:
        s = (line.strip())
        name = email(s)
        print(email(s))

if __name__ == '__main__':
    main()

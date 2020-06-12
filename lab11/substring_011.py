#!/usr/bin/env python3

import sys

def substring(s):
    sub = s.split()[0]
    string = s.split()[1]
    #return(sub, string)
    if sub in string:
        return(True)
    return(False)

def main():
    for line in sys.stdin:
        s = line.strip().lower()
        subs = substring(s)
        print(subs)

if __name__ == '__main__':
    main()

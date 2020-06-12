#!/usr/bin/env python3

import sys

def plural(s):
    vowels = ["a", "e", "o", "u", "i"]
    if s[-1] == "o":
        return(s + "es")
    elif s[-1] == "f":
        return(s[0:-1] + "ves")
    elif s[-2:] == "fe":
        return(s[0:-2] + "ves")
    elif s[-2:] == "ch" or s[-2:] == "sh" or s[-1] == "x" or s[-1] == "s" or s[-1] == "z":
        return(s + "es")
    elif s[-1] == "y" and s[-2] in vowels:
        return(s + "s")
    elif not s[-2] == vowels and s[-1] == "y":
        return(s[0:-1] + "ies")
    else:
        return(s + "s")

def main():
    for line in sys.stdin:
        s = (line.strip())
        pluraled = plural(s)
        print(pluraled)

if __name__ == '__main__':
    main()

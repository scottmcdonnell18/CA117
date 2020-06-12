#!/usr/bin/env python3

import sys

def contains(word1, word2):
    if len(word1) > len(word2):
        return False
    else:
        for c in word1:
            if c in word2:
                word2 = word2.replace(c, "", 1)
                word1 = word1.replace(c, "", 1)
        if word1 == "":
            return True
        else:
            return False


def main():
    for line in sys.stdin:
        word1, word2 = line.strip().lower().split()
        print(contains(word1, word2))


if __name__ == '__main__':
    main()

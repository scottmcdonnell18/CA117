#!/usr/bin/env python3

import sys

def main():
    num_tokens = 0
    for line in sys.stdin:
        tokens = line.split()
        num_tokens += len(tokens)
    print(num_tokens)

if __name__ == '__main__':
    main()

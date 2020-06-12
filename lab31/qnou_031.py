#!/usr/bin/env python3

import sys

def main():
    words = []
    for line in sys.stdin:
        words.append(line.strip())

    print('Words with q but no u: {}'.format(([x for x in words if not x.startswith('qu') and 'qu' not in x])))

if __name__ == '__main__':
    main()

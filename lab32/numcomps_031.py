#!/usr/bin/env python3

import sys

n = int(sys.argv[1]) + 1

def is_prime(x):
    if x == 1:
        return False
    else:
        a = 2
        while x > a:
            if x % a == 0:
                return False
            a = a + 1
        return True

def main():
    print("Multiples of 3: {}".format([x for x in range(1, n) if x % 3 == 0]))
    print("Multiples of 3 squared: {}".format([x * x for x in range(1, n) if (x % 3 == 0)]))
    print("Multiples of 4 doubled: {}".format([x * 2 for x in range(1, n) if (x % 4 == 0)]))
    print(("Multiples of 3 or 4: {}".format([x for x in range(1, n) if x % 3 == 0 or x % 4 == 0])))
    print(("Multiples of 3 and 4: {}".format([x for x in range(1, n) if x % 3 == 0 and x % 4 == 0])))
    print(("Multiples of 3 replaced: {}".format([x if x % 3 != 0 else 'X' for x in range(1, n)])))
    print(("Primes: {}".format([x for x in range(1, n) if is_prime(x)])))

if __name__ == '__main__':
    main()

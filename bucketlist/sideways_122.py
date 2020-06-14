#!/usr/bin/env python3

import sys

def total_lines(l):
    total = 0
    for i in l:
        total += 1
    return total

def length_words(l):
    return len(l[0].strip())

def sort(l):
    return l.lower()

def main():
    arr = []
    lines = sys.stdin.readlines()
    total = total_lines(lines)
    length = length_words(lines)
    i = 0
    while i < length:
        arr.append("")
        i += 1
    j = 0
    while j < length:
        for line in lines:
            line = line.strip()
            arr[j] += line[j]
        j += 1
    arr.sort(key=sort)
    k = 0
    while k < total:
        output = ''
        for i in arr:
            output += i[k]
        print(output)
        k += 1

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys


def countes(words):
    larg = 0
    for word in words:
        if word.count('e') > larg:
            larg = word.count('e')
    return(larg)

def main():
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    largest = countes(words)
    print("Words containing 17 letters: {}".format([x for x in words if len(x) == 17]))
    print("Words containing 18+ letters: {}".format([x for x in words if len(x) >= 18]))
    print("Shortest word containing all vowels: {}".format(sorted([x for x in words if all(t in x.lower() for t in 'aeoiu')], key=len)[0]))
    print("Words with 4 a's: {}".format([x for x in words if x.lower().count('a') == 4]))
    print("Words with 2+ q's: {}".format([x for x in words if x.lower().count('q') >= 2]))
    print("Words containing cie: {}".format([x for x in words if 'cie' in x]))
    print("Anagrams of angle: {}".format([x for x in words if sorted(x.lower()) == sorted("angle") and x != "angle"]))
    print("Words ending in iary: {}".format(len([x for x in words if x.lower().endswith('iary')])))
    print("Words with most e's: {}".format([x for x in words if x.lower().count('e') == largest]))

if __name__ == '__main__':
    main()

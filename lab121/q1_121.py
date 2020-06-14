#!/usr/bin/env python3

import sys

def main():
	s = sys.argv[1]
	n = int(sys.argv[2])
	t = len(s) % n
	newstr = s[-t:] + s[:-t]
	print(newstr)

if __name__ == '__main__':
	main()
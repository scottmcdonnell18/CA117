#!/usr/bin/env python3

import sys


def main():
    xvalues = []
    yvalues = []
    for line in sys.stdin:
        x, y = line.strip().split()
        xvalues.append(x)
        yvalues.append(y)
    for i in range(0, len(xvalues)):
        xvalues[i] = int(xvalues[i])
    for i in range(0, len(yvalues)):
        yvalues[i] = int(yvalues[i])

    x4 = xvalues[0] + (xvalues[2] - xvalues[1])
    y4 = yvalues[0] + (yvalues[2] - yvalues[1])

    g = xvalues[1] + (xvalues[0] - xvalues[2]) 
    h = yvalues[1] + (yvalues[0] - yvalues[2])

    #print(x4, y4)
    #for i in range(0, len(xvalues)):
    if x4 == xvalues[0] or x4 == xvalues[1] or x4 == xvalues[2]:
        print(x4, y4)
    elif y4 == yvalues[0] or y4 == yvalues[1] or y4 == yvalues[2]:
        print(x4, y4)
    else:
        print(g, h)

if __name__ == '__main__':
    main()

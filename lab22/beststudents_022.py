#!/usr/bin/env python3

import sys

def main():
    try:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            topmark = 0
            topstu = ''
            l = []
            for line in lines:
                mark = line.strip().split()[0]
                name = line.strip().split()[1:]
                if int(mark) > topmark:
                    topmark = int(mark)
                    topstu = '' + ' '.join(name)

            for line in lines:
                mark = line.strip().split()[0]
                name = line.strip().split()[1:]
                if topmark == int(mark):
                    l.append(' '.join(name))

            print('Best student(s): {}'.format(', '.join(l)))
            print('Best mark: {}'.format(topmark))

    except FileNotFoundError:
        print('The file {} could not be opened.'.format(sys.argv[1]))

if __name__ == '__main__':
    main()

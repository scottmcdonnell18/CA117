#!/usr/bin/env python3

import sys

def main():
    try:
        with open(sys.argv[1], 'r') as f:
            topmark = 0
            topstu = ''
            l = []
            for line in f:
                mark = line.strip().split()[0]
                name = line.strip().split()[1:]
                if int(mark) > topmark:
                    topmark = int(mark)
                    topstu = '' + ' '.join(name)

            print('Best student: {}'.format(topstu))
            print('Best mark: {}'.format(topmark))

    except FileNotFoundError:
        print('The file {} could not be opened.'.format(sys.argv[1]))

    except ValueError:
        print('Invalid mark {} encountered. Exiting.'.format(mark))

if __name__ == '__main__':
    main()

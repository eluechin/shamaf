#!/usr/bin/python

import sys
import getopt


def main(argv):
    #print('Number of arguments: ' + str(len(sys.argv)) + ' arguments.')
    #print('Argument List: ' + str(sys.argv))

    try:
        opts, args = getopt.getopt(argv, "o:s:d:", ["obfuscation=", "static=", "dynamic="])
    except getopt.GetoptError:
        print('Error in parameter list!')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-o', '--obfuscation'):
            print('Obfuscation: ' + str(arg))
            #sys.exit()
        elif opt in ('-s', '--static'):
            print('Static: ' + str(arg))
            #sys.exit()
        elif opt in ('-d', '--dynamic'):
            print('Dynamic: ' + str(arg))
            #sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])

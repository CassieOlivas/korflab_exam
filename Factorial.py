# Computes the factorial of a number given on the command line.
#   Reports an error if the command line parameter is illegal.
#   The error must be sent to stderr, and the program must exit with non-zero status.

import numpy
import sys

val = (input("Enter your number to compute the factorial: "))

badChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0']

newVal = 0

for x in val:
    if x in badChar:
        sys.stderr.write('Error: Please use only non-zero numbers.\n')
        sys.exit()
    else:
        newVal = int(val)

val_list = list(range(1,newVal+1))

print(sum(val_list))
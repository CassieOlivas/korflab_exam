#Prints the numbers 1-100, except for:
    # If the number is divisible by 3, print "Fizz" instead.
    # If the number is divisible by 5, print "Buzz" instead.
    # If the number is divisible by 3 and 5, print "FizzBuzz" instead.

import numpy

a_list = list(range(1,100))

for x in a_list:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
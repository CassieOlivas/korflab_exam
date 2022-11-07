# Program calculates the median, mean, and standard deviation of values that are given on the command line.
#   Illegal values are skipped, but generate a warning that is sent to stderr.

import numpy
import sys

print("Enter your numbers on the line below and I will calculate the median, mean, and standard deviation.")
userInput = (input("Please separate the numbers with a space: "))

val = userInput.split()

newVal = []

badChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0']

for x in val:
    tempVal = x
    if tempVal.isdigit() == False:
        sys.stderr.write("Incorrect value type. Next time please use only integers. \n")
    else:
        newVal.append(int(x))

# # Debugging: Check output type.
# print(newVal)
# for x in newVal:
#     print(type(x))

# Calculate the mean.
sum, count = 0, 0

for x in newVal:
    sum = sum + x
    count += 1

print("The mean is: " + str(sum/count))

# Calculate the median.


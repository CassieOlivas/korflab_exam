# Program calculates the mean, median, and standard deviation of values that are given on the command line.
#   Illegal values are skipped, but generate a warning that is sent to stderr.

import numpy as np
import sys
import pandas as pd

print("Enter your numbers on the line below and I will calculate the median, mean, and standard deviation.")
userInput = (input("Please separate the numbers with a space: "))

val = userInput.split()

newVal = []

for x in val:
    tempVal = x
    if tempVal.isdigit() == False:
        sys.stderr.write("Warning, " + tempVal + " is an incorrect value type. Next time please use only integers. \n")
        # Considers floats as an incorrect value type.
    else:
        newVal.append(int(x))

# # Debugging: Check output type.
# print(newVal)
# for x in newVal:
#     print(type(x))

# # Calculate the mean.
sum, count = 0, 0

for x in newVal:
    sum = sum + x
    count += 1

print("Mean: " + str(sum/count))

# Calculate the median.
midVal = len(newVal)/2

arrayVal = np.array(newVal)

if float(midVal).is_integer() == True:
    #Length of list is even.
    intVal = int(midVal)
    firstHalf = newVal[:intVal]
    secondHalf = newVal[intVal:]
    tempVal = (firstHalf[intVal - 1] + secondHalf[0]) / 2
    print("Median: " + str(tempVal))
else:
    #Length of list is odd.
    tempVal = arrayVal[int(midVal)]
    print("Median: " + str(tempVal))

# Calculate the standard deviation.
# # Calculate the mean.
meanVal = (sum/count)

arraySD = []

# # Find the square of the distance from the mean.
for x in newVal:
    tempVal = x - meanVal
    tempVal2 = tempVal**2
    arraySD.append(tempVal2)

# # Sum of the values.
sumSD = 0

for x in arraySD:
    sumSD = sumSD + x

# # Divide by the number of values and take the square root.
standDev = sumSD / len(newVal)
standDevSQRT = standDev**(1/2)
print("Standard Deviation: " + str(standDevSQRT))
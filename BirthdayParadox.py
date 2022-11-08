# Program creates a simulation of the birthday paradox asking what is the probability that two people share the same birthday?
# It is limited to arrays only. Dictionaries, sets, and other data structures are not included.

import random

# Create a person with a random birthday.
def Person():
    bDay = random.randrange(10)
    return bDay

# Record the dates and randomize a comparison.
bDayArray = []
bDayArray_Compare = []
bDayArray_Compare.append(Person())
count = 0

for x in range(500): #Set arbitrary number for looping.
    bDayArray.append(Person())
    count += 1
    if bDayArray[x] == bDayArray_Compare[0]:
        print("It took " + str(count) + " people to find a matching birthday.")
        break
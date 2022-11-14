# Program computes the local hydrophilicity/hydrophobicity in a sequence.
# The sequence and window size are command line parameters.
# The output is tabular with columns for position and average hydropathy at the position.

import numpy as np

userInput_Seq = (input("Please insert your amino acid sequence: "))
userInput_Window = (input("Please give the window length: "))

dict_Values = {'I': 4.5,
               'V': 4.2,
               'L': 3.8,
               'F': 2.8,
               'C': 2.5,
               'M': 1.9,
               'A': 1.8,
               'G': -0.4,
               'T': -0.7,
               'S': -0.8,
               'W': -0.9,
               'Y': -1.3,
               'P': -1.6,
               'H': -3.2,
               'E': -3.5,
               'Q': -3.5,
               'D': -3.5,
               'N': -3.5,
               'K': -3.9,
               'R': -4.5
}


#Declare variables.
seq_Array = list(userInput_Seq)
tempArray = []
finalDict = {}
sumVal = 0
count = len(seq_Array)

# # Hydrophilicity/hydrophobicity for the entire sequence ignoring non-key parameters.
# for x in seq_Array:
#     if x in dict_Values:
#         print(x, dict_Values[x])

# Average hydrophilicity/hydrophobicity based on the sequence window.
if len(seq_Array) % userInput_Window == 0: #Check if the entire sequence will be easily divided by the window, or if it'll have a remainder.
    for x in seq_Array:
        tempArray.append(x)
        sumVal = sumVal + dict_Values[x]
        if len(tempArray) == userInput_Window:
            strKey = ''.join(tempArray)
            tempDict = {strKey: sumVal}
            finalDict.update(tempDict)
            # Empty values for next iteration.
            sumVal = 0
            tempArray = []
else:
    for x in seq_Array:
        tempArray.append(x)
        sumVal = sumVal + dict_Values[x]
        count -= 1
        if len(tempArray) == userInput_Window:
            strKey = ''.join(tempArray)
            tempDict = {strKey: sumVal}
            finalDict.update(tempDict)
            # Empty values for next iteration.
            sumVal = 0
            tempArray = []
        elif count < (len(seq_Array) % userInput_Window):
            strKey = ''.join(tempArray)
            tempDict = {strKey: sumVal}
            finalDict.update(tempDict)

for x in finalDict:
    print(x, round(finalDict[x], 5))
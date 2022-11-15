# Program computes the amino acid composition of a sequence given on the command line.
# Output is sorted alphabetically.

def DNAtoAA(userInput_Seq):

    AA_Values = {'TTT': 'F',
                 'TTC': 'F',
                 'TTA': 'L',
                 'TTG': 'L',
                 'CTT': 'L',
                 'CTC': 'L',
                 'CTA': 'L',
                 'CTG': 'L',
                 'ATT': 'I',
                 'ATC': 'I',
                 'ATA': 'I',
                 'ATG': 'M',
                 'GTT': 'V',
                 'GTC': 'V',
                 'GTA': 'V',
                 'GTG': 'V',
                 'TCT': 'S',
                 'TCC': 'S',
                 'TCA': 'S',
                 'TCG': 'S',
                 'CCT': 'P',
                 'CCC': 'P',
                 'CCA': 'P',
                 'CCG': 'P',
                 'ACT': 'T',
                 'ACC': 'T',
                 'ACA': 'T',
                 'ACG': 'T',
                 'GCT': 'A',
                 'GCC': 'A',
                 'GCA': 'A',
                 'GCG': 'A',
                 'TAT': 'Y',
                 'TAC': 'Y',
                 'TAA': 'STOP',
                 'TAG': 'STOP',
                 'CAT': 'H',
                 'CAC': 'H',
                 'CAA': 'Q',
                 'CAG': 'Q',
                 'AAT': 'N',
                 'AAC': 'N',
                 'AAA': 'K',
                 'AAG': 'K',
                 'GAT': 'D',
                 'GAC': 'D',
                 'GAA': 'E',
                 'GAG': 'E',
                 'TGT': 'C',
                 'TGC': 'C',
                 'TGA': 'STOP',
                 'TGG': 'W',
                 'CGT': 'R',
                 'CGC': 'R',
                 'CGA': 'R',
                 'CGG': 'R',
                 'AGT': 'S',
                 'AGC': 'S',
                 'AGA': 'R',
                 'AGG': 'R',
                 'GGT': 'G',
                 'GGC': 'G',
                 'GGA': 'G',
                 'GGG': 'G'
    }

    seq_Array = list(userInput_Seq)
    tempArray = []
    finalArray = []

    # Create an array with the amino acid sequences.
    for x in seq_Array:
        tempArray.append(x)
        if len(tempArray) == 3:
            strKey = ''.join(tempArray)
            finalArray.append(AA_Values[strKey])
            tempArray = []

    finalArray = sorted(finalArray)

    return finalArray

def AACounter():
    # Create a counter for the amino acids.
    counterDict = {}

    for y in DNAtoAA(userInput_Seq):
        if y not in counterDict:
            counterDict[y] = 0
        counterDict[y] += 1

    # Print results based on percentage.

    print("Amino Acid Composition")

    for z in counterDict:
        print(z, (counterDict[z] / len(counterDict)))

    return counterDict

# Main Code

# Test sequence.
# userInput_Seq = "ACAGCCCGACTACTACTA"

userInput_Seq = (input("Please insert your DNA sequence: "))

DNAtoAA(userInput_Seq)
AACounter()

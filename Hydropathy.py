# Program computes the local hydrophilicity/hydrophobicity in a sequence.
# The sequence and window size are command line parameters.
# The output is tabular with columns for position and average hydropathy at the position.

# userInput_Seq = (input("Please insert your sequence: "))
# userInput_Window = (input("Please give the window length: "))


userInput_seq = "ACAAGATGCCAT"

# userInput_seq = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC" \
#                 "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC" \
#                 "CTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG" \
#                 "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCC" \
#                 "CTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG" \
#                 "TTTAATTACAGACCTGAA"

userInput_window = 3

seq_arrayTemp = []
seq_dict = {}
count = 0

for x in userInput_seq:
    seq_arrayTemp.append(x)
    if len(seq_arrayTemp) == userInput_window:
        count += 1
        seq_dict[count].append(x)


print(len(userInput_seq))
print(seq_arrayTemp)
print(len(seq_arrayTemp))
print(seq_dict)


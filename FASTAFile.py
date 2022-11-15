# Function that reads a FASTA file and puts it in a library.

import pandas as pd
from itertools import groupby

def FASTAFile(fasta_name):
    file = open('fastaExample.fasta', 'r')


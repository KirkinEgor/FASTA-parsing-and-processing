from itertools import islice
import os
from FASTA import Seq
from FASTA import FastaReader


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "Sample.fasta")
read = FastaReader(file_path)
for seq in islice(read.read_seq(), 10):
    print(str(seq))
    print(seq.seq_len)
    print(seq.alphabet)
    print("\n")
# CEA003_Chunk_file

This script is written in python 3.x
This script reads a .fasta file and splits the sequences in user defined sized chunks.

required packages: sys, getopt, biopython

parameters:
inputfile: path to .fasta file, outputfile: path to output, number: maximum length of chunk, minimum: minimum length of chunk

While in the directory of the script:
./CEA003_Chunk_file_v2.1.py -i <inputfile> -o <outputfile> -n <number> -m <minimum>

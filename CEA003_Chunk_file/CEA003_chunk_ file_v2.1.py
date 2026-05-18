#!/usr/bin/env python

"""
Written by Lucas van der Gouw
31-1-17
Updated by Lucas van der Gouw
23-10-2020

This script reads a .fasta file and splits the sequences in user defined sized chunks.
"""

import sys, getopt
from Bio import SeqIO

def command(argv):
    '''
    Get values for necessary parameters
    :param argv:
    :return: inputfile: path to .fasta file, outputfile: path to output, number: maximum length of chunk, minimum: minimum length of chunk
    '''
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:n:m:",["ifile=","ofile=","number=","minimum="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile> -n <number> -m <minimum>')
      sys.exit(2)
   for opt, arg in opts:
    if opt == '-h':
         print ('chunker.py -i <inputfile> -o <outputfile> -n <number> -m <minimum>')
         sys.exit()
    elif opt in ("-i", "--ifile"):
         inputfile = arg
    elif opt in ("-o", "--ofile"):
         outputfile = arg
    if opt in ("-n", "--number"):
        number = int(arg)
    if opt in ("-m", "--minimum"):
        minimum = int(arg)
   return inputfile, outputfile, number, minimum

def open_files(inputfile):
    '''
    Open input .fasta and add contig names and contig sequences to lists
    :param inputfile: Path to .fasta
    :return: sequences: list with sequences, contigs: list with contig names
    '''
    contigs = []
    sequences = []
    for record in SeqIO.parse(inputfile, "fasta"):
        contigs.append(record.id)
        sequences.append(record.seq)
    return sequences, contigs

def chunk_content(sequences, number, minimum, contigs):
    '''
    Chunks the sequences.
    If length of sequence is lower then minimum - increase the index of sequences and contig lists by 1 without adding to string.
    If length of seqences is higher then minimum - add contig name and sequence from lists at current index to string.
    If sequence length is lower then maximum, keep adding sequences under the same list index
    but remove a number of nucleotides equal to the maximum from the sequence till length of sequence is smaller then minimum.
    :param sequences: list with sequences
    :param number: maximum length of chunk
    :param minimum: minimum length of chunk
    :param contigs: list with contig names
    :return: chunk_string: string with chunked sequences
    '''
    contignumber = 0 
    chunk_string = ""
    chunknumber = 1
    for contig in contigs:
        if len(sequences[contignumber]) < minimum:
            chunknumber += 1
        elif len(sequences[contignumber]) >= minimum:
            while sequences[contignumber]:
                if len(sequences[contignumber][:number]) >= minimum:
                    chunk_string += ">" + str(contigs[contignumber]) + "_chunk" + str(chunknumber) + "\n" + (sequences[contignumber][:number]) + "\n"
                    chunknumber += 1 
                sequences[contignumber] = sequences[contignumber][number:]
        contignumber += 1                  
    return chunk_string

def write_file(outfile, chunk_string):
    '''
    Writes chunked sequences to a file
    :param outfile: Path to output
    :param chunk_string: string with chunked sequences
    :return:
    '''
    write_file = open(outfile, "w")
    write_file.write(str(chunk_string))
    write_file.close
        
def main(argv):
    inputfile, outfile, number, minimum = command(argv)
    sequences, contigs = open_files(inputfile)
    chunk_string = chunk_content(sequences, number, minimum, contigs)
    write_file(outfile, chunk_string)
    
if __name__ == "__main__":
   main(sys.argv[1:])

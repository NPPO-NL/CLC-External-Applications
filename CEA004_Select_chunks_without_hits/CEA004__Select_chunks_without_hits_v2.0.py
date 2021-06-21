#!/usr/bin/env python
"""
Created on Mon Apr 24 13:43:32 2017

@author: Lucas v.d. Gouw
This script reads a BLASTn result en the multi-fasta that was used for BLASTn, 
extracts the sequences without BLASTn hit and writes this in a new multi-fasta file.
"""

import sys, getopt, re
from Bio import SeqIO

def command(argv):
    '''
    Get values for necessary parameters
    :param argv:
    :return: inputfile1: Path to BLASTn table, inputfile2: Path to .fasta, outputfile: Path to output
    '''
   inputfile1 = ''
   inputfile2 = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hb:c:o:",["ifile1=","ifile2=","ofile="])
   except getopt.GetoptError:
      print ('test.py -b <inputfile1> -c <inputfile2> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
    if opt == '-h':
         print ('selector.py -b <inputfile1> -c <inputfile2> -o <outputfile>')
         sys.exit()
    elif opt in ("-b", "--ifile1"):
         inputfile1 = arg
    elif opt in ("-c", "--ifile2"):
         inputfile2 = arg
    elif opt in ("-o", "--ofile"):
         outputfile = arg
   return inputfile1, inputfile2, outputfile

def open_files(inputfile1, inputfile2):
    '''
    read the BLASTn result and multi-fasta
    :param inputfile1: Path to BLASTn table
    :param inputfile2: Path to .fasta
    :return: read_file1: opened BLASTn table, read_file2: opened .fasta
    '''
    read_file1 = open(inputfile1,"r")
    read_file2 = open(inputfile2,"r")

    return read_file1, read_file2

def add_sequences(read_file1):
    '''
    add BLASTn file to string, use regular expressions to find sequences with 0 hits
    find the sequence names and add the sequence name to a set
    :param read_file1: opened BLASTn table
    :return: sequences: set with sequence names
    '''
    sequences = set()
    blast_file =""
    counter = 0
    for line in read_file1:
        blast_file += line
    read_file1.close()
    matches = re.findall('Query: .+chunk\d*', blast_file)
    hits = re.findall('\d* hits', blast_file)
    for match in matches:
        match = match.replace("Query: ","")
        hitnumber = hits[counter]
        counter += 1
        hitnumber = hitnumber.replace(" hits","")
        if hitnumber == "0":
          sequences.add(str(match))

    return sequences

def processSequences(sequences, sequenceFile, outfile):
    '''
    check if sequence name is in .fasta and add new .fasta file
    :param sequences: sequence names
    :param sequenceFile: Path to .fasta
    :param outfile: Path to .fasta to be written
    :return:
    '''
    new =[]
    for s in SeqIO.parse(sequenceFile, "fasta"):
        if s.id in sequences:
            new.append(s)
    SeqIO.write(new, outfile, "fasta")

def main(argv):
    inputfile1, inputfile2, outfile = command(argv)
    read_file1, read_file2 = open_files(inputfile1, inputfile2)
    sequences = add_sequences(read_file1)
    processSequences(sequences, read_file2, outfile)
    
if __name__ == "__main__":
   main(sys.argv[1:])

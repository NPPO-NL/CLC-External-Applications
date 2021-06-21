#!/usr/bin/env python

"""
Written by Lucas van der Gouw
30-4-2018
This script reads a BLASTN hit table and compares the tax_id of the top hit with 
a list of tax_ids and filters the BLASTN results.
"""

import sys, getopt
from Bio import SeqIO

def command(argv):
    '''
    Get values for necessary parameters
    :param argv:
    :return: blastfile: Path to BLAST table, taxafile: path to file with taxanomy numbers,
    chunkfile: Path to .fasta with sequences, filterfile: Path to output, filetype: number to determane BLASTn or BLASTx input
    '''
   blastfile = ''
   taxafile = '' 
   filterfile = ''
   filetype = ''
   try:
      opts, args = getopt.getopt(argv,"hb:t:c:u:y:",["blastfile=","taxafile=","out1=","out2="])
   except getopt.GetoptError:
      print ('filter.py -i <inputfile> -o <outputfile> -n <number> -m <minimum>')
      sys.exit(2)
   for opt, arg in opts:
    if opt == '-h':
         print ('chunker.py -b <inputfile> -t <outputfile> -o1 <number> -o2 <minimum>')
         sys.exit()
    elif opt in ("-b", "--ifile"):
         blastfile = arg
    elif opt in ("-t", "--ofile"):
         taxafile = arg
    if opt in ("-c", "--number"):
        chunkfile = arg
    if opt in ("-u", "--minimum"):
        filterfile = arg
    if opt in ("-y", "--minimum"):
        filetype = arg       
   return blastfile, taxafile, chunkfile, filterfile, filetype
   
def open_files(blastfile, taxafile, chunkfile):
    '''
    Open nessecary files
    :param blastfile: Path to BLAST table
    :param taxafile: path to file with taxanomy numbers
    :param chunkfile: Path to .fasta with sequences
    :return: read_file1: open BLAST table, read_file2:open file with taxanomy numbers
    read_file3: open .fasta file
    '''
    read_file1 = open(blastfile,"r")
    read_file2 = open(taxafile,"r")
    read_file3 = open(chunkfile,"r")
    return read_file1, read_file2, read_file3

def find_taxa_blastn(read_file1, read_file2):
    '''
    Read BLASTn table and check taxanomy of first hit in BLASTn table
    :param read_file1: open BLASTn table
    :param read_file2: open file with taxanomy numbers
    :return: titlelist: list with sequence names
    '''
    titlelist = []
    blastfile = read_file1.readlines()
    taxfile = read_file2.readlines()
    read_file1.close()
    read_file2.close()
    while blastfile:
        try: 
            tax_ID = blastfile[5].split("\t")[12]
        except IndexError:
            tax_ID = 1
        del blastfile[0]
        try:
            BLASTend = int(blastfile.index('# BLASTN 2.9.0+\n'))
        except ValueError:
            for item in blastfile:
                if 'BLAST' in item:
                    BLASTend = int(blastfile.index(item)) + 1
        if str(tax_ID) + "\n" in taxfile:
            try:
                title = (blastfile[0:BLASTend][0])
                title = title.replace("# Query: ","")
                title = title.replace("\n","")
                titlelist.append(title)
            except IndexError:
                break
            for item in blastfile[0:BLASTend]:
                del blastfile[0]     
    
    return titlelist
    
def find_taxa_blastx(read_file1, read_file2):
    '''
    Read BLASTn table and check taxanomy of first hit in BLASTx table
    :param read_file1: open BLASTn table
    :param read_file2: open file with taxanomy numbers
    :return: titlelist: list with sequence names
    '''
    titlelist = set()
    blastfile = read_file1.readlines()
    taxfile = read_file2.readlines()
    read_file1.close()
    read_file2.close()
    while blastfile:
        try: 
            tax_ID = blastfile[0].split("\t")[12]
        except IndexError:
            tax_ID = 1
        if str(tax_ID) in taxfile:
            titlelist.add(blastfile[0].split("\t")[0])
        del blastfile[0]
        
    return titlelist
        
def find_sequences(read_file3, titlelist, filterfile):
    '''
    Select sequence names from list, find their sequences and write a new .fasta
    :param read_file3: open .fasta file
    :param titlelist: list with sequence names
    :param filterfile: Path to output
    :return:
    '''
    new =[]
    for s in SeqIO.parse(read_file3, "fasta"):
        if s.id in titlelist:
            new.append(s)
    SeqIO.write(new, filterfile, "fasta")
    
def main(argv):
    blastfile, taxafile, chunkfile, filterfile, filetype = command(argv)
    read_file1, read_file2, read_file3 = open_files(blastfile, taxafile, chunkfile)
    if filetype == "1":
        titlelist = find_taxa_blastn(read_file1, read_file2)
    else:
        titlelist = find_taxa_blastx(read_file1, read_file2)
    find_sequences(read_file3, titlelist, filterfile)
    
if __name__ == "__main__":
   main(sys.argv[1:])
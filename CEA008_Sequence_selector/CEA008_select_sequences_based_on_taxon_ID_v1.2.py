#!/usr/bin/env python

"""
Written by Lucas van der Gouw
28-11-2022
version: 1.2
This script reads a BLASTN hit table and compares the tax_id of the top hit with 
a list of tax_ids. For tax_id that match, the query is written to a fasta file along with its sequence
(obtained from a multifasta (" chunkfile" ))   
"""


import sys, getopt, re
from Bio import SeqIO

def command(argv):
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
    read_file1 = open(blastfile,"r")
    read_file2 = open(taxafile,"r")
    read_file3 = open(chunkfile,"r")
    return read_file1, read_file2, read_file3

def find_taxa_blastn(read_file1, read_file2):
    titlelist = []
    blaststring = ""
    blastfile = read_file1.readlines()
    taxfile = read_file2.read().splitlines()
    read_file1.close()
    read_file2.close()
    
    while blastfile:
        try: 
            tax_ID = blastfile[5].split("\t")[12]
        except IndexError:
            tax_ID = 1
        del blastfile[0]
        try:
            reg_hit = re.search("# BLASTN .*[0-9]\+\\n", blaststring.join(blastfile))
            BLASTend = (int(blastfile.index(reg_hit.group())))
        except AttributeError:
            for item in blastfile:
                if 'BLAST' in item:
                    BLASTend = int(blastfile.index(item)) + 1
        if str(tax_ID) in taxfile:
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
    titlelist = set()
    blastfile = read_file1.readlines()
    taxfile = read_file2.read().splitlines()
    read_file1.close()
    read_file2.close()
    while blastfile:
        try: 
            tax_ID = blastfile[0].split("\t")[12].split(";")[0].split("\n")[0]
        except IndexError:
            tax_ID = "1"
            print ("ex")
        if tax_ID in taxfile:
            titlelist.add(blastfile[0].split("\t")[0])
        del blastfile[0]

         
    return titlelist
        
def find_sequences(read_file3, titlelist, filterfile):
    new =[]
    for s in SeqIO.parse(read_file3, "fasta"):
        if s.id in titlelist:
            new.append(s)
    SeqIO.write(new, filterfile, "fasta")
    
def main(argv):
    blastfile, taxafile, chunkfile, filterfile, filetype = command(argv)
    read_file1, read_file2, read_file3 = open_files(blastfile, taxafile, chunkfile)
    if filetype == "BLASTn":
        titlelist = find_taxa_blastn(read_file1, read_file2)
    if filetype == "BLASTx":
        titlelist = find_taxa_blastx(read_file1, read_file2)
    find_sequences(read_file3, titlelist, filterfile)
    
if __name__ == "__main__":
   main(sys.argv[1:])

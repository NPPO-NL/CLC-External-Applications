#!/usr/bin/env python

"""
Written by Lucas van der Gouw
30-4-2018
This script reads a BLASTN hit table and compares the tax_id of the top hit with 
a list of tax_ids and filters the BLASTN results.
"""

import sys, getopt

def command(argv):
    '''
    Get values for necessary parameters
    :param argv:
    :return: blastfile: path to BLAST table, taxafile: path to file with taxanomy numbers,
    combofile: path to BLAST table with the selected organism, filterfile: path to BLAST table without the selected organism
    '''
   blastfile = ''
   taxafile = ''
   combofile = ''
   filterfile = ''
   try:
      opts, args = getopt.getopt(argv,"hb:t:o:u:",["blastfile=","taxafile=","out1=","out2="])
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
    if opt in ("-o", "--number"):
        combofile = arg
    if opt in ("-u", "--minimum"):
        filterfile = arg
   return blastfile, taxafile, combofile, filterfile

def open_files(blastfile, taxafile):
    '''
    Open blastfile and taxafile
    :param blastfile: path to BLAST table
    :param taxafile: path to file with taxanomy numbers
    :return: read_file1 = open blastfile, read_file2 = open taxafile
    '''
    read_file1 = open(blastfile,"r")
    read_file2 = open(taxafile,"r")

    return read_file1, read_file2

def find_taxa(read_file1, read_file2):
    '''
    Check taxonomic ID of first hit of a query with taxanomy numbers in taxanumbers.
    If match > add whole BLAST table hit to filterstring. If not, add to combostring.
    :param read_file1: open blastfile
    :param read_file2: open taxafile
    :return: filterstring: string with all BLAST hits from a specific taxonomy, combostring: string with all BLAST hits excluding a specific taxonomy
    '''
    blastfile = read_file1.readlines()
    taxfile = read_file2.readlines()
    read_file1.close()
    read_file2.close()
    filterstring = ''
    combostring = ''
    while blastfile:
        try: 
            tax_ID = blastfile[5].split("\t")[12]
        except IndexError:
            tax_ID = 1
        del blastfile[0]
        try:
            BLASTend = int(blastfile.index('# BLASTN 2.6.0+\n'))
        except ValueError:
            for item in blastfile:
                if 'BLAST' in item:
                    BLASTend = int(blastfile.index(item)) + 1
        if str(tax_ID) + "\n" in taxfile:
            filterstring += '# BLASTN 2.6.0+\n'
            for item in blastfile[0:BLASTend]:
                filterstring += item
                del blastfile[0]     
        else:
            combostring += '# BLASTN 2.6.0+\n'
            for item in blastfile[0:BLASTend]:
                combostring += item
                del blastfile[0]
                
    return filterstring, combostring

def writefile(filterstring, combostring, filterfile, combofile):
    '''
    Write sequences to file
    :param filterstring: string with all BLAST hits from a specific taxonomy
    :param combostring: string with all BLAST hits excluding a specific taxonomy
    :param filterfile: path to BLAST table without the selected organism
    :param combofile: path to BLAST table with the selected organism
    :return:
    '''
    write_file1 = open(filterfile, "w")
    write_file2 = open(combofile, "w")
    write_file1.write(filterstring)
    write_file2.write(combostring)
    write_file1.close()
    write_file2.close()
    
def main(argv):
    blastfile, taxafile, combofile, filterfile = command(argv)
    read_file1, read_file2 = open_files(blastfile, taxafile)
    filterstring, combostring = find_taxa(read_file1, read_file2)
    writefile(filterstring, combostring, filterfile, combofile)
    
if __name__ == "__main__":
   main(sys.argv[1:])

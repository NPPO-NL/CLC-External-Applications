# CEA007_BLASTn_taxonomy_sorter

This script is written in python 3.x
This script reads a BLASTN hit table and compares the tax_id of the top hit with 
a list of tax_ids and filters the BLASTN results.

required packages: sys, getopt

parameters:
blastfile: path to BLAST table, taxafile: path to file with taxanomy numbers,
combofile: path to BLAST table with the selected organism, filterfile: path to BLAST table without the selected organism

While in the directory of the script:
./CEA003_chunk_ file_v2.1.py -i <blastfile> -o <taxafile> -n <combofile> -m <filterfile>

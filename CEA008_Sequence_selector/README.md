# CEA008_Sequence_selector

This script is written in python 3.x
This script reads a BLASTN hit table and compares the tax_id of the top hit with 
a list of tax_ids and filters the BLASTN results.

required packages: sys, getopt, biopython

parameters:
blastfile: Path to BLAST table, taxafile: path to file with taxanomy numbers,
chunkfile: Path to .fasta with sequences, filterfile: Path to output, filetype: number to determane BLASTn or BLASTx input

While in the directory of the script:
./CEA008_select_sequences_based_on_taxon_ID.py -b <blastfile> -t <taxafile> -c <chunkfile> -u <filterfile> -y <filetype>

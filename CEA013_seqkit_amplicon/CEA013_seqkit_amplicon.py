#!/usr/bin/env python

"""
Code written by: Bas Berbers
Function: This script detects an amplicon within a fasta based on the given primers. Due to the limitations of seqkit
it will always search for the biggest possible amplicon per contig.
Publication date: 02-08-2023
Update date: 22-04-2025
Version: v1.1
Usage: python3 /MolbioDataDrive/Scripts/CEA013_seqkit_amplicon.py {input} {name} {forward} {reverse} {mismatch} {trim} {output}
"""

import argparse
import os

def calculate_primer_lengths(forward_primer, reverse_primer):
    forward_length = len(forward_primer) + 1
    reverse_length = -abs(len(reverse_primer) + 1)
    trim_string = f"{forward_length}:{reverse_length}"
    return trim_string

def generate_dummy_fasta(fasta_filename):
    dummy_data = ">dummy_sequence\n" \
                 "ATCGATCGATCG"

    with open(fasta_filename, 'w') as fasta_file:
        fasta_file.write(dummy_data)

def detect_amplicon_and_blast(args):
    forward_primer = str(args.forward)
    reverse_primer = str(args.reverse)

    if args.trim == "YES":
        trim = calculate_primer_lengths(forward_primer, reverse_primer)
        cmd_seqkit = f"cat {args.input} | /MolbioDataDrive/Scripts/seqkit amplicon -F {forward_primer} " \
          f"-R {reverse_primer} -m {args.mismatch} -r {trim} -o {args.output_fa} > /dev/null 2>&1"
    else:
        cmd_seqkit = f"cat {args.input} | /MolbioDataDrive/Scripts/seqkit amplicon -F {forward_primer} " \
              f"-R {reverse_primer} -m {args.mismatch} -o {args.output_fa} > /dev/null 2>&1"
    os.system(cmd_seqkit)
    fasta_filename = str(args.output_fa)
    print(fasta_filename)
    try:
        with open(fasta_filename, "r") as fasta_file:
            content = fasta_file.read()
            if content.strip() == "":
                raise FileNotFoundError
            print("FASTA file already exists.")
    except FileNotFoundError:
        print("Dummy test.")
        generate_dummy_fasta(fasta_filename)

    # # Check if sequences meet the minimum bp requirement
    # from Bio import SeqIO
    # sequences = list(SeqIO.parse(fasta_filename, "fasta"))
    # long_enough = any(len(record.seq) >= min_bp for record in sequences)
    #
    # if not long_enough:
    #     print(f"No sequences longer than {min_bp} bp. Skipping output.")
    #     return

    temp = str(os.getcwd() + "/temp.txt")
    print(temp)
    # perform a blast with the amplicon detected to get its location in a format that can be converted to a gff
    cmd_blast = f"/Databases/ncbi-blast-2.13.0+/bin/blastn -query {args.input} -task megablast " \
                f"-max_hsps 1 -max_target_seqs 1 " \
                f"-perc_identity 100 -out {temp} -subject {fasta_filename} " \
                f"-outfmt '7 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore staxids ssciname'"
    os.system(cmd_blast)
    print(cmd_blast)
    cmd_gff = f"python3 /MolbioDataDrive/Scripts/CEA012_BLASTn_to_gff.py {temp} {args.name} 1 {args.output_annot}"
    os.system(cmd_gff)
    print(cmd_gff)

    os.system(f"rm {temp}")

    # Filter GFF to ensure the first column matches the NAME= attribute
    with open(args.output_annot, 'r') as infile:
        lines = infile.readlines()

    with open(args.output_annot, 'w') as outfile:
        for line in lines:
            if line.startswith("#") or line.strip() == "":
                outfile.write(line)
                continue
            columns = line.strip().split('\t')
            if len(columns) < 9:
                continue  # skip malformed lines
            seqid = columns[0]
            attributes = columns[8]
            for attr in attributes.split(';'):
                if attr.startswith("NAME="):
                    name_value = attr.split("=")[1]
                    if name_value.strip() == seqid.strip():
                        outfile.write(line)
                    break
def main():
    parser = argparse.ArgumentParser(description="Amplicon detection using Seqkit.")
    parser.add_argument("input", help="Input file containing fasta where amplicon will be detected.")
    parser.add_argument("name", help="user fills in name of primers here so that it can be parsed")
    parser.add_argument("forward", help="user fills in forward primer here")
    parser.add_argument("reverse", help="user fills in reverse primer here")
    parser.add_argument("mismatch", help="Value for amount of mismatches allowed. default is 0")
#    parser.add_argument("min_bp", help="Minimum bp length for filtering amplicons. default is 30")
    parser.add_argument("trim", help="trim the primer sequence from the amplicon. default is YES")
    parser.add_argument("output_fa", help="Output FASTA file.")
    parser.add_argument("output_annot", help="Output gff file.")
    args = parser.parse_args()

    detect_amplicon_and_blast(args)

if __name__ == "__main__":
    main()


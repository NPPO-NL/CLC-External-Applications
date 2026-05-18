#!/usr/bin/env python

"""
Code written by: Bas Berbers
Function: This script reads a BLASTN hit table in outfmt7 format and converts the top hits to a gff3 file
based on how many top hits per query the user wants to convert from blast output
Publication date: 14-12-2022
Version: v1.0
Usage: python3 /MolbioDataDrive/Scripts/CEA012_BLASTn_to_gff.py {blast} {type} {tophits} {output}
"""

import argparse

def read_blast_file(filename):
    with open(filename, "r") as read_file:
        blastfile = read_file.readlines()
    return blastfile

def split_blast_queries(blastfile):
    blast_query = []
    del blastfile[0]  # Remove the header line
    while blastfile:
        try:
            BLASTend = [idx for idx, s in enumerate(blastfile) if '# BLAST' in s][0]
            blast_query.append(blastfile[:BLASTend])
            blastfile = blastfile[BLASTend + 1:]
        except IndexError:
            BLASTend = len(blastfile)
            blast_query.append(blastfile[:BLASTend])
            blastfile = blastfile[BLASTend + 1:]
    return blast_query

def parse_query_data(query, parameter, input_string):
    data_list = []
    counter = 0
    while counter < parameter:
        try:
            seqid = query[4].split("\t")[0]
            source = "BLAST"
            type = input_string
            start_feature = query[4].split("\t")[6]
            end_feature = query[4].split("\t")[7]
            score = query[4].split("\t")[10]
            phase = "."
            attributes1 = query[4].split("\t")[13].strip()
            attributes2 = query[4].split("\t")[12]
            attributes3 = query[4].split("\t")[2]
            attributes4 = query[4].split("\t")[3]
            attributes5 = query[4].split("\t")[11]
            temp_att = query[4].split("\t")[1]
            attributes6 = temp_att.split("|")[3] if "|" in temp_att else temp_att
            attributes7 = query[4].split("\t")[8]
            attributes8 = query[4].split("\t")[9]
            strand = "+" if attributes7 < attributes8 else "-"
            attributes = "subject_sci_name=" + attributes1 + ";taxid=" + attributes2 + ";perc_identity=" + attributes3 + \
                         ";alignment_length=" + attributes4 + ";subject_start=" + attributes7 + ";subject_end=" + attributes8 + \
                         ";bit_score=" + attributes5 + ";NAME=" + attributes6
            data = [seqid, source, type, start_feature, end_feature, score, strand, phase, attributes]
            data_list.append(data)
            counter += 1
            del query[0]
        except IndexError:
            break
    return data_list

def write_to_gff_file(data_list, output_filename):
    with open(output_filename, 'w') as file:
        for tophit in data_list:
            file.writelines('\t'.join(tophit) + '\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("blast", help="input file of blast in outfmt 7 format")
    parser.add_argument("type", help="indicate what you are annotating, default is custom")
    parser.add_argument("tophits", help="choose amount of top matching subjects to annotate per query in gff file")
    parser.add_argument("output", help="name of gff output file")
    args = parser.parse_args()

    blastfile = read_blast_file(args.blast)
    blast_query = split_blast_queries(blastfile)
    parameter = int(args.tophits)
    input_string = str(args.type)
    data_list = []

    for query in blast_query:
        data_list.extend(parse_query_data(query, parameter, input_string))

    write_to_gff_file(data_list, args.output)

if __name__ == "__main__":
    main()

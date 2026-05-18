#!/usr/bin/env python

"""
Code written by: Bas Berbers
Function: This script merges two text files
Publication date: 
Version: v1.0
Usage: python3 /MolbioDataDrive/Scripts/CEA015_merge_text_tables.py {table1} {table2} {output_file}
"""

import argparse

def cat_tables(table1, table2, output_file):
    with open(table1, 'r') as file1, open(table2, 'r') as file2, open(output_file, 'w') as outfile:
        content1 = file1.read()
        content2 = file2.read()
        # merging of the 2 text files
        concatenated_content = content1 + content2
        outfile.write(concatenated_content)

def main():
    parser = argparse.ArgumentParser(description='Concatenate contents of two tables.')
    parser.add_argument('table1', help='Path to the first table')
    parser.add_argument('table2', help='Path to the second table')
    parser.add_argument('output_file', help='Path to the output file')
    args = parser.parse_args()

    try:
        cat_tables(args.table1, args.table2, args.output_file)
    except FileNotFoundError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
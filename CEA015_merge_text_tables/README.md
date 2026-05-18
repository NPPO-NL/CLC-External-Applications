# CEA015_merge_text_tables

## 1.	Description
This CEA merges two text filesby using Python3 to read and join the files. The 2nd file will always be put on a new line. It can be used on any text file, but in NIVIP this CEA is mostly used in CLC workflows to join annotation files (.gff). In CLC there is no possibility to allow variable amount of inputs, therefore if more than 2 text files need to merged the CEA has to be invoked multiple times consecutively.

## 2.	Version
CEA015_merge_text_tables_V1.0

## 3.	Front-end
### 3.1 	Input
CEA15 expects two text files.
example:

### 3.2 	Output
The output will be a merged file of the two input files:

### 3.3 	Adjustable parameters
There are no adjustable parameters

## 4.	Back-end
### 4.1 	Terminal execution
python3 /path/to/CEA015_merge_text_tables.py {file1} {file2} {output}

### 4.2 	Requirements
python3

### 4.3 	Script
Python 3 and makes use of argparse.

## 6.		Research and validation
2024.molbio.001-003
	
## 7. 	References
N/A
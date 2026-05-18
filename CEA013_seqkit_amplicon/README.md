# CEA013_seqkit_amplicon

## 1.	Description
This Python script is developped for amplicon detection using the Seqkit and BLAST tool. The script generates amplicon sequences using Seqkit, then performs a BLAST analysis to determine the location of the amplicon in the original sequence and converts this BLAST output to an annotation file (.gff). If no amplicon can be detected, a dummy sequence is generated so that CLC workflows will not crash. 

## 2.	Version
CEA013_seqkit_amplicon_V1.0

## 3.	Front-end
### 3.1 	Input
It takes user-provided forward and reverse primer sequences, an input FASTA file, and additional parameters such as the allowed number of mismatches and whether to trim the primer sequence from the amplicon. 

### 3.2 	Output
A fasta file with only the detected amplicon and an annotation file (.gff) with the location of the amplicon on the input fasta file.

### 3.3 	Adjustable parameters
The allowed number of mismatches in the alignment between the primer sequences and the input fasta file. The possibility to trim the primer sequences from the detected amplicon. And the name of the amplicon.

## 4.	Back-end
### 4.1 	Terminal execution
python3 /path/to//CEA013_updated.py {input} {name} {forward} {reverse} {mismatch} {trim} {output_fa} {output_annot}

### 4.2 	Requirements
installing Seqkit, BLAST and python

### 4.3 	Script
python

## 5.		Research and validation
2024molbio001-01 
	
## 6. 	References

W Shen, S Le, Y Li*, F Hu*. SeqKit: a cross-platform and ultrafast toolkit for FASTA/Q file manipulation. PLOS ONE. doi:10.1371/journal.pone.0163962.

https://github.com/shenwei356/seqkit

A. Morgulis, G. Coulouris, Y. Raytselis, T.L. Madden, R. Agarwala & A.A. Schaffer (2008). Database Indexing for Production MegaBLAST Searches. Bioinformatics 24:1757-1764.

BLAST® Command Line Applications User Manual  	
https://www.ncbi.nlm.nih.gov/books/NBK279690/

BLAST® Help 	
https://www.ncbi.nlm.nih.gov/books/NBK1762/

NCBI FTP server  	
ftp://ftp.ncbi.nlm.nih.gov/blast/db/
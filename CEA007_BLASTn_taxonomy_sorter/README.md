# CEA007_BLASTn_taxonomy_sorter

## 1. Description
   CEA007_BLASTn_taxonomy_sorter processes the hit table from BLASTn and divides the blast results based on a taxID list. The blast results are either placed in a blast table "taxafiltered_BLASTn" or "nonfiltered_BLASTn." If the taxID of the best hit of a query matches the predefined taxID list, the entire query is written to the "taxafiltered_BLASTn" file.

## 2. Version
   CEA007_BLASTn_taxonomie_sorter_v1.2

## 3. Front-end
### 3.1 Input
        CEA007_BLASTn_taxonomy_sorter expects a hit table from BLASTn.

### 3.2 Output
        CEA007_BLASTn_taxonomie_sorter produces 2 BLASTn hit tables: one with all queries classified via the taxID list and one with all queries from the rest.

### 3.3 Configurable Parameters
        The parameters used for CEA007 are described in Table 1.

_Table 1: Configurable parameters for CEA007, as entered in the command (script), and how it appears in CLC for the user (CLC). The CLC input/output settings represent what CLC fills in the command for the parameters in the background._


| script | CLC | description | CLC Input/output settings |
|--------|-----|-------------|---------------------------|
| -b     | BLASTn file       | The file created by CEA001_BLASTn | User selected input data (CLC data location) – Plain text(.txt/.text) |
| -t     | taxon to filter on | drop down menu with taxa to select for filtering | Csv enumerator - Viridiplantea |
| -o     | Storage window | The path where the non-filtered file is stored. | User-selected input data (CLC data location) – text(.txt/.text) - non_filtered_BLASTn |
| -u     | In taxa list | The path where the filtered file is stored. The filename is standard taxa_filtered_BLASTn. | User-selected input data (CLC data location) – text(.txt/.text) - taxa_filtered_BLASTn. |


## 4. Back-end
### 4.1 Terminal Execution
   ```
   /path/to/CEA007_BLASTn_taxonomy_sorter_v1.2.py -b {BLASTn file} -t {taxon to sort on} -o {not in taxa list} -u {in taxa list}
   ```
### 4.2 Requirements
        TaxID list (available via the NCBI web server) is essential for the script to work. The CEA works in Python 3 and uses biopython 1.74. Could work with newer versions, but is not tested.

### 4.3 Script
        First-party Python script.

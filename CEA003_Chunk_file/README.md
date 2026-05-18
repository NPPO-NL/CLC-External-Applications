# CEA003_Chunk_file

## 1. Description
   The Chunk_file algorithm is developed to chop long DNA sequences of 
   assembled contigs and scaffolds into pieces. This can be used, for example, 
   in a blast analysis to ensure that a blast hit can be obtained for each 
   predefined length. In this way, misassembled long contigs can yield multiple 
   hits with potentially different organisms. Additionally, the CEA can be 
   used as a minimum length filter.

## 2. Version
   CEA003_Chunk_file_v2.1

## 3. Front-end
### 3.1 Input
    CEA003_Chunk_file expects a file with nucleotide sequences in fasta format 
    (*.fa, *.fas, *.fasta, etc.), as obtained after generating an assembly or 
    consensus sequence.

### 3.2 Output
        CEA003_Chunk_file produces a file with nucleotide sequences in fasta format (*.fa, *.fas, *.fasta, etc.).

### 3.3 Configurable Parameters
        The parameters used for CEA003 are described in Table 1. Figure 1 shows how the CLC user sees the parameters.

   _Table 1: Configurable parameters for CEA003, as entered in the command (script), and how it appears in CLC for the user (CLC). The CLC input/output settings represent what CLC fills in the command for the parameters in the background._
   
| Command line | CLC     | description                                                                                                                                   | CLC Input/output settings |
|--------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| -i | in      | select the input file                                                                                                                               | User-selected input data(CLC data location) – FASTA(.fa/.fsa/.fasa) |
| -n     | maximum chunk length                                                                                                                                | the maximum length the sequences should be. Default value=1,000     | *Integer* - 1000 |
| -m     | minimum chunk length                                                                                                                                | the minimum length the sequences should be. Default value=50        | *Integer* - 50   |
| -o   | Storage window | Select the path where the output is stored. | The filename is standard BLASTn_result.txt, Output file from CLC - FASTA(.fa/.fsa/.fasa) - _chunked.fasa |

## 4. Back-end
### 4.1 Terminal Execution
   
   `/path/to/CEA003_Chunk_file_v2.1.py -i {in} -o {out} -n {maximum chunk length} -m {minimum chunk length}`

### 4.2 Requirements
        The script uses Python 3 and BioPython v1.74.

### 4.3 Script
        First-party Python script.

## 5. References
   BioPython: [http://biopython.org/](http://biopython.org/)

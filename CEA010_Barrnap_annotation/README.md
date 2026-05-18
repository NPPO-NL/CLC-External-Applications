

1. **Description**
   Barrnap is a third-party application that enables the detection and annotation of ribosomal DNA from a fasta sequence. To use this tool in CLC, a Python script has been written to pass arguments to the command line application. The application accepts a multi-record ribosomal fasta file and then executes Barrnap to annotate it.

2. **Version**
   CEA010_Barrnap_annotation_v1.0  
   Contains: Barrnap_v0.9

3. **Front-end**
   3.1 **Input**
      A multi-fasta file with Ribosomal DNA sequences.

   3.2 **Output**
      A multi-record GFF file with all detected annotated Ribosomal genes.

   3.3 **Configurable Parameters**
      The parameters used for CEA010 are described in Table 1.

      Table 1: Configurable parameters for CEA010, as entered in the command (script), and how it appears in CLC for the user (CLC). The CLC input/output settings represent what CLC fills in the command for the parameters in the background.
      
| script | CLC     | Description                                                                             | CLC Input/output settings                                        |
|--------|---------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| {1}    | Input   | Ribosomal DNA fasta file                                                                | FASTA (.fa/.fsa/.fasta)                                          |
| {2}    | Output  | GFF export                                                                              | Plain Text (.txt/.text) Output file from CL Default: “_gff”      |
| {3}    | Kingdom | Kingdom dropdown menu for selecting Archaea, Bacteria, Eukaryota, Metazoan_Mitochondria | Csv enumirator: Archaea,Bacteria,Eukaryota,Metazoan_Mitochondria 
    

4. **Back-end**
   4.1 **Terminal execution**
      Bash command:
      ```
      /bin/bash -c '/path/to/CEA010_Barrnap_annotation.py {input} {output} {kingdom}'
      ```

      Python Barrnap call:
      ```
      os.system("barrnap --kingdom {} {} > {}".format(arguments.kingdom, arguments.input, arguments.output))
      ```

   4.2 **Requirements**
      Default Python Anaconda 3.8.3 installation or `conda install -c bioconda barrnap`.

   4.3 **Script**
      CEA010 consists of a first-party Python script that invokes a third-party Perl script. The Python script and any previous versions can be found in our Labcloud molbiostorage drive: X:\3.Scripts_pipelines\Scripts\CEA010\

5. **Research and Validation**
   - 2020.molbio.001-06 CEA010_Barrnap_annotation
   - 2019.molbio.007 Validation Nematode pipeline

6. **References**
   - GitHub - tseemann/barrnap: Bacterial ribosomal RNA predictor

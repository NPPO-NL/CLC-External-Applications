**Translation:**

1. **Description**
   Mitos is a third-party pipeline that enables the detection and annotation of mitochondrial DNA from a fasta sequence de novo. To use this tool in CLC, a "data handler" has been built around it in Python and Bash scripts. The "data handler" accepts a multi-record mitochondrial fasta file and executes a Mitos run for each fasta record. The GFF output files from the runs are merged and converted into a Genbank file. The latter is performed by CEA011, but CEA009 passes the files and executes CEA011.

2. **Version**
   CEA009_Mitos_annotation_gbk_v1.1  
   Contains: Mitos_v1.0.5

3. **Front-end**
   3.1 **Input**
      A multi-fasta file with Mitochondrial DNA sequences.

   3.2 **Output**
      A multi-record Genbank file with all annotated Mitochondrial genes.

   3.3 **Configurable Parameters**
      The parameters used for CEA009 are described in Table 1.

      Table 1: Configurable parameters for CEA009, as entered in the command (bash command), and how it appears in CLC for the user (CLC). The CLC input/output settings represent what CLC fills in the command for the parameters in the background.

 | \| bash command | \| CLC                 | \| Description                                                                                     | \| CLC Input/output settings                                                  | \| |
|-----------------|------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|----|
| \| {$1}         | \| fasta               | \| Multi-fasta input file                                                                          | \| User - selected input data (CLC data location) – FASTA(.fa/.fsa/.fasta) \| |    |
| \| {$2}         | \| translational_table | \| Species translation tables. Options include                                                     |                                                                               |    |
|                 |                        | 1. The Standard Code,                                                                              |                                                                               |    |
|                 |                        | 2. The Vertebrate Mitochondrial Code,                                                              |                                                                               |    |
|                 |                        | 3. The Yeast Mitochondrial Code,                                                                   |                                                                               |    |
|                 |                        | 4. The Mold and Protozoan and Coelenterate Mitochondrial Code and the Mycoplasma/Spiroplasma Code, |                                                                               |    |
|                 |                        | 5. The Invertebrate Mitochondrial Code,                                                            |                                                                               |    |
|                 |                        | 6. The Ciliate and Dasycladacean and Hexamita Nuclear Code,                                        |                                                                               |    |
|                 |                        | 9. The Echinoderm and Flatworm Mitochondrial Code,                                                 |                                                                               |    |
|                 |                        | 10. The Euplotid Nuclear Code,                                                                     |                                                                               |    |
|                 |                        | 11. The Bacterial and Archaeal and Plant Plastid Code,                                             |                                                                               |    |
|                 |                        | 12. The Alternative Yeast Nuclear Code,                                                            |                                                                               |    |
|                 |                        | 13. The Ascidian Mitochondrial Code,                                                               |                                                                               |    |
|                 |                        | 14. The Alternative Flatworm Mitochondrial Code,                                                   |                                                                               |    |
|                 |                        | 16. Chlorophycean Mitochondrial Code,                                                              |                                                                               |    |
|                 |                        | 21. Trematode Mitochondrial Code,                                                                  |                                                                               |    |
|                 |                        | 22. Scenedesmus obliquus Mitochondrial Code,                                                       |                                                                               |    |
|                 |                        | 23. Thraustochytrium Mitochondrial Code,                                                           |                                                                               |    |
|                 |                        | 24. Rhabdopleuridae Mitochondrial Code,                                                            |                                                                               |    |
|                 |                        | 25. Candidate Division SR1 and Gracilibacteria Code,                                               |                                                                               |    |
|                 |                        | 26. Pachysolen tannophilus Nuclear Code,                                                           |                                                                               |    |
|                 |                        | 27. Karyorelict Nuclear Code,                                                                      |                                                                               |    |
|                 |                        | 28. Condylostoma Nuclear Code,                                                                     |                                                                               |    |
|                 |                        | 29. Mesodinium Nuclear Code,                                                                       |                                                                               |    |
|                 |                        | 30. Peritrich Nuclear Code,                                                                        |                                                                               |    |
|                 |                        | 31. Blastocrithidia Nuclear Code,                                                                  |                                                                               |    |
|                 | \|                     | 33. Cephalodiscidae Mitochondrial UAA-Tyr Code                                                     |                                                                               |    |
| \| {$3}         | \| Storage window      | \| The path where the output is stored.                                                            | \| Output file from CLC – _gbk.genbank                                        |    |
      


4. **Back-end**
   4.1 **Terminal execution**
      Bash command
      ```
      /bin/bash -c 'source /etc/environment; /path/to/mitos_gbk_V1.2 {fasta} {translational_table} {gbk-output}'
      ```

      Python command run for Mitos
      ```
      os.system("{}runmitos.py -i {} -c {} -o {} -r {}".format(mitos_install, fasta, genetic_table, mitos_output, reference))
      ```

   4.2 **Requirements**
      Important requirements for Mitos to function include Python version 2.7 and Biopython v1.73. These and other requirements are included in a conda environment.

      Conda installation to create a conda environment with the command:
      ```
      conda create -n MITOS -c bioconda -c conda-forge -c default 'MITOS=1.0.5' 'r-base=3.5.1'
      ```

      A text file with all tools in this conda environment can be found on the Labcloud molbiostorage drive: X:\3.Scripts_pipelines\Scripts\CEA009\mitos_env.txt

      Mitos download from GitHub page: https://gitlab.com/Bernt/MITOS

   4.3 **Script**
      CEA009 consists of several components: a bash script that invokes a "Mitos handler," a Mitos handler that calls the Mitos pipeline, and then calls CEA011. This script and previous versions can be found in our Labcloud molbiostorage drive: X:\3.Scripts_pipelines\Scripts\CEA009\

      Bash script: A first-party script.
      Mitos handler: A first-party Python script.
      Mitos pipeline: Set of third-party Python scripts.

5. **Changes Compared to Previous Version**
   1. Mitos version from v1.0 to v1.1.
   2. CEA009 Python script is modified in the way it calls Python. Previously, it called Python from the Linux system, but now it calls it from the conda environment so that system updates cannot affect the functioning of CEA009.
   3. Additional information added about conda environment.

6. **Research and Validation**
   - 2020.molbio.001-05 CEA009_ Mitos_annotation
   - 2020.molbio.001-07 CEA011_gff_to_gbk
   - 2019.molbio.007 Validation Nematode pipeline

7. **References**
   - Mitos: https://gitlab.com/Bernt/MITOS



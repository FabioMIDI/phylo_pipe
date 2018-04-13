# phylo_pipe
A pipeline to perform phylogenesis from protein sequences

# OPERATIVE SYSTEM

The pipeline is designed on Ubuntu 14.04 LTS, and was only tested on this Linux distribution.

# DESCRIPTION

phylo_pipe is a pipeline to perform phylogenesis from protein sequences. 

It combines softwares and scripts in the order below:

1-orthofinder ------> standalone software, find orthologus from protein, more info here: https://github.com/davidemms/OrthoFinder
2-read_ortho_out.py ---> create p/a matrix, multifastas of single copy orthologs (SCO)
3-muscle_batchrun.py -----------> aligns single copy orthogroups with Muscle
4-phi_batchrun.py [optional]---------> perform test for recombination with Phi; recombining SCO are discarded
5-gblock_batchrun.py -----------> perform Gblocks on each alignment to remove not informative sites
6-orthos2cat.py--------> concatenate gblocked multialigned SCO into one file

The final output is obtained from orthos2cat.py and is a concatenated Multiple Single Alignment (MSA) combining all not recombinant single copy orthologs gblocked MSAs. This file can be used as input for a phylogenetic software such as FastTree or RaxML. A temp folder includes every output for each software 1-5.

# WARNINGS

The file name of each protein mutifasta will be the one appearing in the phylogenetic tree; change it accordingly.
Anyway, the file name must be no longer than 60 characters and it mustn't end with "a" (ex: "Midichloria.faa" it's not fine, it should be converted in Midichlori.faa or something else without "a" as the last character) 

When performing the pipeline on a reduced number of taxa (~less than 3/4) and/or on taxa with short proteins, Phi may not be able to work; the pipeline will continue skipping this step and printing a WARNING. 

# REQUIREMENTS

The following softwares must be installed for the pipeline to work: Blast+, MCL
And the following python modules: python-dev, pandas, numpy, biopython.
How to install from the terminal:
Blast+, MCL -----> "sudo apt-get install [software name]" 
python-dev, pandas, numpy, biopython -----> "sudo apt-get install python-[name of module]" (python-dev is a requirement for all other modules, install it first)

# HOW TO RUN

Full manual from the terminal: "python phylo_pipe.py -h"

The pipeline must be run inside its folder.
Once you're inside the folder, from the terminal: 
"python phylo_pipe.py -i [input_folder] -t [number_of_threads] {-r} -p [Phi_test]"

see the description below:

-i -----> MANDATORY, folder containing one protein multifasta for each organism, you have to specifies the folder's path
-t -----> MANDATORY, number of threads depending of your PC, more is faster
-r -----> OPTIONAL, remove temp folder: if -r is specificed it will remove the temp folder. If it is not present it will keep it.
-p -----> OPTIONAL, if -p True is specified it will run Phi test. If it is not present it will skip this step.

Examples: 
Run the pipeline with 11 threads, does NOT remove the temp folder, perform Phi test
"python phylo_pipe.py -i fasta_folder -t 11 -p True"

Run the pipeline with 11 threads, remove the temp folder, perform Phi test
"python phylo_pipe.py -i fasta_folder -t 11 -r -p True"

Run the pipeline with 8 threads, remove the temp folder, do not perform Phi test
"python phylo_pipe.py -i fasta_folder -t 8 -r"

# OUTPUT

output files will be in the multifastas folder (input_folder as described in 4.) and will be the following:

- orthos2cat_out; the main output of the pipeline (described in 1.)
- [OPTIONAL] temp; temporary files folder (if multiple analyses are run; each one will have a temp folder with a progressive number -e.g. temp, temp_1, temp_2 etc. - ) containing the output of all softwares and scripts componing the pipeline.


The process may require some time, depending of your hardware specifics and number of taxa/number of proteins per taxon. 

# TEST 

You can test the pipeline with the "test" folder, which contains a trial dataset of multifastas.

Run the pipeline with "test" folder
"python phylo_pipe.py -i test -t 11 -p True"

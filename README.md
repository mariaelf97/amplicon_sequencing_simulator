# Snakemake workflow: `Amplicon Read Simulator`

[![Snakemake](https://img.shields.io/badge/snakemake-≥6.3.0-brightgreen.svg)](https://snakemake.github.io)
[![GitHub actions status](https://github.com/<owner>/<repo>/workflows/Tests/badge.svg?branch=main)](https://github.com/mariaelf97/amplicon_sequencing_simulator/actions?query=branch%3Amain+workflow%3ATests)


A Snakemake workflow for Amplicon read simulation for waste water sequencing or other aplications. Users can easily simulate reads from mutiple samples with different proportions using this pipeline.


## Usage

The usage of this workflow is described in the [Snakemake Workflow Catalog](https://snakemake.github.io/snakemake-workflow-catalog/?usage=<owner>%2F<repo>).

If you use this workflow in a paper, don't forget to give credits to the authors by citing the URL of this (original) <https://github.com/mariaelf97/amplicon_sequencing_simulator> repository and its DOI (see above).

# Steps
* Clone the git repository and change the working directory `cd amplicon_sequencing_simulator`
* Install snakemake `conda create -n snakemake bioconda::snakemake`
* Run the wrapper using `python workflow/scripts/amplicon_simulator_wrapper.py -s sample1,sample2 -sp path_to_sample1,path_to_sample2 -pr sample1_proportion,sample2_proportion(e.g. 0.2,0.8) -p path_to_primer_bed_file -n total_number_of_reads -o path_to_output_directory`
* Please remember that the primer file must contain a column containing primer sequence. Please note that maximum mismatch allowed for each primer sequence is 1 SNP.
* To learn more about how to adjust other parameters use `python workflow/scripts/amplicon_simulator_wrapper.py --help`
* The final outputs will be located at `provided_output_path/results'. Simulated reads from all samples are located in `provided_output_path/results/merged_reads.fastq'
* Once you run the pipeline, it will create a config.yaml file in your current working directory that contains information about all the parameters used in the simulation.

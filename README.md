# Snakemake workflow: `Amplicon Read Simulator`

[![Snakemake](https://img.shields.io/badge/snakemake-≥6.3.0-brightgreen.svg)](https://snakemake.github.io)
[![GitHub actions status](https://github.com/mariaelf97/amplicon_sequencing_simulator/workflows/Tests/badge.svg?branch=main)](https://github.com/mariaelf97/amplicon_sequencing_simulator/actions?query=branch%3Amain+workflow%3ATests)


A Snakemake workflow for Amplicon read simulation for waste water sequencing or other aplications. Users can easily simulate reads from mutiple samples with different proportions using the additional wrapper provided in the reporsitory or just use the pipeline by adjusting the config file located in `config/config.yaml` with their desired input, output and simulation parameters.


## Usage

The usage of this workflow is described in the [Snakemake Workflow Catalog](https://snakemake.github.io/snakemake-workflow-catalog/?usage=<owner>%2F<repo>).

If you use this workflow in a paper, don't forget to give credits to the authors by citing the URL of this (original) <https://github.com/mariaelf97/amplicon_sequencing_simulator> repository and its DOI (see above).

# Steps
* Clone the git repository and change the working directory `cd amplicon_sequencing_simulator/`
* Install snakemake `conda create -n snakemake bioconda::snakemake`
* Run the wrapper using
 ```
 python workflow/scripts/amplicon_simulator_wrapper.py -s sample1,sample2 -sp path_to_sample1,path_to_sample2 -pr sample1_proportion,sample2_proportion(e.g. 0.2,0.8) -p path_to_primer_bed_file -n total_number_of_reads -o path_to_output_directory
 ```
* Please remember that the primer file must contain a column containing primer sequence. The maximum mismatches allowed for each primer sequence is 1 SNP.
* To learn more about how to adjust other parameters use `python workflow/scripts/amplicon_simulator_wrapper.py --help`
* The final outputs will be located at `provided_output_path/results`. Simulated reads from all samples are located in `provided_output_path/results/merged_reads.fastq`
* Once you run the pipeline, it will create a config.yaml file in your current working directory that contains information about all the parameters used in the simulation.
* In order to find more about amplicon dropouts, please refer to `provided_output_path/results/sample_name/amplicon_stats.csv` file.
If there is  no right or left primer match, the start or end and length of the amplicon will equal to zero.

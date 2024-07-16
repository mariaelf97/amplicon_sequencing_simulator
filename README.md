# Snakemake workflow: `Amplicon Read Simulator`

[![Snakemake](https://img.shields.io/badge/snakemake-≥6.3.0-brightgreen.svg)](https://snakemake.github.io)
[![GitHub actions status](https://github.com/<owner>/<repo>/workflows/Tests/badge.svg?branch=main)](https://github.com/<owner>/<repo>/actions?query=branch%3Amain+workflow%3ATests)


A Snakemake workflow for `Amplicon read simulation for waste water sequencing or other aplications.`


## Usage

The usage of this workflow is described in the [Snakemake Workflow Catalog](https://snakemake.github.io/snakemake-workflow-catalog/?usage=<owner>%2F<repo>).

If you use this workflow in a paper, don't forget to give credits to the authors by citing the URL of this (original) <repo>sitory and its DOI (see above).

# Steps
* Clone the git repository and change the working directory `cd amplicon_sequencing_simulator`
* Install snakemake `conda create -n snakemake bioconda::snakemake`
* Replace your sample names in `data/isolates.txt`. One sample entry per line.
* Place your sample fasta files in `data/genomes` and your primer bed file in `data/primer`. The primer file should be named as `primer.bed`
* Run the workflow using `snakemake --cores 5 --use-conda --rerun-incomplete`
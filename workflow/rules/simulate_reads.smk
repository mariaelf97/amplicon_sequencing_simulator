rule wgsim:
    input:
        ref="results/amplicons/all_amplicons_filtered.fasta"
    output:
        read1="results/reads/reads_1.fastq",
        read2="results/reads/reads_2.fastq"
    params:
        "-1 400 -2 400 -r 0.00001 -d 100 -R 0.00001 -X 0 -e 0.00001 -N 50000"
    wrapper:
        "v3.13.6/bio/wgsim"
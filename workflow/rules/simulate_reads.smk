rule wgsim:
    input:
        ref="results/{isolate}/amplicons/all_amplicons_filtered.fasta"
    output:
        read1="results/{isolate}/reads/reads_1.fastq",
        read2="results/{isolate}/reads/reads_2.fastq"
    log:
        "logs/{isolate}/{isolate}_read_simulation.log"
    params:
        "-1 400 -2 400 -r 0.00001 -d 100 -R 0.00001 -X 0 -e 0.00001 -N 50000"
    wrapper:
        "v3.13.6/bio/wgsim"
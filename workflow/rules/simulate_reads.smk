rule simulate_reads:
    input:
        "results/amplicons/all_amplicons_filtered.fasta",
    output:
       reads_1="results/reads/reads_1.fastq",
       reads_2="results/reads/reads_2.fastq"
    conda:
        "../envs/wgsim"
    shell:
        """wgsim -1 400 -2 400 -r 0.00001 -d 100 -R 0.00001 -X 0 -e 0.00001 -N 50000 {input} {output.reads_1} {output.reads_2}"""
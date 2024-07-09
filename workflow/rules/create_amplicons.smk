rule create_amplicon:
    input:
        genome="resources/genomes/sample1.fasta",
        primer=config["primers"]["primer_bed"],
    output:
        directory("results/amplicons")

    conda:
        "../envs/freyja.yaml"
    shell:
        """python ../scripts/create_amplicons.py\
         -g {input.genome} -o {output} -p {input.primer}"""
rule create_amplicon:
    input:
        genome="data/genomes/{isolate}.fasta",
        primer="data/primers/primer.bed",
    output:
        directory("results/{isolate}/amplicons")

    conda:
        "../envs/freyja.yaml"
    shell:
        """python ../scripts/create_amplicons.py\
         -g {input.genome} -o {output} -p {input.primer}"""
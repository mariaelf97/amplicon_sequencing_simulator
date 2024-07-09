rule create_amplicon:
    input:
        genome="genomes/{isolate}.fna",
        primer="primers/primer_v2.bed"
    output:
        directory("/home/mahmadi/tb_seqs/seq_simulation/amplicons/hybrid/primer_V2/{isolate}/amplicons")

    conda:
        "../envs/freyja.yaml"
    shell:
        """python ../scripts/create_amplicons.py\
         -g {input.genome} -o {output} -p {input.primer}"""
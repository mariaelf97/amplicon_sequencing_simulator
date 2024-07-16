rule combine_amplicons:
    input:
        "results/{isolate}/amplicons"
    output:
        "results/{isolate}/amplicons/all_amplicons.fasta"
    log:
        "logs/{isolate}/{isolate}_combine_amplicon.log"
    conda:
        "../envs/freyja.yaml"
    shell:
        """python ../scripts/combine_amplicons.py\
         -i {input} -o {output}"""

rule combine_amplicons:
    input:
        directory("results/amplicons")
    output:
        "results/amplicons/all_amplicons.fasta"
    shell:
        """python ../scripts/combine_amplicons.py\
         -i {input} -o {output}"""

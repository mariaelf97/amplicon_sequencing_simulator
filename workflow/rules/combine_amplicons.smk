rule combine_amplicons:
    input:
        directory("results/{isolate}/amplicons")
    output:
        "results/{isolate}/amplicons/all_amplicons.fasta"
    shell:
        """python ../scripts/combine_amplicons.py\
         -i {input} -o {output}"""

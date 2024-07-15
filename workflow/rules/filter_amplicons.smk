rule filter_amplicons:
    input:
        "results/{isolate}/amplicons/all_amplicons.fasta",
    output:
        "results/{isolate}/amplicons/all_amplicons_filtered.fasta"
    conda:
        "../envs/freyja.yaml"
    shell:
        """python ../scripts/filter_amplicons.py -i {input} -o {output}"""
rule filter_amplicons:
    input:
        "results/{isolate}/amplicons/all_amplicons.fasta",
    output:
        "results/{isolate}/amplicons/all_amplicons_filtered.fasta"
    log:
        "logs/{isolate}/{isolate}_filter_amplicon.log"
    conda:
        "envs/freyja.yaml"
    shell:
        """python workflow/scripts/filter_amplicons.py -i {input} -o {output}"""
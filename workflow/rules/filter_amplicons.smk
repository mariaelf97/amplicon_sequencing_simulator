rule filter_amplicons:
    input:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons/all_amplicons.fasta"),
    output:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons/all_amplicons_filtered.fasta"),
    log:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons/filter_amplicon.log")
    conda:
        "envs/freyja.yaml"
    shell:
        """python ../workflow/scripts/filter_amplicons.py -i {input} -o {output}"""
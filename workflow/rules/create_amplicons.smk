rule create_amplicon:
    input:
        genome=config["samples"]["sample_path"],
        primer=config["primers"]["primer_file"],
    output:
        output1=directory(os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons")),
        output2=os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons/all_amplicons.fasta")
    log:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons/create_amplicon.log")
    conda:
        "envs/freyja.yaml"
    shell:
        """python workflow/scripts/create_amplicons.py\
         -g {input.genome} -o {output.output1} -p {input.primer}"""
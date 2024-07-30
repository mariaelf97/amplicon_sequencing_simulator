rule create_amplicon:
    input:
        genome=config["samples"]["sample_path"],
        primer=config["primers"]["primer_file"],
    output:
        directory(
            os.path.join(
                config["output"]["output_path"],
                "results",
                config["samples"]["sample_name"],
                "amplicons",
            )
        ),
    log:
        os.path.join(
            config["output"]["output_path"],
            "results",
            config["samples"]["sample_name"],
            "amplicons/create_amplicon.log",
        ),
    conda:
        "envs/freyja.yaml"
    shell:
        """python workflow/scripts/create_amplicons.py\
         -g {input.genome} -o {output} -p {input.primer}"""

rule wgsim:
    input:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons")
    output:
        directory(os.path.join(config["output"]["output_path"],"results",config["samples"]["sample_name"],"reads"))
    log:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"simulation.log")
    params:
        read_length_1 = config["simulation"]["read_length_1"],
        read_length_2 = config["simulation"]["read_length_2"],
        r = config["simulation"]["r"],
        d = config["simulation"]["d"],
        R = config["simulation"]["R"],
        X = config["simulation"]["X"],
        e = config["simulation"]["e"],
        N = config["simulation"]["read_cnt"]
    conda:
        "envs/wgsim.yaml"
    shell:
        """python workflow/scripts/run_wgsim.py -in {input} -d {params.d} -r {params.read_length_1}\
         -e {params.e} -m {params.r} -i {params.R} -p {params.X} -o {output} -N {params.N}"""
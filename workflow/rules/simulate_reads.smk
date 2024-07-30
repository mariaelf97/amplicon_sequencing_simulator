rule wgsim:
    input:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons")
    output:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"reads")
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
        """python workflow/scripts/run_wgsim.py -in {input} -d {params.d}\
         -N {params.N} -o {output} -1 {params.read_length_1} -e {params.e}\
          -r {params.r} -R {params.R} -X {params.X}"""
rule wgsim:
    input:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"amplicons/all_amplicons_filtered.fasta")
    output:
        read1=os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"reads/reads_1.fastq"),
        read2=os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"reads/reads_2.fastq")
    log:
        os.path.join(config["output"]["output_path"],"results",
        config["samples"]["sample_name"],"read_simulation.log")
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
        """wgsim -1 {params.read_length_1} -2 {params.read_length_2} -r {params.r}\
         -d {params.d} -R {params.R} -X {params.X} -e {params.e} -N {params.N}\
          {input} {output.read1} {output.read2}"""
rule create_amplicon:
    input:
        genome="data/genomes/{isolate}.fasta",
        primer="data/primers/primer.bed",
    output:
        output1=directory("results/{isolate}/amplicons"),
        output2="results/{isolate}/amplicons/all_amplicons.fasta"
    log:
        "logs/{isolate}_amplicon.log",
    conda:
        "envs/freyja.yaml"
    shell:
        """python workflow/scripts/create_amplicons.py\
         -g {input.genome} -o {output.output1} -p {input.primer}\
          && python workflow/scripts/combine_amplicons.py\
         -i {output.output1} -o {output.output2} """
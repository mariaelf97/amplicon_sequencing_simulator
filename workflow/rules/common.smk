configfile: "config/config.yaml"

ISOLATES = [i for i in open(config["samples"]).read().split('\n') if len(i) >0]

def get_final_output():
    final_output = expand("results/{isolate}/amplicons/all_amplicons.fasta",isolate = ISOLATES)
    final_output.extend(expand("results/{isolate}/amplicons/all_amplicons_filtered.fasta",isolate = ISOLATES))
    final_output.extend(expand("results/{isolate}/reads/reads_1.fastq",isolate = ISOLATES))
    final_output.extend(expand("results/{isolate}/reads/reads_2.fastq",isolate = ISOLATES))
    return final_output
    

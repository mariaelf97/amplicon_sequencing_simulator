# amplicon_simulator_wrapper.py
import subprocess
import os
import sys
import argparse
import yaml
import pandas as pd

def run_amplicon_simulator():
    command = [ "snakemake",
        "--configfile", "config.yaml", "--cores", "5", "--use-conda"
    ]
    subprocess.run(command, check=True)
    
def create_config_dict(sample_name,sample_path,primer_file,output_file,read_cnt,read_length,r,d,R,X,e):
    """
    Generates a config file based on user-defined parameters
    
    Parameters:
    parameters : defined in argparser
    config file (str): config dictionary
    """
    config = {
        'samples': {
            'sample_name': str(sample_name),
            'sample_path':str(sample_path)
        },
        'primers': {
            'primer_file': str(primer_file)
        },
        'output': {
            'output_path': str(output_file)
        },
        'simulation': {
            'read_cnt': int(read_cnt),
            'read_length_1': int(read_length),
            'read_length_2': int(read_length),
            'r': r,
            'd': d,
            'R': R,
            'X': X,
            'e': e
        }
    }
    return config

def write_yaml(config):
    """
    Writes config dictionary to a yaml formatted file.
    
    Parameters:
    config : config dictionary
    config file (str): yaml formatted config file
    """
    with open("config.yaml", 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

 
def merge_fastq_files(fastq_file, output_file):
    """
    Merges a FASTQ file into an output FASTQ file using subprocess.call.

    Parameters:
    fastq_file (str): Path to the input FASTQ file.
    output_file (str): Path to the output FASTQ file.
    """
    command = f'cat "{fastq_file}" >> "{output_file}"'
    subprocess.call(command, shell=True)

def main():
    parser = argparse.ArgumentParser(description="Amplicon sequencing simulator with user-defined proportions")
    parser.add_argument("--samplenames", "-s", help="name of samples in order, separated by a comma")
    parser.add_argument("--samplepaths", "-sp", help="path of samples in order, separated by a comma")
    parser.add_argument("--proportions", "-pr", help="sample proportions separated by a comma, 0.0-1.0")
    parser.add_argument("--primers", "-p", help="Path to primer bed file")
    parser.add_argument("--readscnt", "-n", help="Total number of reads to be generated")
    parser.add_argument("--readlength", "-l", help="Total number of reads to be generated", default=150)
    parser.add_argument("--mutationrate", "-r", help="Mutation rate",default=0.00001)
    parser.add_argument("--outerdistance", "-d", help="outer distance between reads", default=100)
    parser.add_argument("--indelfraction", "-R", help="Fraction of indels", default=0.00001)
    parser.add_argument("--indelextended", "-X", help="probability an indel is extended", default=0)
    parser.add_argument("--baseerrorrate", "-e", help="base error rate", default= 0)
    parser.add_argument("--output", "-o", help="Path to output file")
    
    args = parser.parse_args()
    # create a list of sample names, paths and proportions
    sample_names = str(args.samplenames).split(",")
    sample_paths = str(args.samplepaths).split(",")
    proportions = str(args.proportions).split(",")
    proportions = list(map(float, proportions))
    # error if the proportion counts do not match the sample counts
    if len(sample_names) != len(proportions) != len(sample_paths) != len(sample_paths):
        raise Exception("Number of samples and proportions should match!")
    # error if proportions do not add up to 1.0
    if sum(proportions) != 1.0:
        raise Exception("Sum of all proportions should equal to 1.0!")
    col_names = ["ref","start", "end", "left_right", "primer_pool","strand", "primer_seq"]
    # read the primer bed file
    primer_bed = pd.read_csv(args.primers, sep= "\t", names=col_names)
    # split the amplicon name into number and left/right
    primer_bed["amplicon_number"] = primer_bed["left_right"].str.split('_').str[1]
    amplicon_cnt = int(primer_bed['amplicon_number'].nunique())
    # create read counts based on user-defined proportions
    read_cnts = [i * int(args.readscnt) for i in proportions]
    read_cnts_per_amp = [int(i /amplicon_cnt) for i in read_cnts]
    # loop over each isolate and create reads
    for name,path,count in zip(sample_names,sample_paths, read_cnts_per_amp):
        config_file = create_config_dict(name,path,args.primers,args.output,count,args.readlength,
                                     args.mutationrate,args.outerdistance,
                                     args.indelfraction,args.indelextended,
                                     args.baseerrorrate)
        # write config file for each run
        write_yaml(config=config_file)
        # simulate reads based on config file
        run_amplicon_simulator()
        # create paths to merge all reads after simualtion
        read_path = os.path.join(os.path.abspath(args.output),"results",name,"reads/merged_reads.fq")
        output_path = os.path.join(os.path.abspath(args.output),"results/merged_reads.fastq")
        # merge fastq files 
        merge_fastq_files(read_path,output_path)
    
    
if __name__ == "__main__":
    main()
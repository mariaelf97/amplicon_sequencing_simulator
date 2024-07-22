# amplicon_simulator_wrapper.py
import subprocess
import os
import sys
import argparse
import yaml

def run_amplicon_simulator():
    command = [ "snakemake",
        "--configfile", "config.yaml", "--cores", "5", "--use-conda"
    ]
    subprocess.run(command, check=True)
    
def create_config_dict(sample_name,sample_path,primer_file,output_file,read_cnt,read_length,r,d,R,X,e):
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
            'read_cnt': read_cnt,
            'read_length_1': read_length,
            'read_length_2': read_length,
            'r': r,
            'd': d,
            'R': R,
            'X': X,
            'e': e
        }
    }
    return config

def write_yaml(config):
    with open("config.yaml", 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

def main():
    parser = argparse.ArgumentParser(description="Amplicon sequencing simulator with user-defined proportions")
    parser.add_argument("--samplenames", "-s", help="name of samples in order, separated by a comma")
    parser.add_argument("--samplepaths", "-sp", help="path of samples in order, separated by a comma")
    parser.add_argument("--proportions", "-pr", help="sample proportions separated by a comma, 0.0-0.1")
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
    # the sequence used to create amplicons
    sample_names = str(args.samplenames).split(",")
    sample_paths = str(args.samplepaths).split(",")
    proportions = str(args.proportions).split(",")
    proportions = list(map(float, proportions))
    if len(sample_names) != len(proportions) != len(sample_paths):
        raise Exception("number of samples and proportions should match")
    if sum(proportions) != 1.0:
        raise Exception("Sum of all proportions should equal to 1.0")
    read_cnts = [i * int(args.readscnt) for i in proportions]
    for name,path,count in zip(sample_names,sample_paths, read_cnts):
        config_file = create_config_dict(name,path,args.primers,args.output,count,args.readlength,
                                     args.mutationrate,args.outerdistance,
                                     args.indelfraction,args.indelextended,
                                     args.baseerrorrate)
        write_yaml(config=config_file)
        run_amplicon_simulator()
    
    
if __name__ == "__main__":
    main()
import os
import subprocess
import argparse

def get_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Run wgsim on all FASTA files in a directory.")
    parser.add_argument("-in", "--directory", required=True, help="Directory containing FASTA files.")
    parser.add_argument("-d", "--outerdistance", required=True, type=int, help="outer distance")
    parser.add_argument("-N", "--readcnt", required=True, type=int, help="number of reads per amplicon")
    parser.add_argument("-o", "--output", required=True, help="Directory to store output files.")
    parser.add_argument("-1", "--read_length", required=True, type=int, help="Read length (e.g., 100).")
    parser.add_argument("-e", "--error_rate", required=True, type=float, help="Base error rate (e.g., 0.02).")
    parser.add_argument("-r", "--mutation_rate", required=True, type=float, help="Mutation rate (e.g., 0.001).")
    parser.add_argument("-R", "--indel_fraction", required=True, type=float, help="Fraction of indels (e.g., 0.15).")
    parser.add_argument("-X", "--indel_extend_probability", required=True, type=float, help="Probability an indel is extended (e.g., 0.3).")
    return parser.parse_args()

def run_wgsim_on_fasta(fasta_file, output_dir, read_length, error_rate, mutation_rate, outer_distance, read_cnt, indel_fraction, indel_extend_probability):
    """Runs wgsim on a single FASTA file with the given parameters."""
    output_prefix = os.path.splitext(os.path.basename(fasta_file))[0]
    output1 = os.path.join(output_dir, f"{output_prefix}_1.fq")
    output2 = os.path.join(output_dir, f"{output_prefix}_2.fq")
    merged_output = os.path.join(output_dir, "merged_reads.fq")

    command = [
        "wgsim",
        "-e", str(error_rate),
        "-r", str(mutation_rate),
        "-d", str(outer_distance),
        "-N", str(read_cnt),
        "-R", str(indel_fraction),
        "-X", str(indel_extend_probability),
        "-1", str(read_length),
        "-2", str(read_length),
        fasta_file,
        output1,
        output2
    ]

    subprocess.run(command, check=True)
    print(f"wgsim completed for {fasta_file}")
    command = f'cat "{output1}" >> "{merged_output}"'
    subprocess.call(command, shell=True)
    
def main():
    args = get_arguments()

    # Check if the input directory exists
    if not os.path.isdir(args.directory):
        print(f"Directory {args.directory} does not exist.")
        return

    # Create the output directory if it doesn't exist
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Iterate over all files in the directory
    for filename in os.listdir(args.directory):
        if filename.endswith(".fasta") or filename.endswith(".fa"):
            fasta_file = os.path.join(args.directory, filename)
            run_wgsim_on_fasta(fasta_file, args.output, args.read_length, args.error_rate, args.mutation_rate, args.outerdistance, args.readcnt, args.indel_fraction, args.indel_extend_probability)
if __name__ == "__main__":
    main()

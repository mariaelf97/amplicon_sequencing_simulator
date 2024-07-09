import argparse
import os


def combine_fasta_files(input_dir, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(input_dir):
            if filename.endswith('.fasta') or filename.endswith('.fa'):
                filepath = os.path.join(input_dir, filename)
                with open(filepath, 'r') as infile:
                    outfile.write(infile.read())


def main():
    parser = argparse.ArgumentParser(description="remove amplicons with length equal to 0 or more than 10k")
    parser.add_argument("--input", "-i", help="amplicon directory", required=True)
    parser.add_argument("--output", "-o", help="output multi fasta file", required=True)

    args = parser.parse_args()
    combine_fasta_files(args.input, args.output)


if __name__ == "__main__":
    main()
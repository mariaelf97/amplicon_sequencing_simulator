import argparse
from Bio import SeqIO


def filter_fasta(input_file, output_file, min_length=1, max_length=10000):
    # Open input and output files
    with open(input_file, "r") as handle, open(output_file, "w") as out_handle:
        # Iterate over records in input FASTA file
        for record in SeqIO.parse(handle, "fasta"):
            # Check if sequence length is within the specified range
            if min_length <= len(record.seq) <= max_length:
                # Write the record to the output file
                SeqIO.write(record, out_handle, "fasta")


def main():
    parser = argparse.ArgumentParser(description="remove amplicons with length equal to 0 or more than 10k")
    parser.add_argument("--input", "-i", help="amplicon multi fasta file", required=True)
    parser.add_argument("--output", "-o", help="output multi fasta file", required=True)

    args = parser.parse_args()
    filter_fasta(args.input, args.output)


if __name__ == "__main__":
    main()
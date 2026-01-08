from collections import Counter
import matplotlib.pyplot as plt
import os

def read_fasta(filename):
    sequences = {}
    with open(filename, "r") as file:
        protein = ""
        seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if protein:
                    sequences[protein] = seq
                protein = line[1:]
                seq = ""
            else:
                seq += line
        sequences[protein] = seq
    return sequences


def analyze_sequences(sequences):
    lengths = {}
    amino_acids = Counter()

    for protein, seq in sequences.items():
        lengths[protein] = len(seq)
        amino_acids.update(seq)

    return lengths, amino_acids


def plot_amino_acids(amino_acids):
    if not os.path.exists("results"):
        os.makedirs("results")

    acids = list(amino_acids.keys())
    counts = list(amino_acids.values())

    plt.figure()
    plt.bar(acids, counts)
    plt.xlabel("Amino Acids")
    plt.ylabel("Frequency")
    plt.title("Amino Acid Distribution Across Proteins")
    plt.savefig("results/amino_acid_distribution.png")
    plt.close()


def main():
    sequences = read_fasta("sequences.fasta")
    lengths, amino_acids = analyze_sequences(sequences)

    print("Protein Length Analysis")
    print("-----------------------")
    for protein, length in lengths.items():
        print(f"{protein}: {length} amino acids")

    print("\nTop 5 Most Frequent Amino Acids")
    for aa, count in amino_acids.most_common(5):
        print(f"{aa}: {count}")

    plot_amino_acids(amino_acids)
    print("\nPlot saved in results/amino_acid_distribution.png")


if __name__ == "__main__":
    main()

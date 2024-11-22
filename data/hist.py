import matplotlib.pyplot as plt
import numpy as np
import argparse
import csv
import os
import statistics

plt.rcParams.update({'font.size': 18})
plt.rcParams.update({"text.usetex": True})
plt.rc('text.latex', preamble=r'\usepackage{sansmath}\sansmath')

plt.figure(figsize=(5,3))  # Adjust figure size

def create_hist(data, filename):
    data_max = max(data)
    data_min = min(data)

    x_min = data_min - data_min % 10
    x_max = data_max + (10 - data_max % 10)

    bins = (x_max - x_min) // 10

    bin_edges = np.linspace(x_min, x_max, bins + 1)
    print(bin_edges)

    bin_counts = [0] * bins
    for entry in data:
        for i in range(1, len(bin_edges)):
            if entry < bin_edges[i]:
                bin_counts[i-1] += 1
                break

    assert(sum(bin_counts) == len(data))
    for i in range(len(bin_counts)):
        bin_counts[i] /= len(data)
        bin_counts[i] *= 100
    print(sum(bin_counts))

    # Compute the bin centers for plotting
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    box_face_color = 'mediumspringgreen'
    plt.bar(bin_centers, bin_counts, width=bin_edges[1] - bin_edges[0], edgecolor='black', color=box_face_color)

    plt.xlabel('Latency (ms)')
    plt.ylabel('Percentage of Times')

    # Show the plot
    plt.savefig(filename, bbox_inches='tight')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str)

    args = parser.parse_args()

    with open(args.filename, "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = [int(round(float(row[-1]))) for row in reader]

    output_file = os.path.splitext(os.path.basename(args.filename))[0] + '.pdf'
    create_hist(data, output_file)

    print(f'mean: {statistics.mean(data)}, median: {statistics.median(data)}, std dev: {statistics.stdev(data):.2f}, p99: {np.percentile(data, 99)}')

if __name__ == "__main__":
    main()

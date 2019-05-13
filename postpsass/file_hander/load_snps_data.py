from collections import defaultdict


def load_snps_data(snps_file_path=None):
    snps_file = open(snps_file_path, 'r')
    snps_pos = defaultdict(lambda: defaultdict(list))
    for line in snps_file:
        split_line = line.strip().split('\t')
        snps_pos[split_line[0]][split_line[1]] = split_line[2:]
    return snps_pos

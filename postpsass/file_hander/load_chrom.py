from collections import defaultdict


def load_chrom(chrom_len_path=None):
    chrom_len_file = open(chrom_len_path, 'r')
    chrom_pos_data = defaultdict()
    for line in chrom_len_file:
        line_split = line[:-1].split('\t')
        chrom_pos_data[line_split[0]] = line_split[1]
    return chrom_pos_data

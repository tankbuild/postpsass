from postpsass.file_hander.load_chrom import load_chrom
from postpsass.file_hander.load_snps_data import load_snps_data


def load_all(first_file_path=None,
             second_file_path=None,
             chrom_len_path=None):
    print("load all data")
    chrom_pos_data = load_chrom(chrom_len_path)
    first_data = load_snps_data(first_file_path)
    second_data = load_snps_data(second_file_path)
    data = [chrom_pos_data, first_data, second_data]
    return data

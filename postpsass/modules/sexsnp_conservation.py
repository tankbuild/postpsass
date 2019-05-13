from postpsass.file_hander import load_all
from postpsass.output import output
from collections import defaultdict
import numpy as np
from tqdm import tqdm


def sexsnp_conservation(first_file_path,
                        second_file_path,
                        chrom_len_path,
                        range_het,
                        range_hom,
                        resolution,
                        win_size,
                        output_file_path,
                        win_file_path):

    data = load_all(first_file_path,
                    second_file_path,
                    chrom_len_path)
    info = sexsnp(data, range_het, range_hom, resolution, win_size)
    output(info, output_file_path, win_file_path)


def sexsnp(data=None,
           range_het=None,
           range_hom=None,
           resolution=None,
           win_size=None):
    sexsnps = defaultdict(lambda: defaultdict(list))
    na_fill = ['NA'] * 12
    print('#### Genetating sex snps dictionary ####')
    for name in tqdm(data[0]):
        for pos in range(int(data[0][name])):
            pos += 1
            pos = str(pos)
            if pos in data[1][name].keys() and pos in data[2][name].keys():
                first_male_snp = np.array(list(map(float, np.array(data[1][name][pos][1:7]))))
                first_female_snp = np.array(list(map(float, np.array(data[1][name][pos][7:]))))
                second_male_snp = np.array(list(map(float, np.array(data[2][name][pos][1:7]))))
                second_female_snp = np.array(list(map(float, np.array(data[2][name][pos][7:]))))
                if data[1][name][pos][0] == data[2][name][pos][0] == 'M':
                    if list(first_male_snp >= (0.5 - range_het)) == list(second_male_snp >= (0.5 - range_het)) and list(first_female_snp >= (1 - range_hom)) == list(second_female_snp > (1 - range_hom)):
                        sexsnps[name][pos].extend(['M', 'Common'])
                        sexsnps[name][pos].extend(data[1][name][pos][1:])
                        sexsnps[name][pos].extend(data[2][name][pos][1:])
                    else:
                        sexsnps[name][pos].extend(['M', 'Divergence_minor_allele'])
                        sexsnps[name][pos].extend(data[1][name][pos][1:])
                        sexsnps[name][pos].extend(data[2][name][pos][1:])
                elif data[1][name][pos][0] == data[2][name][pos][0] == 'F':
                    if list(first_female_snp >= (0.5 - range_het)) == list(second_female_snp >= (0.5 - range_het)) and list(first_male_snp >= (1 - range_hom)) == list(second_male_snp > (1 - range_hom)):
                        sexsnps[name][pos].extend(['F', 'Common'])
                        sexsnps[name][pos].extend(data[1][name][pos][1:])
                        sexsnps[name][pos].extend(data[2][name][pos][1:])
                    else:
                        sexsnps[name][pos].extend(['F', 'Divergence_minor_allele'])
                        sexsnps[name][pos].extend(data[1][name][pos][1:])
                        sexsnps[name][pos].extend(data[2][name][pos][1:])
                else:
                    sexsnps[name][pos].extend(['N', 'Divergence_major_allele'])
                    sexsnps[name][pos].extend(data[1][name][pos][1:])
                    sexsnps[name][pos].extend(data[2][name][pos][1:])
            elif pos in data[1][name].keys() and pos not in data[2][name].keys():
                sexsnps[name][pos].extend([data[1][name][pos][0], 'Unique_1'])
                sexsnps[name][pos].extend(data[1][name][pos][1:])
                sexsnps[name][pos].extend(na_fill)
            elif pos not in data[1][name].keys() and pos in data[2][name].keys():
                sexsnps[name][pos].extend([data[2][name][pos][0], 'Unique_2'])
                sexsnps[name][pos].extend(na_fill)
                sexsnps[name][pos].extend(data[2][name][pos][1:])
            else:
                next
    # generating sex snps in window size
    sexsnp_win = defaultdict(lambda: defaultdict(dict))
    print('#### Genetating sex snps dictionary in window size ####')
    for name in tqdm(data[0]):
        step = list(range(0, int(data[0][name]), resolution))
        for r in step:
            count = {'Common': 0, 'Unique_1': 0, 'Unique_2': 0, 'Divergence_minor_allele': 0, 'Divergence_major_allele': 0}
            for pos in range(r, r + win_size):
                pos = str(pos)
                if pos in sexsnps[name]:
                    count[sexsnps[name][pos][1]] += 1
            sexsnp_win[name][r] = count

    return sexsnps, sexsnp_win

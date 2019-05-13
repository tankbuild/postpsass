

def output(info=None,
           output_file_path=None,
           win_file_path=None):
    output_file = open(output_file_path, 'w')
    print('write sexsnp_conservation.tsv file')
    output_file.write('Contig' + '\t' + 'Position' + '\t' + 'sex' + '\t' + 'snp_type' + '\t' \
                      + 'M_A_1' + '\t' + 'M_T_1' + '\t' + 'M_G_1' + '\t' + 'M_C_1' + '\t' + 'M_N_1' + '\t' + 'M_I_1' + '\t' \
                      + 'F_A_1' + '\t' + 'F_T_1' + '\t' + 'F_G_1' + '\t' + 'F_C_1' + '\t' + 'F_N_1' + '\t' + 'F_I_1' + '\t' \
                      + 'M_A_2' + '\t' + 'M_T_2' + '\t' + 'M_G_2' + '\t' + 'M_C_2' + '\t' + 'M_N_2' + '\t' + 'M_I_2' + '\t' \
                      + 'F_A_2' + '\t' + 'F_T_2' + '\t' + 'F_G_2' + '\t' + 'F_C_2' + '\t' + 'F_N_2' + '\t' + 'F_I_2' + '\t' \
                      + '\n')
    for name in info[0]:
        for pos in info[0][name]:
          output_file.write(name + '\t' + pos + '\t' + info[0][name][pos][0] + '\t' + info[0][name][pos][1] + '\t' \
                      + info[0][name][pos][2] + '\t' + info[0][name][pos][3] + '\t' + info[0][name][pos][4] + '\t' + info[0][name][pos][5] + '\t' + info[0][name][pos][6] + '\t' + info[0][name][pos][7] + '\t' \
                      + info[0][name][pos][8] + '\t' + info[0][name][pos][9] + '\t' + info[0][name][pos][10] + '\t' + info[0][name][pos][11] + '\t' + info[0][name][pos][12] + '\t' + info[0][name][pos][13] + '\t' \
                      + info[0][name][pos][14] + '\t' + info[0][name][pos][15] + '\t' + info[0][name][pos][16] + '\t' + info[0][name][pos][17] + '\t' + info[0][name][pos][18] + '\t' + info[0][name][pos][19] + '\t' \
                      + info[0][name][pos][20] + '\t' + info[0][name][pos][21] + '\t' + info[0][name][pos][22] + '\t' + info[0][name][pos][23] + '\t' + info[0][name][pos][24] + '\t' + info[0][name][pos][25] + '\t' \
                      + '\n')
    print('write sexsnp_conservation_win.tsv file')
    win_file = open(win_file_path, 'w')
    win_file.write('Contig' + '\t' + 'Position' + '\t' + 'n_Common' + '\t' + 'n_Unique_1' + '\t' \
                      + 'n_Unique_2' + '\t' + 'n_Divergence_minor_allele' + '\t' + 'n_Divergence_major_allele' \
                      + '\n')
    for name in info[1]:
        for pos in info[1][name]:
          win_file.write(name + '\t' + str(pos) + '\t' + str(info[1][name][pos]['Common']) + '\t' + str(info[1][name][pos]['Unique_1']) + '\t' \
                      + str(info[1][name][pos]['Unique_2']) + '\t' + str(info[1][name][pos]['Divergence_minor_allele']) + '\t' \
                      + str(info[1][name][pos]['Divergence_major_allele']) + '\n')

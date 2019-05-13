from postpsass.modules.sexsnp_conservation import sexsnp_conservation
# import sys
# from radseq_analysis.modules import visualization


def analysis(first_file_path=None,
             second_file_path=None,
             chrom_len_path=None,
             range_het=None,
             range_hom=None,
             resolution=None,
             win_size=None,
             output_file_path=None,
             win_file_path=None,
             analysis=None):
    # print('**data is been analyzed**')
    # toolbar_width = 40
    # sys.stdout.write("[%s]" % (" " * toolbar_width))
    # sys.stdout.flush()
    # sys.stdout.write("\b" * (toolbar_width + 1))
    # if analysis == 'sexsnp_conservation':
        sexsnp_conservation(first_file_path,
                            second_file_path,
                            chrom_len_path,
                            range_het,
                            range_hom,
                            resolution,
                            win_size,
                            output_file_path,
                            win_file_path)
    # sys.stdout.write("\n")
    # elif analysis == 'visualize':
    #     visualization(parameters)

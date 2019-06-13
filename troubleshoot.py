#!/usr/bin/python3
# -*- coding: utf-8 -*-



#1)про неизменяемые типы
# def create_complex_string(name_of_gene, name_of_gene2, strand_tmp, count, length_of_exon ):
#     template =  '{0}_{1}_{2}_{3}'
#     return template.format(name_of_gene2, "exon", (count + 1), name_of_gene) if strand_tmp == "+" \
#         else template.format(name_of_gene2, "exon", (length_of_exon - count), name_of_gene)
#а на месте вызова comp_string возвращать строку в список
#2)про глобальные переменные
# final table вернуть из new_list

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
final_table = []



def create_complex_string(tmp_list, name_of_gene, name_of_gene2, strand_tmp, count, length_of_exon):
    if strand_tmp == "+":

        compl_str = '{0}_{1}_{2}_{3}'.format(name_of_gene2, 'exon', (count + 1), name_of_gene)
        tmp_list.append(compl_str)
    else:
        compl_str = '{0}_{1}_{2}_{3}'.format(name_of_gene2, 'exon', (length_of_exon - count), name_of_gene)
        tmp_list.append(compl_str)
    return tmp_list


def new_list(chr, ex_start, ex_end, name2, name, strand, tx_start_tmp,
             cd_start_tmp, tx_end_tmp, cd_end_tmp, utr_include):
    global tmp
    for i in range(len(ex_start)):

        if i == 0:
            if not utr_include:  # yes, include utr
                tmp = [chr, ex_start[i], ex_end[i]]
                tmp = create_complex_string(tmp, name, name2, strand, i, len(ex_end))

                tmp.append(tx_start_tmp)
                tmp.append(cd_start_tmp)

            elif utr_include:  # do not include utr
                if ex_start[i] == tx_start_tmp:
                    tmp = [chr, cd_start_tmp, ex_end[i]]
                    tmp = create_complex_string(tmp, name, name2, strand, i, len(ex_end))

                    tmp.append(tx_start_tmp)
                    tmp.append(cd_start_tmp)
                else:
                    tmp = [chr, ex_start[i], ex_end[i]]
                    tmp = create_complex_string(tmp, name, name2, strand, i, len(ex_end))

                    tmp.append(tx_start_tmp)
                    tmp.append(cd_start_tmp)

        elif i == len(ex_end) - 1:
            if not utr_include:  # yes, include utr
                tmp = [chr, ex_start[i], ex_end[i]]
                tmp = create_complex_string(tmp, name, name2, strand, i, len(ex_end))

                tmp.append(tx_start_tmp)
                tmp.append(cd_start_tmp)

            elif utr_include:  # do not include utr
                if ex_end[i] == tx_end_tmp:
                    tmp = [chr, ex_start[i], cd_end_tmp]
                    tmp = create_complex_string(tmp, name, name2, strand, i, len(ex_end))

                    tmp.append(tx_start_tmp)
                    tmp.append(cd_start_tmp)
                else:
                    tmp = [chr, ex_start[i], ex_end[i]]
                    tmp = create_complex_string(tmp, name, name2, strand, i, len(ex_end))

                    tmp.append(tx_start_tmp)
                    tmp.append(cd_start_tmp)

        else:
            tmp = [chr, ex_start[i], ex_end[i]]
            tmp = create_complex_string(tmp, name, name2, strand, i, len(ex_end))

            tmp.append(tx_start_tmp)
            tmp.append(cd_start_tmp)

        final_table.append(tmp)

initial_file = open ( 'PULM_exons_initial.txt', 'r')
spl_init = initial_file.read().split('\n')

for j in range(1, len(spl_init) - 1):

    cell = spl_init[j].split('\t')


    short_list = []

    if cell[2] != 'chrX':
        if cell[2] != 'chrY':
            short_list.append(int(cell[2].replace('chr', '')))  # (0)chr_x
        else:
            short_list.append(25)
    else:
        short_list.append(24)




    short_list.append(cell[9])   # (1) exon_start list
    short_list.append(cell[10])  # (2) exon_stop list
    short_list.append(cell[12])  # (3) name2 list
    short_list.append(cell[1])   # (4) name1 list
    short_list.append(cell[3])   # (5) strand
    short_list.append(cell[4])   # (6) tx_start
    short_list.append(cell[6])   # (7) cd_start
    short_list.append(cell[5])   # (8) tx_end
    short_list.append(cell[7])   # (9) cd_end


    ex_start_list = short_list[1].split(',')
    ex_start_list.pop()
    ex_stop_list = short_list[2].split(',')
    ex_stop_list.pop()

    tmp_extend = 0

    if tmp_extend > 0:
        for i in range(0, len(ex_start_list)):
            ex_start_list[i] = int(
                ex_start_list[i]) - tmp_extend
            ex_stop_list[i] = int(ex_stop_list[i]) + tmp_extend
        tx_start = int(short_list[6]) - tmp_extend
        cd_start = int(short_list[7]) - tmp_extend
        tx_end = int(short_list[8]) + tmp_extend
        cd_end = int(short_list[9]) + tmp_extend
    else:
        for i in range(0, len(ex_start_list)):
            ex_start_list[i] = int(ex_start_list[i])
            ex_stop_list[i] = int(ex_stop_list[i])
        tx_start = int(short_list[6])
        cd_start = int(short_list[7])
        tx_end = int(short_list[8])
        cd_end = int(short_list[9])

    tmp_utr = True

    new_list(short_list[0], ex_start_list, ex_stop_list, short_list[3], short_list[4], short_list[5], tx_start, cd_start, tx_end, cd_end, tmp_utr)

final_table.sort()

f = open('PULM_enlarged_UTR_included.bed', 'w')
for i in final_table:
    if i[0] == 24:
        i[0] = "chrX"
    elif i[0] == 25:
        i[0] = "chrY"
    else:
        i[0] = "chr" + str(i[0])
    string = [str(i[0]), str(i[1]), str(i[2]), str(i[3]), "\n"]
    f.write('\t'.join(string))

f.close()

for i in final_table:
    print(i)

# file = open('sample_NCBI_refSeq.txt', "r")
# for line in file:
#     print(line[0])
#
# file = open('test.csv', 'r')
# for line in file:
#     print(line)
import xlrd as xlrd
import xlwt as xlwt
#


workbook = xlrd.open_workbook('test.xlsx')
worksheet = workbook.sheet_by_index(0)
name = worksheet.col_values(1,2)     #какой столбик, с какого элемента начинать, каким заканчивать
chrom = worksheet.col_values(2,2)    #получаем список, можем обращатся к нему поэленемтно   crom[3]/name[3]
name2 = worksheet.col_values(12,2)
strand = worksheet.col_values(3,2)
exon_number = worksheet.col_values(8,2)
exonStarts = worksheet.col_values(9,2)
exonEnds = worksheet.col_values(10,2)


for n in exon_number:
    for m in range(0,exon_number[n])
        exonStarts:
    a = exonStarts[n].split(',')
    b = sorted(a)
    for i in b:
        if i == '':
            b.remove(i)
            n=n+1
print(b)






for i, elem in enumerate(exon_number):       #здесь мы список из float преобразуем в список из int
    exon_number[i] = int(elem)
for n in exon_number:                       #здесь мы создаем список из номеров интронов
    list_of_amount_of_exons = [i for i in range(1, n + 1)]   #необходимо для элемента n в last_col = name2_exon_n_name
    # print(list_of_amount_of_exons)
#     тут нужно добавить условие про +- цепь
# if strand[2] == '+':
#     list_of_exons.sort   нужно как-то умудриться отсортировать
# else:
#     list_of_exons.sort reverse
#



# chr_raw = worksheet.col_values(0,0,7)
# print(chr_raw)
for colnum in range(0,worksheet.nrows+1,1):
    col_chr = worksheet.col_values(2,2,colnum)
#
# for i in col:
#     print(i)
# print(col)
for colnum in range(0,worksheet.nrows+1,1):
    col_stEx = worksheet.col_values(9,2,colnum)
    # for i in col_stEx:
    #     print(i)
# print(col_stEx)

for colnum in range(0,worksheet.nrows+1,1):
    col_EndEx = worksheet.col_values(10,2,colnum)


Coordinates = dict (zip(col_stEx,col_EndEx))
# print(Coordinates.items())

#n=number of exons
#last_col = name2_exon_n_name



# value = worksheet.cell()
# chr_raw = worksheet.col(1,2,7)
#
# print(worksheet.n)
#
#


# for i in worksheet:
#     if i != 0:
#         print(worksheet.cell(4,i).value)          TypeError: 'Sheet' object is not iterable

# chr_raw = worksheet.col(0,2)


# workbook = xlwt.Workbook()
# workbook.save('my_file.xls')
# sheet = workbook.add_sheet('Sheet_1')

import xlwt
# for n in chr_raw:


# wb = xlwt.Workbook()
# ws = wb.add_sheet('A Test Sheet')
#
# ws.write(1,1, chr_raw)
#
#
# wb.save('example.xls')

# import csv
#
# FILENAME = "test.csv"
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     print(reader)
    # for row in reader:
    #      print(row['chrom'],row['name'])

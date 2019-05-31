import csv
import pandas as pd
from numpy import nan as Nan



def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]


table=[]
with open('2019-04-09_BCD057.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:

        table.append(row)



data = table[6:]

Names = table[2]


'''
преобразуем типы данных внутри таблицы'''

for i in range(len(data)):
    for j in range(len(data[i])):

        if ',' in data[i][j]:
            data[i][j] = float(data[i][j].replace(',', '.'))



for i in range(len(data)):
    for j in range(len(data[i])):
        if type(data[i][j]) is not float and data[i][j].isnumeric():

            data[i][j] = int(data[i][j])


'''only ST'''
st=[]
for i in data:
    for j in i:
        if type(j)==str and j.startswith('ST'):

            st.append(i)

intensity=[]
for i in st:
    for j in i:
        if type(j) is float:
            intensity.append(j)


'''делим на отдельные векторы'''



B = 'B		ST1_1	ST1_2	ST1_3	ST1_4	ST1_5	ST1_6	ST1_7	ST1_8	ST1_9	ST1_10			ST1_1	ST1_2	ST1_3	ST1_4	ST1_5	ST1_6	ST1_7	ST1_8	ST1_9	ST1_10			ST1_1	ST1_2	ST1_3	ST1_4	ST1_5	ST1_6	ST1_7	ST1_8	ST1_9	ST1_10			ST2_1	ST2_2	ST2_3	ST2_4	ST2_5	ST2_6	ST2_7	ST2_8	ST2_9	ST2_10			ST2_1	ST2_2	ST2_3	ST2_4	ST2_5	ST2_6	ST2_7	ST2_8	ST2_9	ST2_10			ST3_1	ST3_2	ST3_3	ST3_4	ST3_5	ST3_6	ST3_7	ST3_8	ST3_9	ST3_10			ST3_1	ST3_2	ST3_3	ST3_4	ST3_5	ST3_6	ST3_7	ST3_8	ST3_9	ST3_10			ST3_1	ST3_2	ST3_3	ST3_4	ST3_5	ST3_6	ST3_7	ST3_8	ST3_9	ST3_10			ST4_1	ST4_2	ST4_3	ST4_4	ST4_5	ST4_6	ST4_7	ST4_8	ST4_9	ST4_10			ST4_1	ST4_2	ST4_3	ST4_4	ST4_5	ST4_6	ST4_7	ST4_8	ST4_9	ST4_10			ST4_1	ST4_2	ST4_3	ST4_4	ST4_5	ST4_6	ST4_7	ST4_8	ST4_9	ST4_10																																												'



concentrations = []
for i in data:
    concentrations.append(i[0].split('-'))
conc=[]
for i in concentrations:
    conc.append(i[1])
concentrations.clear()
for i in conc[:10]:
    concentrations.append(float(i))







d = [x for x in range(216)]
with open('try.txt', 'w') as tre:
    print('<>', end='	', file=tre)
    for i in d:
        print(i+1, end='	', file=tre)

    print('\nA', end='	', file=tre)
    for i in range(216):
        print('',end='	', file=tre)
    print('\n',B, file=tre)
    for i in range(10):
        print(*concentrations, sep='\t',end='		', file=tre)
    print('\nB', end='	', file=tre)
    for i in intensity:
        print(i, sep='\t',end='\t', file=tre)
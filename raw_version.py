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


intensity = split_list(intensity, wanted_parts=12)

first_plate = intensity[0:6]
second_plate = intensity[6:12]

print(first_plate)




B = 'B		ST1_1	ST1_2	ST1_3	ST1_4	ST1_5	ST1_6	ST1_7	ST1_8	ST1_9	ST1_10			ST1_1	ST1_2	ST1_3	ST1_4	ST1_5	ST1_6	ST1_7	ST1_8	ST1_9	ST1_10			ST1_1	ST1_2	ST1_3	ST1_4	ST1_5	ST1_6	ST1_7	ST1_8	ST1_9	ST1_10			ST2_1	ST2_2	ST2_3	ST2_4	ST2_5	ST2_6	ST2_7	ST2_8	ST2_9	ST2_10			ST2_1	ST2_2	ST2_3	ST2_4	ST2_5	ST2_6	ST2_7	ST2_8	ST2_9	ST2_10			ST3_1	ST3_2	ST3_3	ST3_4	ST3_5	ST3_6	ST3_7	ST3_8	ST3_9	ST3_10			ST5_1	ST5_2	ST5_3	ST5_4	ST5_5	ST5_6	ST5_7	ST5_8	ST5_9	ST5_10			ST5_1	ST5_2	ST5_3	ST5_4	ST5_5	ST5_6	ST5_7	ST5_8	ST5_9	ST5_10			ST5_1	ST5_2	ST5_3	ST5_4	ST5_5	ST5_6	ST5_7	ST5_8	ST5_9	ST5_10			ST7_1	ST7_2	ST7_3	ST7_4	ST7_5	ST7_6	ST7_7	ST7_8	ST7_9	ST7_10			ST7_1	ST7_2	ST7_3	ST7_4	ST7_5	ST7_6	ST7_7	ST7_8	ST7_9	ST7_10			ST7_1	ST7_2	ST7_3	ST7_4	ST7_5	ST7_6	ST7_7	ST7_8	ST7_9	ST7_10																																												'
print(B)


# with open('fr.txt', 'w') as fr:
#     print(result.to_string(index=False, header=False), file=fr)

d = [x for x in range(216)]
with open('try.txt', 'w') as tre:
    print('<>', end='	', file=tre)
    for i in d:
        print(i+1, end='	', file=tre)
    print()
    print('\nA', end='	', file=tre)
    for i in range(216):
        print('',end='	', file=tre)


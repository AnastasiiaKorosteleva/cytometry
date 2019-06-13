import csv

'''function to split lists'''


def split_list(alist, wanted_parts=1):

    length = len(alist)
    return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts)]


'''reading the file'''
table = []
with open('2019-04-09_BCD057.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        table.append(row)

'''cut technical lines'''
data = table[6:]
names = table[2]


Tube_name = [data[i][0] for i in range(len(data))]
Sample_id = [data[i][1] for i in range(len(data)) if data[i][1].startswith('ST')]
Singlets = [data[i][2] for i in range(len(data))]
Intensities = [data[i][3] for i in range(len(data))]


Tube_name = [i.split('-') for i in Tube_name]
Concentrations = [Tube_name[i][1] for i in range(len(Tube_name))]
'''exclude isotype & unstained'''
indexes = []
for i in range(len(Concentrations)):
    if not Concentrations[i].isalpha():
        indexes.append(i)



Intensities = [Intensities[i] for i in indexes]
Concentrations = [i for i in Concentrations if not i.isalpha()]



first_string = [i+1 for i in range(216)]

with open('output.txt','w') as output:
    print('<>', *first_string, sep='\t', end='\t', file=output)
    print('\nA', '\t'*len(first_string), sep='\t', file=output)
    print('B\t', *Intensities[:10], '\t', *Intensities[60:70], sep='\t', end='\t',  file=output)
    print('\t'*193, file=output)
    print('C\t',*Intensities[10:20], '\t', *Intensities[70:80], sep='\t', end='\t',  file=output)
    print('\t'*193, file=output)
    print('D\t', *Intensities[20:30], '\t', *Intensities[80:90], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('E\t', *Intensities[30:40], '\t', *Intensities[90:100], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('F\t', *Intensities[40:50], '\t', *Intensities[100:110], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('G\t', *Intensities[50:60], '\t', *Intensities[110:120], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('H', '\t' * len(first_string), sep='\t', file=output)
    print('<>', *first_string, sep='\t', end='\t', file=output)
    print('\nA', '\t' * len(first_string), sep='\t', file=output)
    print('B\t', *Concentrations[:10], '\t', *Concentrations[60:70], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('C\t', *Concentrations[10:20], '\t', *Concentrations[70:80], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('D\t', *Concentrations[20:30], '\t', *Concentrations[80:90], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('E\t', *Concentrations[30:40], '\t', *Concentrations[90:100], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('F\t', *Concentrations[40:50], '\t', *Concentrations[100:110], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('G\t', *Concentrations[50:60], '\t', *Concentrations[110:120], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('H', '\t' * len(first_string),sep='\t', file=output)
    print('<>', *first_string, sep='\t', end='\t', file=output)
    print('\nA', '\t' * len(first_string),sep='\t', file=output)
    print('B\t', *Sample_id[:10], '\t', *Sample_id[60:70], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('C\t', *Sample_id[10:20], '\t', *Sample_id[70:80], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('D\t', *Sample_id[20:30], '\t', *Sample_id[80:90], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('E\t', *Sample_id[30:40], '\t', *Sample_id[90:100], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('F\t', *Sample_id[40:50], '\t', *Sample_id[100:110], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('G\t', *Sample_id[50:60], '\t', *Sample_id[110:120], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('H', '\t' * len(first_string), sep='\t', file=output)


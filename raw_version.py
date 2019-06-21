import csv
import datetime
import getpass
import sys

now = datetime.datetime.now()
time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)


'''reading the file'''
table = []
with open(sys.argv[1], newline='') as csvfile:
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
controls = []
for i in range(len(Concentrations)):
    if not Concentrations[i].isalpha():
        indexes.append(i)
    else:
        controls.append(i)


intensities = [Intensities[i] for i in indexes]
Controls = [data[i] for i in controls]
Concentrations = [i for i in Concentrations if not i.isalpha()]
first_string = [i+1 for i in range(216)]

'''replace ',' with ',' and reduce zeros'''

for i in range(len(Concentrations)):
    Concentrations[i] = Concentrations[i].replace('.', ',')
    if Concentrations[i] == '0':
        Concentrations[i] = '0,0000001'


'''output generating, very dirty way'''
with open('output.asc','w', encoding='ASCII') as output:
    print('<>', *first_string, sep='\t', end='\t', file=output)
    print('\nA', '\t'*len(first_string), sep='\t', file=output)
    print('B\t', *intensities[:10], '\t', *intensities[60:70], sep='\t', end='\t',  file=output)
    print('\t'*193, file=output)
    print('C\t',*intensities[10:20], '\t', *intensities[70:80], sep='\t', end='\t',  file=output)
    print('\t'*193, file=output)
    print('D\t', *intensities[20:30], '\t', *intensities[80:90], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('E\t', *intensities[30:40], '\t', *intensities[90:100], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('F\t', *intensities[40:50], '\t', *intensities[100:110], sep='\t', end='\t', file=output)
    print('\t' * 193, file=output)
    print('G\t', *intensities[50:60], '\t', *intensities[110:120], sep='\t', end='\t', file=output)
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
    print('Date of measurement: ', end='', file=output)
    print(now.year, now.month, now.day, sep='-', end='', file=output)
    print('/Time of measurement: ', end='', file=output)
    print(now.hour, now.minute, now.second, sep=':', file=output)
    print('Project: ADAL', file=output)
    print('Subject: Binding', file=output, )
    print('User:', getpass.getuser(),file=output)
    print('ST1: 1', file=output)
    print('ST2: 2', file=output)
    print('ST3: 3', file=output)
    print('ST4: 4', file=output)
    print('Number of plates: 2', file=output)
    print('---', file=output)


import csv
import datetime
import getpass
import sys
import os

now = datetime.datetime.now()
time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)

'''reading the file'''
table = []
with open(sys.argv[1], newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        table.append(row)


'''cut technical lines'''

data = table[3:]
names = table[2]

Tube_name = [data[i][0] for i in range(len(data))]
Sample_id = [data[i][1] for i in range(len(data)) if data[i][1].startswith('ST')]
Singlets = [data[i][2] for i in range(len(data))]
Intensities = [data[i][3] for i in range(len(data))]
Tube_name = [i.split('-') for i in Tube_name]
Concentrations = [Tube_name[i][1] for i in range(len(Tube_name))]


'''exclude isotype & unstained
get indexes where value in Concentration list != numeric'''
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

'''replace ',' with ',' and reduce zeros'''

for i in range(len(Concentrations)):
    Concentrations[i] = Concentrations[i].replace('.', ',')
    if Concentrations[i] == '0':
        Concentrations[i] = '0,1'

'''how many samples?'''

name = os.path.basename(sys.argv[1])[:-4]+'.asc'

project = input('Enter project name:')
subject = input('Enter subject name:')
act = input('Enter act#:')
first_sample = input('Enter sample 1 name: ')
second_sample = input('Enter sample 2 name: ')
third_sample = input('Enter sample 3 name: ')
fourth_sample = input('Enter sample 4 name: ')
fifth_sample = input('Enter sample 5 name: ')
sixth_sample = input('Enter sample 6 name: ')
plates = int(input('Number of plates: '))
'''tabs calculation'''
x = 0
if plates == 1:
    x = 345
elif plates == 2:
    x = 335
elif plates == 3:
    x = 325
'''output generating'''
first_string = [i+1 for i in range(360)]
try:
    with open(name, 'w', encoding='ASCII') as output:
        print('<>', *first_string, sep='\t', end='\t', file=output)
        print('\nA', '\t'*len(first_string), sep='\t', file=output)
        print('B\t', *intensities[:10], '\t', *intensities[60:70], '\t', *intensities[120:130],
              sep='\t', end='\t', file=output)
        print('\t'*x, file=output)

        print('C\t',*intensities[10:20], '\t', *intensities[70:80], '\t', *intensities[130:140],
              sep='\t', end='\t', file=output)
        print('\t'*x, file=output)
        print('D\t', *intensities[20:30], '\t', *intensities[80:90], '\t', *intensities[140:150],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('E\t', *intensities[30:40], '\t', *intensities[90:100], '\t', *intensities[150:160],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('F\t', *intensities[40:50], '\t', *intensities[100:110], '\t', *intensities[160:170],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('G\t', *intensities[50:60], '\t', *intensities[110:120], '\t', *intensities[170:180],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('H', '\t' * len(first_string), sep='\t', file=output)
        print('<>', *first_string, sep='\t', end='\t', file=output)
        print('\nA', '\t' * len(first_string), sep='\t', file=output)
        print('B\t', *Concentrations[:10], '\t', *Concentrations[60:70], '\t', *Concentrations[120:130],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('C\t', *Concentrations[10:20], '\t', *Concentrations[70:80], '\t', *Concentrations[130:140],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('D\t', *Concentrations[20:30], '\t', *Concentrations[80:90], '\t', *Concentrations[140:150],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('E\t', *Concentrations[30:40], '\t', *Concentrations[90:100], '\t', *Concentrations[150:160],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('F\t', *Concentrations[40:50], '\t', *Concentrations[100:110], '\t', *Concentrations[160:170],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('G\t', *Concentrations[50:60], '\t', *Concentrations[110:120], '\t', *Concentrations[170:180],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('H', '\t' * len(first_string), sep='\t', file=output)
        print('<>', *first_string, sep='\t', end='\t', file=output)
        print('\nA', '\t' * len(first_string),sep='\t', file=output)
        print('B\t', *Sample_id[:10], '\t', *Sample_id[60:70], '\t', *Sample_id[120:130],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('C\t', *Sample_id[10:20], '\t', *Sample_id[70:80], '\t', *Sample_id[130:140],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('D\t', *Sample_id[20:30], '\t', *Sample_id[80:90], '\t', *Sample_id[140:150],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('E\t', *Sample_id[30:40], '\t', *Sample_id[90:100],'\t',  *Sample_id[150:160],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('F\t', *Sample_id[40:50], '\t', *Sample_id[100:110], '\t', *Sample_id[160:170],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('G\t', *Sample_id[50:60], '\t', *Sample_id[110:120], '\t', *Sample_id[170:180],
              sep='\t', end='\t', file=output)
        print('\t' * x, file=output)
        print('H', '\t' * len(first_string), sep='\t', file=output)

        '''infobox'''
        print('Date of measurement: ', end='', file=output)
        print(now.year, now.month, now.day, sep='-', end='', file=output)
        print('/Time of measurement: ', end='', file=output)

        print(now.hour, now.minute, now.second, sep=':', file=output)
        print('Project:', project, file=output)
        print('Subject:', subject, file=output)
        print('User:', getpass.getuser(), file=output)
        print('Act:', act, file=output)
        print('ST1: {}'.format(first_sample), file=output)
        print('ST2: {}'.format(second_sample), file=output)
        print('ST3: {}'.format(third_sample), file=output)
        print('ST4: {}'.format(fourth_sample), file=output)
        print(('ST5: {}'.format(fifth_sample)), file=output)
        print(('ST6: {}'.format(sixth_sample)), file=output)
        print('Number of plates: ', plates, file=output)
        print('---', file=output)

        print('File successfully converted')
except:
    e = sys.exc_info()[0]
    print("<p>Error: %s</p>" % e)



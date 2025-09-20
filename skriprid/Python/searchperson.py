"""
Täiendus, lisaks näita mitu nime leiti
"""

import csv

filename='Persons.csv'
total = 0

phrase = input('Sisest otsitav fraas (min 2 märki): ')

if len(phrase) > 1:
    with open(filename, 'r', encoding='utf-8') as f:
        contents = csv.reader(f, delimiter=';')
        for row in contents:
            phrase = phrase.lower() # Tee väiketähtedeks
            first = row[0].lower() # Eesnimi väiketähtedeks
            last = row[1].lower() #perekonna nimi väiketähtedeks
            if phrase in first or phrase in last:
                print(';'.join(row)) #Tee list stringiks
                total += 1
        print(f'Leiti {total} nime')
else:
    print('Otsitav Fraas liiga kühike')

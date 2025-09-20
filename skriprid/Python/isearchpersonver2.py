filename='Persons.csv'
total = 0

phrase = input('Sisest otsitav fraas (min 2 märki): ')


if len(phrase.strip()) > 1:
    phrase = phrase.strip().lower()
    f = open(filename, 'r', encoding='utf-8')
    contents = f.readlines()[1:] #Alates teisest reast
    f.close() # Sulge fail
    for line in contents:
        line = line.strip() #Korrasta rida, eemalda \n
        if phrase in line.lower():
            print(line) # Väljasta rida
            total += 1 # Suurenda loendurit
    print(f'Leiti  {total} nime') # Leitud ridade/nimede arv.
else:
    print('Otsingu fraas on liiga lühike')
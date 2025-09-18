from datetime import datetime

name = 'raido suurmets' # Muutuja string (sõne) minu nimega
age = 39 # täisarv ehk int (integer)
height = 1.83 #ujuvkoma (float)

print (name,age,height) #Väljasta kolm väärtust

print (f'Kasutaja {name.title()} vanuse {age} ja pikkusega {height} meetrit istu lauataga.')

print ('Kasutaja ' + name.title() + ' vanuse ' + str(age) + ' ja pikkusega ' + str(height) + ' meetrit isus lauataga.')

#Arvutamine

birth_year = datetime.now().year - age
print (birth_year)

name = name.title() # Korrasta nimi ja kasutaja sama muutujat
print (name[1]) #Võtab teise tähe nimest
print (name [1:5]) #teiset 5-da kohani (5-dat ei võta) tähed.
print (name [6:]) # hakkab 6positsioonist
print (name [:5]) # Algusest esimesed 4 tähte
print (name [::-1]) # kirjutab tagurpidi.

age =int(input('Sisesta vanus: '))

if age < 1 or age > 123:
    print('Vanus on vales vahemikus, lubatud on 1-122')
elif age < 18:
    print ('Alakas!')
elif age < 65:
    print('Tööealine')
elif age < 100:
    print ('pensionäär')
else:
    print('pikaealised')
"""
Mitmerealine kommentaar

    """
    
place = input('Sisesta elukoht: ')
print(f'Sisestati {place}')

if len(place) > 1 and len(place) <= 7:
    print(f'Lühikese nimega koht {place.title()}')
elif len(place) > 7:
    print(f'Pika nimega koht {place.title()}')
else:
    print ('Koht liiga lühike')

# väljastaja muutujate andmetüübid

print(type(name))
print(type(age))
print(type(height))
print(type(place))


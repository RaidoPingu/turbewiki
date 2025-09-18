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


import random

names = ['Raido', 'Triinu', 'Mari', 'Jüri']

#Väljasta listis olevad nimed:

for name in names:
    print(name)

print()
# Teistmoodi väljastus # x= 0..3
for x in range(len(names)):
    print(names[x], random.randint(1, 122))

print()

# Lihtsalt numbrid
for x in range (1, 5):
    print(x, end=' ')
print('\n') #Kaks reavahetust

for x in range(0, 10, 2): #paaris arvud
    print(x, end=' | ')
print('\n')

# While loop

x= 0
while x < len(names):
    print(names[x])
    x += 1 # x= x + 1
print()

"""
Väljasta listi nimed iga nimi eraldi real, kuiud iga nime ees on järjekorra number. Järjekorra number algab ühega. Korrektne rida on järgnev.
1. Raido
2. Triinu
3. Mari
4. Jüri
"""
ages = []
print('Lahendus:')
for x in range(len(names)):
    ages.append(random.randint(1, 100))
    print(str(x+1) + '. ' +  names[x] + ' ' +str (ages[x]))
print(names)
print(ages)

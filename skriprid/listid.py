places = [] # tühi list

places.append('Kehtna') #Lisa Lõppu
places.append('Rapla') # Lisa lõppu
places [1:1] = ['Tallinn', 'Pärnu'] #lisa Kehtna ja Rapla vahele
places.extend(['Viljandi', 'Tartu', 'Rapla']) #lisab lõppu
places.insert(2, 'Are') #sisestab kohale 2 Tallinna ja pärnu vahele

print(places)

# Kustutamine
places.remove ('Rapla') # Kustutab esimese Rapla
places.pop(6) #Kustutab indexil 6 oleva eseme
del places [2] # Are kustutamine, indexil 3
 
print(places)

# Ülesanne: Lisa Rapla lõppu ja Peale Pärnut

places.append('Rapla')
places.insert(3, 'Rapla')

print(places)

place = places[-1] # Muutuja saab väärtuseks listi viimase elemendi
index = places.index(place) # Mitmes element on Rapla (ainult üks!)
count = places.count(place) #mitu Raplat on listis

# Kas rapla on nimekirjas
if place in places:
    print(f'{place} on nimekirjas')

#Teeme nimekirjast koopia:
list_copy=places.copy()
list_list = list(places) 

print (index, count) 
print (place)
print (list_copy)
print (list_list)

list_copy.sort() # A->Z
list_list.sort(reverse=True) # Z-> A
print() # tühi rida
print (list_copy)
print (list_list)

new_sorted_list = sorted(places, reverse=False) #A->Z
print (new_sorted_list)

# Tühjenda listi sisu
new_sorted_list.clear()
list_copy.clear()
list_list.clear()

print(new_sorted_list)
print(list_copy)
print(list_list)
print(places)

# Ülessanne Väljasta listi places viimane element ilma [-1] kasutama

print (places[len(places)-1])

# Väljasta konsooli elemendi pärnu keskmine täht trükitähena

print(places[2][2].upper())
# Versioon 2 samast asjast
city = places[2]
cahr = city[2].upper()
print(cahr)


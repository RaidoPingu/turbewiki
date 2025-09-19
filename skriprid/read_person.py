"""
Luua etteantud kasutajatele kasutajanimi ja eposti aadress
Kasutajanimi:
    eesnimi.perenimi
    eesnimes eemaldada tühi ja/või sidekriips Mari Liis, Mari-Liis
    eemaldada rõhumärgid ja täpitähed
    kasutajanimi on läbivalt väikeste tähtedega
Eposti aadress:
    Kasutajanimi@asutus.com
Kellel teha:
    Sündinud 1990-1999 k.a.
Uue faili sisu on:
Eesnimi;Perenimi;Isikukood;Kasutajanimi;EPost
Eesnimi;Perenimi;Sünniaeg;Sugu;Isikukood <-- originaal
"""
import csv
import unicodedata

src = 'Persons.csv' # algallinas
dst = 'Persons_account.csv' #uus fail
header = 'Eesnimi;Perenimi;Isikukood;Kasutajanimi;EPost' # Uue faILI PÄIS
domain = '@asutus.com' # eposti domeen

"""
Eemaldab rõhumärgid ja täpitähed

https://stackoverflow.com/questions/517923
"""
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

with open(src, 'r', encoding='utf-8') as f: # Avame lugemiseks faili
   with open(dst, 'w', encoding='utf-8') as d: # avame kirjutamiseks faili
        contents = csv.reader(f, delimiter=';') #loetav fail loetakse muutujasse läbi csv readeri
        d.write(header + '\n') # Kirjutame faili headeri ja reavahetuse
        next(contents) #vii lugemis järg järgmisele reale
        
        for row in contents:
            date = row[2] # Kuupäev eraldi muutujasse
            year = int(date.split('.')[2]) # võtame aasta välja kuupäevast
            if year >= 1990 and year <= 1999:
                first_name=row[0] #Eesnimi eraldi
                last_name=row[1] #Perenimi eraldi

                #Eemalda tühik ja sidekriips
                first_name = first_name.replace(' ', '') #Eemaldame tühikud
                first_name = first_name.replace('-', '') # Eemaldame Sidekriipsud

                #Kasutjanime loomine
                username = '.'.join([first_name, last_name]).lower() # Paneme ees ja perenime kokku
                username = strip_accents(username) #eemaldame rõhud ja täpitähed

                print(row[0], row [1], first_name, last_name, username)

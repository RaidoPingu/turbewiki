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
      


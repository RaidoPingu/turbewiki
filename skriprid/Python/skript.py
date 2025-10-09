import random
from datetime import datetime


def arvutame(sisend:list[int]):
    """
    Loen sisse listi ja võtab nendest välja summa, keskmise ja suurima arvu
    
    args:
        sisend[list]: Täisarvuline list
    
    returns:
        str: annab väärtused summa, keskmine, suurim.
    """
    # Kasutame sisse ehitatuid funktsioone sum, ja max ning keskmise arvutame.
    summa = sum(sisend) 
    keskmine = summa / len(sisend)
    suurim = max(sisend)

    # Väljastame kohe õigel kujul stringi mida väljastada

    return f'Summa: {summa} \nKeskmine: {keskmine:.2f} \nSuurim arv: {suurim}' 
time = datetime.now() # Kutsume välja 
vormindatud =time.strftime('%d.%m.%Y %H:%M:%S') # Vormindmae aja ära, et oleks nagu vaja 
filename = 'andmed.txt' # Genereeritava faili nimi
arvud =[] # Tühi list kuhu hiljem korjame arvud.

# Siit hakkab faili genereerimise ning kuupäeva ja juhuslike arvude salvestamise kood.

with open(filename, 'w', encoding='utf-8') as f: # Avame faili kirjutamiseks
    f.write(f'Kuupäev: {vormindatud} \n') # Kirjutame kohe kuupäeva faili
    f.write('Arvud: ') # Alustame uuelt realt sõnadega arvud
    count = 0 # Teeme While loopi jaoks counteri
    while count < 20: # While loop juhuslike arvude genereerimiseks
        nr = random.randint(1, 101) # Genereerime juhusliku arvu
        f.write(f' {nr}') # Kirjutame selle arvu faili
        count += 1 # Lisame +1 counterisse.

# Loeme faili sisse ja puhastame välja ainult arvud listi

with open(filename, 'r', encoding='utf-8' ) as f:
    contents = f.readlines()[1:] # Loeme faili sisu muutujasse, alates teisest reast
    for parts in contents: # Loop elementide lahti võtmiseks
        parts = parts.split() # Kaotame ära tühikud
        for part in parts: # teine loop mis võtab 1 elemendi
            if part.isdigit(): # Kontrollime kas on tegu arvuga
                arvud.append(int(part)) # Kui on arv lisame loodud tühja listi. 

#Võtame selle listi ja teem maagiat.

print(f'Failist loetud arvud {arvud}')
print(arvutame(arvud))


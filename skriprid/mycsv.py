filename = 'Create-MyCSV-v.csv'
column = 4 # veerg mida kokku liita
total = 0 #veeru summa

with open(filename, 'r') as f:
    contents = f.readlines() #Loeb faili sisu muutujasse
    for line in contents:
        line = line.strip() # Eemalda tühikud ja reavahetus
        parts = line.split(';') #tükelda semikoolinist
        if parts[column].isdigit(): #Kas kõik on numberid
            total += int(parts[column])

    print(total) #Test
        


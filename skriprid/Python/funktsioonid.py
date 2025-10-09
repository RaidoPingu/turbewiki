def welcome():
    """Väljastab staatilise tervitusteksti"""
    print('Tere, Kuidas läheb')

def welcome_name(name):
    """Tagastab tervitusesõnumi koos nimega"""
    return f'Tere, {name}'

def division(number1, number2):
    """
    Teostab kahe arvuga jagamistehte

    args: 
        number1(float): Jagatav arv 
        number2(float): Jagaja (ei tohi olla null)

    returns:
        float: Jagatise väärtus
    """
    if number2 != 0:
        return number1 / number2
    return -1

def introduce(name, age=25):
    """
    Loob lihtsa tutvustava lause.
    
    :param name: Isiku nimi
    :type: str
    :pram age: Isiku vanu (vaikimisi 25)
    :type age: int, valikuline
    :return: Tektiline tutvustus vormis
        'Tema on <nimi> ja ta on <vanus> aastane!
    :rtype: str
    """
    return f'Tema on {name} ja ta on {age} aastane!'


division()
welcome()
print(welcome_name('Raido'))
num1 = 10
num2 = 5

print(division(num1, num2))
print(division(num2, 0))

print(introduce('Raido'))
print(introduce('Raido', 39))



"""
Ülesanne: Loo list kome viie, väljasta viie nime tervitus.
"""

nimed = ['Raido', 'Triin', 'Jüri', 'Kass', 'Koer']
for nimi in nimed:
    print(welcome_name(nimi))


import random
print('one random number', random.randint(1, 100)) #losuje od 1 do 100
print('\n')

print('choosing random number from a range', random.choice(range(1, 100))) #zwraca element z podanego zakresu
print('\n')

print('choosing random number from a range - easier ', random.randrange(1, 100)) #łatwiejsza opcja tego co wyżej
print('\n')

lista = ['John', 'Tomasz', 'Peter', 'Susan', ' Emily', 'Greg', 'Chris'] #wymieszanie losowe pozycji w liście
random.shuffle(lista)
print('reordered list ', lista)
print('\n')

print('just a random float: ', random.random()) #losowa liczba typu float
print('\n')
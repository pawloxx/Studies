'''
Wyświetl zestawienie w postaci:

    A - 80%-10%
    D - less then 50%
    C - 50-60%
    B - 60%-80%
'''

slownik = {'A': '80%-10%', 'B': '60%-80%', 'C': '50%-60%', 'D': 'less then 50%'}

for key, value in slownik.items():
    print(key, '-', value)
"""
funkcja math
"""
f_smaller = 3.141592653589793
f_bigger = 3.87756392764
import math

print(math.ceil(f_smaller), math.ceil(f_bigger)) # zwraca najmniejszą liczbę całkowitą większą od podanej danej
print('\n')

print(math.floor(f_smaller), math.floor(f_bigger)) #zwraca największą liczbę która jest mniejsza od podanej danej
print('\n')

print(math.ceil(-f_smaller), math.ceil(-f_bigger)) #zwraca najmniejszą liczbę większą od podanej danej
print('\n')

print(math.floor(-f_smaller), math.floor(-f_bigger)) # zwraca największą liczbę mniejszą od przekazanego argumentu
print('\n')

print(pow(2, 8), pow(9, 0.5)) #potęgowanie i pierwiastkowanie
print('\n')

print(math.sqrt(16)) # pierwiastek 2go stopnia
print('\n')

print(math.pi, math.e) #w module math są też stałe (tutaj pi i e)
print('\n')

print(math.sin(math.pi/2), math.cos(math.pi/4)) #sinus i cosinus
print('\n')








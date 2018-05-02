# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:55:01 2018

@author: t.pawlowski
"""

#Lists
countries = ['FR','US','DE','RU','PL']
print(countries[1:3]) #tak jak z wyswietlaniem przy tekstach
countries.append('PL') #dodawanie do listy

print(countries)
#wstawianie wartosci do listy z wyznaczeniem pozycji wpisu w liscie
countries.insert(2,'ES')
print(countries)
#usuwanie wartosci z listy
countries.remove('RU')
#sortowanie wartosci na liscie
countries.sort()
print(countries)
#odwrocenie kolejnosci wartosci w liscie
countries.reverse()
print(countries)
#funkcja pop
print('pop',countries.pop(2))
#funkcja index
print('index',countries.index('PL'))
#zliczanie iloci wystąpień wartosci na liscie
print('count',countries.count('PL'))

#Tworzenie  i rozszerzanie istniejącej listy o wartosci z nowej
newList = ['FI','SE']
countries.extend(newList)
#wartosc listy mozna przypisac do innej listy
countriesCopy = countries.copy()
countries.clear()
print('countriesCopy',countriesCopy)

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:48:25 2018

@author: t.pawlowski
"""

#TYPY I ZMIENNE TRICKI

Title = 'Python'
print('Title is',type(Title))
#str
Version = 3
print(type(Version))
#int
Pr = 0.21
print(type(Pr))
#float

#sztuczki

x = 1
y = 1
z = 1
print(x,y,z)

a=b=c=2
print(a,b,c)
c = 3
print(a,b,c)

#kolejnoć wykonywania działań
print(2+2*2) #python jest zgodny z zasadami matematyki (nawiasy, kolejnoć działań)
print(6/2*(1+2))

#Potęgowanie
print(4**3**2)

#zmienianie wartosci zmiennych liczb

x=1
x = x+1
print(x)

x+=1
print(x)
x-=1
print(x)
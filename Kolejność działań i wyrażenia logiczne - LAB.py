# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:06:55 2018

@author: t.pawlowski
"""

#Kolejność działań i wyrażenia logiczne - LAB
#Sekcja 4, wykład 32

nrButa = 39
print((nrButa*5+50)*20+1018-1989)

2+2*2
7+7/7+7*7-7

'''
Wykładowca mówi studentom. Zaliczysz semestr jeżeli masz obecność co najmniej 
80% i średnią >= 3.0 lub zaliczyłeś pracę semestralną. Zbuduj wyrażenie w 
Python które stwierdzi czy student, który ma obecność 0.85, średnią 3.5 i 
nie zaliczył pracy semestralnej zda czy nie.
'''

obecnosc = 0.95
srednia = 2
pracaSem = False

zaliczysz = obecnosc >= 0.8 and srednia >= 3.0 and pracaSem == True
if zaliczysz is True:
    print('zaliczysz')
else:
    print('nie zdaałas')
    




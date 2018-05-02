# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 08:07:20 2018

@author: t.pawlowski
"""

#fn print LAB
'''
   1 Wyświetl napisy: TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV. Użyj jednego polecenia print
   2 Wyświetl w/w teksty używając jako separatora znaku ";"
   3 Korzystając z jednego polecenia print wyświetl napis (bez podtekstów!):
    I like computers but better is TVP1 but better is TVP2 but better is TVN but better is Polsat but better is BBC but better is HBO but better is MTV 
   4 Zadeklaruj zmienne ProgramName o wartości 'BBC', Item o wartości 'News'' i Time o wartości '18:00'. Nie używaj konkatenacji napisów (łączenia napisów). Użyj tylko polecenia print
    Wyświetl napis (zwróć uwagę na kropkę na końcu!):
    I like watching News at 18:00 on BBC .
   7 Zmień napis tak, aby kropka była zaraz za  BBC. Nadal nie korzystamy z konkatenacji ale z pojedyńczego polecenia print.
'''

#1
print('TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV')
#2
print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=';')
#3
print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=' but better is ')
#4
programName='BBC'
item='NEWS'
time='18:00'
print('I like watching ',item,' at ',time,' on ',programName+'.')
print('I like watching ',item,' at ',time,' on ',programName,'.',sep='')
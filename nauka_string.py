# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 08:39:12 2018

@author: t.pawlowski
"""

# zmienne, typy zmiennych
# string
atext='this is a text.'
print(atext.endswith('ext'))
print(atext.islower())
print(atext.upper())
print(atext.endswith('ext.'))
print(atext.upper().isupper())
print(atext.find('is'))
print(atext.find('is',3))
print(atext.replace('a','4'))
print(atext.replace('a','4').replace('i','1').replace('e','3'))

#split
print(atext.split(' '))
sthLikeNumber='1000'
#sprawdzanie zmiennej
print(sthLikeNumber.isdigit()) #czy liczba
print(sthLikeNumber.isdecimal()) #czy zmiennoprzecinkowa
print(sthLikeNumber.isalpha()) #czy są same litery
print(sthLikeNumber.isalnum()) #czy są same cyfry
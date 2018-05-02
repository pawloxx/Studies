# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:56:49 2018

@author: t.pawlowski
"""

#String jako tablica znaków
s="A Python script"
print(s[0]) #zwraca pierwszą pozycję ze zmiennej
print(s[0:7]) # zwraca ciąg od 0 do 7 ze zmiennej
print(s[:8])
print(s[8:])

message = 'Document "cv.doc" was printed on printer: XEROX'
#jak wydobyć tylko nazwę drukarki
print(message.find(':'))
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])
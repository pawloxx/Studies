# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 12:29:24 2018

@author: t.pawlowski
"""

#Minikalkulator
amountPLN=234
USD=3.65
EUR=4.23
ValueAsText='123.45'
factor=1.23

print('curr','\texchange','ammount')
print('USD','\t',USD,'\t',amountPLN/USD)
print('EUR','\t',EUR,'\t',amountPLN/EUR)

print('value is',ValueAsText,'factor is',factor,'value * factor=',float(ValueAsText)*factor,sep=' ')
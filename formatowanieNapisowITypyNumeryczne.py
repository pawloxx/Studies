# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:19:41 2018

@author: t.pawlowski
"""

#Formatowanie napisów i typy numeryczne - LAB

name = 'Chris'
age = 17
daysInYear = 365

'''
message = name+' is '+str(age)+' years old, so is about '+str(age*daysInYear)+' days old'
print(message)
message1 = '%s is %d years old, so is about %d days old'
print(message1 % (name,age,daysInYear*age))

message2 = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message2.format(name,age,age*daysInYear))

'''
a = 1234567890
b = 12345

message9 = '{0:d} divided by {1:d} is {2:d} and rest is {3:d}'

print(message9.format(a,b,a//b,a%b))


#zajebicie zaliczone
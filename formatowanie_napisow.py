# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:39:08 2018

@author: t.pawlowski
"""
'''
#Formatowanie napisów
message1='Processing file %s'
print(message1 % ('file_1.txt'))
message2='File %s has size %d KB'
print(message2 % ('file1_txt',100))

message3='File %20s has size %10d KB'
print(message3 %('File1.txt',100))
'''
#to jest spoko
message4 = 'File {0:s} has size {1:d}'
print(message4.format('file1.txt',100))

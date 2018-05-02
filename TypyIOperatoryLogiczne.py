# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:44:21 2018

@author: t.pawlowski
"""

#typy i operatory logiczne
isWeekend = True
print("Is weekend =",isWeekend)

Temperature = 20
print("Temperature =",Temperature)

ToDoList = ''
isHappy = isWeekend and Temperature >= 20 and ToDoList == '' \
or not isWeekend and not Temperature >= 20 and ToDoList != ''
print("IsHappy =",isHappy)
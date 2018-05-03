'''
Ciąg Fibonacciego to ciąg rozpoczynający się od 0 i 1 a każda kolejna liczba to suma dwóch poprzenich, np:

0
1
0+1 = 1
1+1 = 2
1+2 = 3
2+3 = 5
'''


fibIter = 6
a1 = 0
a2 = 1
a3 = 0

for i in range(fibIter):
    print(i, a3)
    a1 = a2
    a2 = a3
    a3 = a1 + a2
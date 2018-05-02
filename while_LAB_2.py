'''
ZADANIE 2
Dana jest liczba całkowita dodatnia number = 20730906, Oblicz sumę cyfr tej liczby.
'''

number = 20730906
tmpNumber = number
sumOfDigits = 0

while tmpNumber > 0:
    digit = tmpNumber % 10
    sumOfDigits += digit
    tmpNumber = tmpNumber // 10
else:
    print(sumOfDigits)
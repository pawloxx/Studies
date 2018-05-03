# sprawdzanie za pomocą pętli czy wyświetlona liczba jest parzysta

for number in range(1, 101):
    if number % 2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))
    ##print(x)
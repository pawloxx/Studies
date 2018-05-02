'''
wyszukiwanie wzorca w ciągu liczb
'''

values = [10, 43, 12, 48, 12, 11, 18, 98, 57, 28, 19, 27, 49, 19, 74]

i = 0
max = len(values) - 2

while i < max:
    print(i,values[i], values[i+1], values[i+2])
    if values[i] < values[i+1] and values[i+1] < values[i+2]:    #sprawdzamy czy ciąg 3 wartości w liście jest rosnący, jeśli tak to zwracamy te liczby.
        print('\tFound: ', values[i], values[i+1], values[i+2])
    i += 1


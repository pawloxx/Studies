f_smaller = 3.141592653589793
f_bigger = 3.87756392764

print(f_smaller, f_bigger)
print('\n')

print('rzutowanie na int ', int(f_smaller), int(f_bigger)) #rzutowanie na int
print('\n')

print('wartosc bezwzgledna ', abs(f_smaller), abs(-f_smaller)) # wartość bezwzględna
print('\n')

print('zaorkąglanie ', round(f_smaller, 2), round(f_bigger, 2), round(f_bigger, 3))
print('\n')

print(min(f_smaller, f_bigger), max(f_smaller, f_bigger))
print('\n')

list = [1, 2, 3, 4, 5, 6, 4, 8, 9, 10]

print(sum(list), len(list))
print('liczenie średniej', sum(list) / len(list))
print('\n')
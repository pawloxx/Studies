'''
zastosowanie funkcji random
'''

# wyświetlanie tabeli ASCII

#for i in range(32, 127):
#    print(i, chr(i))

# generowanie hasła
import random

ints = range(33, 127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))

print('password is: ', password)
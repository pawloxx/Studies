'''Write a short program that prints each number from 1 to 100 on a new line.
For each multiple of 3, print "Fizz" instead of the number. For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''

i = 1
iMax = 100
while i <= iMax:
   # print('i = ', i)
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')

    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print('i =', i)
    i += 1
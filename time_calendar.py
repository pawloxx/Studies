#playing with time
import time
print(time.time()) #sposób unixowy liczony od 1970-01-01
print('\n-----------------------------------------------------------------')
print('\n')
print(time.localtime(time.time())) #funkcja jako parametr przyjmuje czas unixowy (time.time) a zwraca tuple
print('\n-----------------------------------------------------------------')
print('\n')
print(time.asctime(time.localtime(time.time()))) #jako parametr przyjmuje time.time, która jako parametr przyjmuje time.time
print('\n-----------------------------------------------------------------')
print('\n')
print('current time is.... for human ', time.localtime(time.clock()))

import calendar
print('\n-----------------------------------------------------------------')
print('\n')
print(calendar.month(2017,9,w=5,l=2)) #kalendarz na dany miesiąc danego roku,
print('\n-----------------------------------------------------------------')
print('\n')
print(calendar.month(2017,9)) #bez karqs - bardziej kompaktowy kalendarz
print('\n-----------------------------------------------------------------')
print('\n')
print('week day is', calendar.weekday(2018, 5, 7)) #zwraca który to był dzień tygodnia
print('\n-----------------------------------------------------------------')
print('\n')
calendar.setfirstweekday(6) #wplywa tylko na to od którego dnia będzie rysowany kalendarz
print('\n-----------------------------------------------------------------')
print('\n')
print(calendar.month(2018, 5))
print('\n-----------------------------------------------------------------')
print('\n')
print('is 2020 a leap year?', calendar.isleap(2020)) #zwraca czy podany rok jest przestępny
print('\n-----------------------------------------------------------------')
print('\n')
print('Leap days 2000-2017', calendar.leapdays(2000, 2017))
print('Leap days 2017-2020', calendar.leapdays(2000, 2020))
print('Leap days 2020-2021', calendar.leapdays(2000, 2021)) # zwraca ilość dni prestępnych w podanym zakresie lat

print(calendar.calendar(2018))
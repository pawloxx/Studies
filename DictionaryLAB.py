# Dictionary LAB
'''
Nadal analizujesz wydajność kanałów, jakimi można dotrzeć do klientów. Każdorazowo po zmienie słownika wyświetl jego zawartość

1. Utwórz obiekt dictionary o nazwie chanels z następującymi kluczami i wartościami:

-Google - 1480
-Email - 300
-Natural Traffic - 440
-TV Spot - 700

2. Wyświetl wartość skojarzoną z kluczem "Email"

3. Utwórz nowy słownik chanelsUpdate z kluczami i wartościami:

-Natural Traffic -  520
-News - 600

4.Zaktualizuj słownik chanels wartościami z chanelsUpdate

5. Wyświetl wszystkie klucze z chanels

6. Usuń wartość 'Email' ze słownika
'''

chanels = {'Google':'1480', 'Email':'300', 'Nature Traffic':'440', 'TV Spot':'700'}
print(chanels['Email'])
chanelsUpdate = {'Natural Traffic':'520', 'News':'600'}
chanels.update(chanelsUpdate)

print(chanels.keys())
print(chanels.pop('Email'))
print(chanels)
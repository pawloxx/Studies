'''
Tym razem pomożemy lekarzom przeprowadzając wstępną analizę: czy pacjent ma grypę, czy tylko przeziębienie
(zakładamy, że pacjentowi coś dolega, w tym zadaniu mamy tylko pomóc zdiagnozować czy to jest grypa czy przeziębienie):

1, Utwórz 3 zmienne

-musclePain - wartość false
-fever - wartość true
-weakness - wartość true

2. Napisz wyrażenie if, które

-jeśli występuja wszystkie 3 objawy wyświetli komunikat "suspiction of influenza"
-w przeciwnym razie wyświetli "The flu is unlikely"

3. Napisz wyrażenie if, które:

-jeśli występuja wszystkie 3 objawy wyświetli komunikat "suspiction of influenza"
-jeśli wystęouje osłabienie (weakness) ale nie ma gorączki lub nie ma bólu mięśni to wyświetli "Just take a rest!"
-w przeciwnym razie wyświetli "you may be cold"

4. Mężczyźni przeziębienie przechodzą jak grypę... dodaj zmienną isMan o wartości true

5. Napisz wyrażenie if, które:

-komunikat o grypie wyświetli jeżeli występują wszystkie 3 objawy lub co najmniej jeden z nich o ile pacjent jest mężczyzną
-w pozostałych przypadkach zachowanie ma być jak w  poprzednim przykładzie
'''

musclePain = False
fervex = False
weakness = False
isMan = True

if musclePain and fervex and weakness:
    print('suspiction of influenza')
else:
    print('the flu is unlikely')
print('#2')

if musclePain and fervex and weakness:
    print('suspiction of influenza')
elif weakness and not (fervex and musclePain):
    print('just take a rest!')
else:
    print('you may be cold')
print('#3')

if (musclePain or fervex or weakness) and isMan:
    print('suspiction of influenza')
elif weakness and not fervex or not musclePain:
    print('just take a rest!')
else:
    print('you may be cold')
print('#5')


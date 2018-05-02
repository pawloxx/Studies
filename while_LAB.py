'''ZADANIE 1

Na konto została wpłacona kwota initialCapital w wysokości 20000.
Oprocentowanie na koncie to percent = 0.03.
Klient banku postanawia oszczędzać przez maxTimeYears = 10 lat.
Po każdym roku oszczędzania zarobiona kwota jest dodawana do oszczędności i zarabia
odsetki przez pozostały czas.

Zadeklaruj wymagane zmienne, a następnie stwórz pętlę, która
wyświetli informację o tym ile pieniędzy jest na koncie pod koniec
roku, kiedy odsetki się kapitalizują. Dodaj na zakończenie informację
o całkowitej kwocie zarobionej w banku.

'''

initialCapital = 20000
oprocentowanie = 0.03
maxTimeYears = 10
r = 1

while r <= maxTimeYears:
    print('po roku ', r, 'saldo wynosi', int(initialCapital + r * initialCapital * oprocentowanie))
    r += 1
else:
    print('Przez ', maxTimeYears, 'lat zarobiłeś', int(maxTimeYears * initialCapital * oprocentowanie), 'PLN')
print('wydawaj rozsądnie')
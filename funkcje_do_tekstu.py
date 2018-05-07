line = 'this IS a very STRANGE text'
print(line.capitalize()) #konwersja tekstu do zdania zaczynającego się dużą literą

print(line.title()) # każde słowo rozpoczyna się od wielkiej litery


polskie = 'chrząszcz'
print(line.upper())
print(line.lower())
print(line.swapcase())
print(line.casefold())
print(polskie.casefold())
print(polskie.replace('ą', 'a'))
print(line.count('e')) #liczenie krotności wystąpienia znaku w tekście
print(line.find('e')) #sprawdzanie od lewej na której pozycji znajduje się znak zwraca -1 gdy taki znak nie występuje
print(line.rfind('e')) #sprawdzanie od prawej na której pozycji znajduje się znak zwraca -1 gdy taki znak nie występuje
print(line.index('e'))
print(line.rindex('e'))

print(line.startswith('this')) #sprawdzanie czy tekst rozpoczyna się danym znakiem/ciągiem znaków
print(line.endswith('THIS')) #sprawdzanie czy tekst kończy się danym znakiem/ciągiem znaków

#przy tekście który jest długi można go zamknąć w """ """



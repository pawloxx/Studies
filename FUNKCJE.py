'''W tym ćwiczeniu użyjesz istniejącej funkcji oraz dodasz swoją własną, aby stworzyć w pełni funkcjonalny program.

    Dodaj funkcję nazwaną lista_korzysci() – która zwraca tablicę następujących napisów: "Lepiej zorganizowany kod",
    "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczenia go w
    calosc przez rozne osoby"

    Dodaj funkcję nazwaną buduj_zdanie(info), która otrzymuje pojedynczy argument zawierający napis i zwraca zdanie
    zaczynające się podanym napisem i kończące się " jest zaleta funkcji!"

    Wykonaj i zobacz jak funkcje ze sobą współpracują.
'''

def lista_korzysci(): pass
    tablica = ["Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu",
               "Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby"]
    return tablica


def buduj_zdanie(korzysc):
    return korzysc + "jest zaleta funkcji!"

def nazwij_korzysci():
    tabela = lista_korzysci()
    for korzysc in tabela:
        print buduj_zdanie(korzysc)
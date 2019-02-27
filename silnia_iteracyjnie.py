x = int(input("podaj liczbę: "))
def silnia_itr(x):
    ih = 1
    if x in (0, 1):
        return 1
    else:
        for i in range(2, x+1):
            ih = ih *i
        return ih
print(silnia_itr(x))
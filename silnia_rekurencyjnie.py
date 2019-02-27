"silnia rekurencyjnie"
x = int(input("Podaj liczbę: "))
def silnia(x):
    if x > 1:
        return x*silnia(x-1)
    elif x in (0,1):
        return 1;
print("Silnia z",x,"to",silnia(x))


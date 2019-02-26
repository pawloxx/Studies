"""prosta, staropolska kostka do losowania, argument określa max zakres"""
def kostka(x):
    from random import randint
    inoroz = True
    while inoroz:
        print("wypadlo",randint(1,x))
        print("Inoroz?")
        inoroz = ("t" or "tak") in input().lower()

kostka(100)
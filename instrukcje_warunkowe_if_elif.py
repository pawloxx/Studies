#if and elif

#zmienne
age = 17
isDrunk = False
isRestrictedArea = False

#to jest trudne do zrozumienia, zagnieżdżona instrukcja warunkowa, ale można łatwiej
if age < 18:
    print('za młody na alko')
else:
    if isDrunk:
        print('jestes pijany? nie moge Ci sprzedac alkoholu')
    else:
        if isRestrictedArea:
            print('alkohol jest tutaj zabrioniony')
        else:
            print('mozesz kupic u nas alko')
print('----')

#lepszy sposób

if age < 18:
    print('za młody na alko')
elif isDrunk:
    print('jestes pijany? nie moge Ci sprzedac alkoholu')
elif isRestrictedArea:
    print('alkohol jest tutaj zabrioniony')
else:
    print('mozesz kupic u nas alko')
# Tuplet,krotka - lista statyczna, którą trzeba skonwertować na listę żeby móc coś w niej zmieniać
tax = (4, 7, 8, 23)
print(tax)
print(tax[2])
print(tax[-1])
#sprawdzanie na której pozycji znajduje się wartość 7
print(tax.index(7))
#sprawdzanie ile razy dana wartość występuje w krotce
print(tax.count(8))
#sprawdzanie jaka jest najwyższa wartość w krotce
print(max(tax))
#zmiana krotki w listę (żeby móc coś w niej zmieniać
taxList = list (tax)
taxList.append(30)
#zmiana listy w tuple/krotkę

Newtax = tuple(taxList)
print(Newtax)

#przypisanie w locie do istniejącej krotki zmiennych odpowiadających jej zawartości
(tax1, tax2, tax3, tax4) = tax
print(tax1, tax2, tax3, tax4)

a=1
b=10
print("a =",a,"\tb=",b)
#temp = a
#a=b
#b=temp
print("a =",a,"\tb =",b)

#albo inaczej ale w tle
(a,b)=(b,a)
print("a =",a,"\tb =",b)
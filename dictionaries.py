# słowniki
#Tworzenie słownika
CountryLeaders={'PL':'Duda','US':'Trump'}
# dodawanie pozycji do słownika
CountryLeaders['DE'] = 'Merkel'
# zwracanie wartości dla elementu w słowniku
print(CountryLeaders['US'])
# Metody dla słownika
#print(CountryLeaders.keys())
#print(CountryLeaders.values())
#print(CountryLeaders.items())
#print(CountryLeaders.popitem())
#print(CountryLeaders.setdefault('FR', 'Macron'))
#print(CountryLeaders.get(('RU'))
NewLeaders = {'RU':'Putin', 'DE':'Schulz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)
print(CountryLeaders)




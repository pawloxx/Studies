# tworzenie listy mailowej używając pętli for

persons = ['Elizabeth', 'Steven', 'Sebastian', 'Margaret', 'Svetlana', 'Raphael']
domain = 'mycompany.com'

for person in persons:
    email = person + '@' + domain
    print('Email for\t', person, '\tis\t', email)
else:
    print('== end of the list --')
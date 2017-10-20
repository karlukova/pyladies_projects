from random import randint
nahodneCislo=randint(0,101)
print('Vybrala jsem cislo', nahodneCislo)
if nahodneCislo % 2 == 0:
    print('Cislo', nahodneCislo, 'je sude!')
else:
    print('Cislo', nahodneCislo, 'je liche!')

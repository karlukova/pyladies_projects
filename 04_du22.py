from math import factorial
cislo=int(input('Zadej cislo:'))
faktorial=factorial(cislo)
print('Faktorial cisla', cislo, 'je',faktorial)
if cislo>1:
    for n in (2, cislo):
        if cislo%n==0:
            print('Cislo', cislo, 'neni prvocislo')
        elif cislo%n!=0:
            print('Gratuluju! Cislo', cislo, 'je prvocislem!')
elif cislo<1:
    print('Cislo', cislo, 'neni prvocislo')

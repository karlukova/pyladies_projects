x='X'
i=int(input('Zadej cislo radku:'))
for cislo_radku in range(1, i+1):
    if cislo_radku==1 or cislo_radku==i:
        for n in range(1,7):
            print(x, end=' ')
        print(end='\n')
    else:
        print(x, x, sep='         ')

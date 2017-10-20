x='X'
for cislo_radku in range(1, 6):
    if cislo_radku==1 or cislo_radku==5:
        for n in range(1,7):
            print(x, end=' ')
        print(end='\n')
    else:
        print(x, x, sep='         ')
    

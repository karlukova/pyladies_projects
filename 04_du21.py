n=range(0,101)

for n in range(0,101):
    if n%3==0 and n%5==0:
        print('bum-bac')
    elif n%3==0:
        print(n,'bum')
    elif n%5==0:
        print('bac')
    else:
        print(n)    

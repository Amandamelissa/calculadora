from math import sqrt
def menu():
    print ('descobrir cateto ou hipotenusa? ')
    print ('[0] cateto')
    print ('[1] hipotenusa')
    print ('[2] sair')
def hipotenusa():
    ca = int(input ('cateto adjacente: '))
    co = int(input ('cateto oposto: '))
    h = sqrt (ca**2 + co**2)
    print (h)
def cateto():
    c1 = int(input('cateto: '))
    h = int(input('hipotenusa: '))
    c2 = sqrt (h**2 - c1**2)
    print (c2)
def pitagoras():
    while True:
        menu()
        escolha = int(input('escolha: '))
        if escolha == 0:
            cateto()
        elif escolha == 1:
            hipotenusa()
        elif escolha == 2:
            break
        else:
            print('voce nao escolheu nada')

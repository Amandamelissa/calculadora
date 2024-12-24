import math
def menu():
        print ('[0] descobrir o valor da enesima posicao')
        print ('[1] descobrir a posicao do valor X')
        print ('[2] descobrir o valor da soma da sequencia')
        print ('[3] sair')
def papg():
    print ('*********')
    print ('*pa & pg*')
    print ('*********')
    print ('------')
    print ('-menu-')
    print ('------')
    po = 0
    while po != 2:
        e1 = (input('pa[0], pg[1] ou sair[2]?'))
        if e1.isnumeric():
            e3 = int(e1)
            if e3 == 0:
                print ('------')
                print ('-menu-')
                print ('------')
                print (menu())
                e2 = (input('escolha: '))
                if e2.isnumeric():
                    e4 = int(e2)
                    if e4 == 0:
                        p = float(input('primeiro termo: '))
                        r = float(input('razao: '))
                        up = int(input('posicao: '))
                        u = p + (up-1) * r
                        print (f'A {up} posicao equivale a {u}')
                        print ('********************')
                        print ('[0] tentar novamente')
                        print ('[1] sair')
                        po =(input('escolha: '))
                        if po.isnumeric():
                            po1 = int(po)
                            if po1 == 0:
                                continue
                            elif po1 == 1:
                                break
                    elif e4 == 1:
                        a1 = float(input('primeiro termo: '))
                        r = float(input('razao: '))
                        n = int(input('posicao: '))
                        u = (r + n - a1) / r
                        print (f'A {n} posicao equivale a {u}')
                        print ('********************')
                        print ('[0] tentar novamente')
                        print ('[1] sair')
                        po = (input('escolha: '))
                        if po.isnumeric():
                            po1 = int(po)
                            if po1 == 0:
                                continue
                            elif po1 == 1:
                                break
                    elif e4 == 2:
                        p = float(input('A1: '))
                        u = float(input('An: '))
                        qn = float(input('quantidade de termos: '))
                        u = (p + u) * qn/2
                        print (f'o somatorio da pa equivale a {u}')
                        print ('********************')
                        print ('[0] tentar novamente')
                        print ('[1] sair')
                        po = (input('escolha: '))
                        if po.isnumeric():
                            po1 = int(po)
                            if po1 == 0:
                                continue
                            elif po1 == 1:
                                break
                    elif e4 == 3:
                        break
                    else:
                        print('voce escolheu nada')
                else:
                    print('voce escolheu nada')
            elif e3 == 1:
                print ('------')
                print ('-menu-')
                print ('------')
                print (menu())
                e2 = (input('escolha: '))
                if e2.isnumeric():
                    e4 = int(e2)
                    if e4 == 0:
                        a1 = float(input('primeiro termo: '))
                        q = float(input('razao: '))
                        an = int(input('posicao: '))
                        u = a1 * q ** (an-1)
                        print (f'A {an} posicao equivale a {u}')
                        print ('********************')
                        print ('[0] tentar novamente')
                        print ('[1] sair')
                        po = (input('escolha: '))
                        if po.isnumeric():
                            po1 = int(po)
                            if po1 == 0:
                                continue
                            elif po1 == 1:
                                break
                    elif e4 == 1:
                        a1 = float(input('primeiro termo: '))
                        q =  float(input('razao: '))
                        an = float(input('termo a ser procurado '))
                        u =  math.log (an*q/a1, q)
                        if u %1 != 0:
                            print (f'{an} nao pertence a pg')
                        else:
                            print (f'A {an} posicao equivale a {u}')
                        print ('********************')
                        print ('[0] tentar novamente')
                        print ('[1] sair')
                        po = (input('escolha: '))
                        if po.isnumeric():
                            po1 = int(po)
                            if po1 == 0:
                                continue
                            elif po1 == 1:
                                break
                    elif e4 == 2:
                        i = int(input('finita[0] ou infinita[1]?'))
                        a1 = float(input('A1:'))
                        q = float (input('razao: '))
                        if i == 0:
                            an = float(input('An: '))
                            n = int(input('quantidade de termos: '))
                            u = (a1 * (q ** n - 1 )) / (q-1)
                            print (f'o somatorio da pg equivale a {u}')
                            print ('********************')
                            print ('[0] tentar novamente')
                            print ('[1] sair')
                            po = (input('escolha: '))
                            if po.isnumeric():
                                po1 = int(po)
                            if po1 == 0:
                                continue
                            elif po1 == 1:
                                break
                        elif i == 1:
                            u = (a1) / (1-q)
                            print (f'o somatorio da pg equivale a {u}')
                            print ('********************')
                            print ('[0] tentar novamente')
                            print ('[1] sair')
                            po = (input('escolha: '))
                        if po.isnumeric():
                            po1 = int(po)
                            if po1 == 0:
                                continue
                            elif po1 == 1:
                                break
                    elif e4 == 3:
                        break
                    else:
                        print('voce escolheu nada')
                        print ('[0] tentar novamente')
                        print ('[1] sair')
                        po = (input('escolha: '))
                        if po.isnumeric():
                            po1 = int(po)
                            if po1 == 0:
                                continue
                            elif po1 == 1:
                                break
            elif e3 == 2:
                break
            else:
                print ('voce escolheu nada, tente novamente')
        else:
            print ('voce escolheu nada, tente novamente.')


def sequencia(termos):
    n1 = 1
    n2 = 1
    n3 = 0
    print (n1)
    print (n2)
    for termos in range(0,termos-2):
        n3 = n2 + n1
        print (n3)
        n1 = n2
        n2 = n3

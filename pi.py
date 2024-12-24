import math
def pi():
    numerador = 4
    denominador = 3
    pi = 3
    termos = int(input('termos: '))
    for termo in range (0,termos):
        pi =((numerador / ((denominador-1)* denominador * (denominador+1)))+pi)
        numerador = numerador * -1
        denominador = denominador + 2
        print(pi)
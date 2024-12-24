valores = [0.01 , 0.05 , 0.10, 0.25 , 0.50 , 1 , 2 , 5 , 10 , 20 , 50 , 100]
usadas = []

def troco():
    i = valores[-1]
    a = -1
    troco = round(float(input('troco: ')) , 2)
    while troco > 0:
        if troco >= round(i , 2):
            troco = round(troco - round(i , 2), 2)
            usadas.append(i)
        else:
            a = a - 1
            i = valores[a]
def notas():
    i = valores[-1]
    a = -1
    for valor in valores:
        if usadas.count(i) > 0:
            print(i , ' x ' , usadas.count(i))
        if a > -12:
            a = a - 1
            i = valores[a]
        else:
            break
    
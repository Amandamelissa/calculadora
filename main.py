import math
import fibonacci
import PaEPg
import pitagoras
import primos
import funcoes
def menu():
    print ('calculadora')
    print ('o quer voce quer fazer?')
    print ('[0] soma')
    print ('[1] subtracao')
    print ('[2] multiplicacao')
    print ('[3] divisao')
    print ('[4] exponenciacao')
    print ('[5] raiz quadrada')
    print ('[6] fibonacci')
    print ('[7] pa/pg')
    print ('[8] pitagoras')
    print ('[9] checagem de numeros primos')
    print ('[10] calcular troco')
    print ('[11] sair')
def soma(): 
    print ('digite 0 para parar')
    numero = 1
    total = int(0)
    while numero != 0:
        numero = int(input('numero a somar: '))
        total = total + numero 
        print (total)
def subtracao():
    print ('digite 0 para parar')
    numero = 1
    total = int(input('numero inicial: '))
    while numero != 0:
        numero = int(input('numero a subtrair: '))
        total = total - numero
        print (total)
def multiplicacao():
    print ('digite 1 para parar')
    numero = 0
    total = int(1)
    while numero != 1:
        numero = int(input('numero a multiplicacao: '))
        total = total * numero 
        print (total)
def divisao():
    print ('digite 1 para parar')
    numero = 0
    total = int(input('numero a ser dividido: '))
    while numero != 1:
        numero = int(input('numero a dividir: '))
        if numero == 0:
            print ('erro')
            break
        total = total / numero 
        print (total)
def exponenciacao(): 
    print ('digite 1 para parar')
    numero = 0
    total = int(input('base: '))
    while numero != 1:
        numero = int(input('expoente: '))
        total = total ** numero
        print (total)
def raizquadrada(): 
    total = int(input('radical: '))
    if total <= 0:
        print ('valor inexistente')
    total = math.sqrt(total)
    print (total)
operacao = 0
while True:
    menu()
    operacao = int(input('escolha: '))
    if operacao == 0:
        soma()
    elif operacao == 1:
        subtracao()
    elif operacao == 2:
        multiplicacao()
    elif operacao == 3:
        divisao()
    elif operacao == 4:
        exponenciacao()
    elif operacao == 5:
        raizquadrada()
    elif operacao == 6:
        tamanho = int(input('tamanho da sequencia: '))
        fibonacci.sequencia(tamanho)
    elif operacao == 7:
        PaEPg.papg()
    elif operacao == 8:
        pitagoras.pitagoras()
    elif operacao == 9:
        primos.primos()
    elif operacao == 10:
        funcoes.troco()
        funcoes.notas()
    elif operacao == 11:
        print ('tchau!')
        break
    else:
        print('voce escolheu nada, tente novamente')
        continue


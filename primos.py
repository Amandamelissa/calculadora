def primos():
    numero = int(input('numero a ser checado: '))
    divisor = int(2)
    primo = True
    while divisor < numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor = divisor + 1
    if primo:
        print('primo')
    else:
        print(f'nao e primo, pois e divisivel por {divisor}')

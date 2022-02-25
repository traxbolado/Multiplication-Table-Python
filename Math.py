print(".___________..______           ___      ___   ___ ")
print("|           ||   _  \         /   \     \  \ /  / ")
print("`---|  |----`|  |_)  |       /  ^  \     \  V  /  ")
print("    |  |     |      /       /  /_\  \     >   <   ")
print("    |  |     |  |\  \----. /  _____  \   /  .  \  ")
print("    |__|     | _| `._____|/__/     \__\ /__/ \__\ ")
print("\n")

print('=============[Calc]=============')
print("=    [1] Multiplicação         =")
print("=    [2] Soma                  =")
print("=    [3] Subtração             =")
print("=    [4] Divisão               =")
print('================================ \n')

Area = input("Escolha alguma alternativa acima: ")

if Area == '1':
    print('[Multiplicação] Digite um valor: ')
    valor1 = int(input())

    print('[Multiplicação] Digite outro valor: ')
    valor2 = int(input())

    resultado = (valor1 * valor2)

    print(f'[Multiplicação | Resultado] {valor1} x {valor2} = {resultado}')

if Area == '2':
    print('[Soma] Digite um valor: ')
    valor1 = int(input())

    print('[Soma] Digite outro valor: ')
    valor2 = int(input())

    resultado = (valor1 + valor2)

    print(f'[Soma | Resultado] {valor1} + {valor2} = {resultado}')

if Area == '3':
    print('[Subtração] Digite um valor: ')
    valor1 = int(input())

    print('[Subtração] Digite outro valor: ')
    valor2 = int(input())

    resultado = (valor1 - valor2)

    print(f'[Subtração | Resultado] {valor1} - {valor2} = {resultado}')

if Area == '4':
    print('[Divisão] Digite um valor: ')
    valor1 = int(input())

    print('[Divisão] Digite outro valor: ')
    valor2 = int(input())

    resultado = (valor1 / valor2)

    print(f'[Divisão | Resultado] {valor1} ÷ {valor2} = {resultado}')

while True:
    Area = input("Escolha alguma alternativa acima: ")

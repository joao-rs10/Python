#5. Escreva um algoritmo que solicite quinze números informados pelo usuário e exiba a raiz quadrada
#de cada número (Dica: importe a biblioteca math).

import math

for i in range(1, 16):
    num = float(input(f"Digite um número: "))
    raiz = math.sqrt(num)
    print(f"A raiz quadrada de {num} é {raiz:.2f}")
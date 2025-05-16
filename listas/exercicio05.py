#Preencha a lista com 10 números aleatórios. Na sequência, solicite um número ao
#usuário e informe quantas vezes esse número aparece na lista.

import random
lista = []
for i in range(10):
    num = random.randint(1,10)
    lista.append(num)
print(lista)

n = int(input("Informe um número: "))
quantidade = 0
for item in lista:
    if item == n:
        quantidade += 1
print(f"Aparece {quantidade} vezes")
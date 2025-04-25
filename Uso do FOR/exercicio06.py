#6. Criar um algoritmo que leia dez números inteiros e informe o maior e o menor número
n = int(input("Número: "))
maior = n
menor = n
for i in range(9):
    n = int(input("Número: "))

    if n > maior:
        maior = n

    if n < menor:
        menor = n



print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")



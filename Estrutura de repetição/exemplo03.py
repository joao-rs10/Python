#Solicitar 10 números e contar quantos sao pares e quantos sao negativos

cont =1
cont_pares = 0
cont_negativo = 0
cont_impares = 0
while cont <= 10:
    numero = int(input("Número: "))
    if numero % 2 == 0:
        cont_pares += 1       #conta os números pares
    else:
        cont_impares +=1
    if numero < 0:
        cont_negativo += 1
    cont += 1
print(f"Quantidade de números pares é:  {cont_pares}")
print(f"Quantidade de números negativos é: {cont_negativo}")
print(f"Quantidade de númers impares é: {cont_impares}")
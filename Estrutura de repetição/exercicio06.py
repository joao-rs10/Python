#Escreva um algoritmo que solicite 10 números e informe qual foi o menor número digitado.

print("Escreva 10 números.")
cont = 1
primeiro_numero = int(input("Número: "))
menor_numero = primeiro_numero
while cont <=9:
    numero = int(input("Número: "))
    if numero < menor_numero:
        menor_numero = numero
    cont +=1
print(f"O menor número é: {menor_numero}")
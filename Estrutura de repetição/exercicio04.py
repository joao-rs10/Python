#Faça um algoritmo que solicite N números e calcule a média dos números pares e a
# média dos números ímpares (o valor de N deve ser solicitado ao usuário no início do programa).

cont = 1
cont_pares = 0
cont_impares = 0

print('Escreva 10 números')

while cont <=10:
    numero= int(input('Numero: '))
    if numero %2 == 0:
        cont_pares += numero
    else:
        cont_impares += numero
    cont += 1
    mediapar = cont_pares / 10
    mediaimpar = cont_impares / 10

print(f"A média dos numeros pares é: {mediapar}")
print(f"A média dos numeros impares é: {mediaimpar}")

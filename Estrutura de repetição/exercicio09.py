#Fazer um algoritmo que solicite um número inteiro N qualquer e exiba a tabuada de N.

cont = 1
num= int(input("Número: "))

while cont <= 10:
    print(f"{num * cont}")
    cont += 1
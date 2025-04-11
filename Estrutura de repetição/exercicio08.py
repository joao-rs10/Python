#Fazer um algoritmo que exiba na tela todos os números ímpares de 1 a n, onde n é fornecido pelo usuário.

cont = 1
numeros= int(input("Até que número você gostaria de saber quantos números impares tem? "))
while cont <= numeros:
    if cont % 2 != 0:
        print(cont)
    cont += 1



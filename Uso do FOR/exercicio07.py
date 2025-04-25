#7. Escreva um algoritmo que solicite um número inteiro e exiba todos os divisores desse número
num = int(input("Número: "))

for i in range(1,num+1):
    if num % i == 0:
        print(f"Os divisores sao: {i}")



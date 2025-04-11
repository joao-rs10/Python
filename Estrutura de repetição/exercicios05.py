# Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo
# deve solicitar os números novamente) e informe a soma entre os números.

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

while num1 == num2:
    print("Digite números diferentes")
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

soma = num1 + num2
print(f"A soma dos números é: {soma}")





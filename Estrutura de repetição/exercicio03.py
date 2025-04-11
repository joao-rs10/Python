# Solicite vários números ao usuário (até que ele digite o número zero) e informe o  somatório dos números digitados.

cont = 1
soma_numeros = 0

while True:
    numero = int(input("Digite o número para somar: "))
    if numero <= 0:
        break
    soma_numeros += numero
    cont += 1
print(f"A soma dos números digitados é: {soma_numeros}")



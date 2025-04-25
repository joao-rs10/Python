#Solicitar a idade de 10 pessoas e calcular as medias
soma = 0

n = int(input("Quantidade de pessoas: "))

for cont in range(n):
    idade = int(input("Informe a idade: "))
    soma += idade
media = soma/n
print(f"Media das idades: {media}")
nome =(input("Digite o nome do vendedor: "))

carrovendido =float(input("Digite a quantidade de carros vendidos: "))

total =float(input("Digite o valor total das vendas: "))

final= 2500 + 200 * carrovendido + total * 0.02
print(f"O salário do(a) vendedor(a) {nome} será de: {final}")

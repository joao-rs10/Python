salario = float(input("Digite seu salário fixo: "))
vendas = float(input("Digite o valor total de vendas: "))

vendasmenor= (vendas * 0.03) + salario
vendasmaior= (vendas * 0.05) + salario

if vendas <= 1500:
    print(f"Seu salário será de {vendasmenor} R$")
elif vendas > 1500:
    print(f"Seu salário sera será de {vendasmaior} R$")
    
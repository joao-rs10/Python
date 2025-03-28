carro= int(input("Digite o valor do custo de fabríca do carro: "))

impostos= 45/100 * carro
distribuidor= 28/100 * carro
consumidor= impostos + distribuidor + carro

print(f"Valor do custo ao consumidor será de {consumidor} R$")
#Escreva um algoritmo que solicite a idade de 10 pessoas e informe a quantidade de pessoas com idade inferior a 18 anos.


cont = 1
cont_idade = 0

while cont <=10:
     idade= int(input('Informe a idade: '))
     if idade < 18:
         cont_idade += 1
     cont += 1

print(f"A quantidade de pessoas menor de idade é: {cont_idade}")

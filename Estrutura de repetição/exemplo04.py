#Solicitar a idade de 10 pessoas e calcular a média dessas pessoas.
#Finalizar quando o usuário informar uma idade negativa.

conta_idade = 0
soma_idade = 0

while True:                 #loop infinito
    idade = int(input("Informe a idade: "))
    if idade < 0:
        break                    # interrompe um loop
    soma_idade += idade
    conta_idade += 1


print(soma_idade)
if conta_idade > 0:
    media= soma_idade / conta_idade
    print(f"Média de idade das pessoas: {media:.2f}")
else:
    print('Idade inválida')



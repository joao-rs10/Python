a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))

print("1-soma")
print("2-subtração")
print("3-multiplicação")
print("4-divisão")
opcao=int(input("escolha uma das opcções acima: "))

if opcao == 1:
    print(f"Resultado da soma é: {a+b} ")
elif opcao == 2:
    print(f"Resultado da subtração é: {a-b} ")
elif opcao == 3:
    print(f"Resultado da multiplicção é: {a*b} ")
elif opcao == 4:
    if b != 0:
        print(f"Resultado da divisão é: {a / b}")
    else:
        print("Não é possível fazer uma divisão por zero.")
else:
    print('Opção inválida.')

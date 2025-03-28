horas = int(input("Digite um número inteiro: "))
minutos = int(input("Digite outro número inteiro: "))

if horas > 23:
    print('hora invalida.')
elif minutos > 59:
    print("minuto invalido invalida")
else:
    print(f"A hora é {horas}:{minutos}")
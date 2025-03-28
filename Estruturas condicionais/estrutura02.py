media= float(input("Digite sua média: "))
faltas= int(input("Quantidade de faltas: "))

if media >= 6:
    if faltas <= 20:
        print("Aprovado.")
    else:
        print("Reprovado por faltas.")
else:
    print("Reprovado por média.")
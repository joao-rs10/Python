nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))
nota3= float(input("Digite a terceira nota: "))

media= (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'aprovado, sua média foi de: {media}')
else:
    print(f'reprovado, sua média foi de: {media}')
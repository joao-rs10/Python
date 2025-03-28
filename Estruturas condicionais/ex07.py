num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite um número inteiro: "))

if num1 > num2:
    print(f"{num1}")
elif num2 > num1:
    print(f"{num2}")
elif num1 == num2:
    print("Os números são iguais.")
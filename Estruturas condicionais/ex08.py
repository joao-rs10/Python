num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite um número inteiro: "))
num3= int(input("Digite um número inteiro: "))

if num1 < num2 and num1 < num3:
    print(f"{num1}")
elif num2 < num1 and num2 < num3:
    print(f"{num2}")
elif num3 < num1 and num3 < num2:
    print(f"{num3}")

elif num1 == num2 == num3:
    print('Os números sao iguais.')
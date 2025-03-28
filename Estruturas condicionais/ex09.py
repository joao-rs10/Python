num1= float(input("Digite o valor do lado 1: "))
num2= float(input("Digite o valor do lado 2: "))
num3= float(input("Digite o valor do lado 3: "))

if num1 == num2 == num3:
    print("Triângulo equilátero")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Triângulo isóceles")
else:
    print("Triâgulo escaleno")
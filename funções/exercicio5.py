#Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada area
#que calcula e retorna a área do círculo e outra função chamada perimetro que calcula e retorna o
#perímetro do círculo. Utilize as fórmulas abaixo
#Área = π * r2
#Perímetro = π * 2 * r

def area(raio):
    area = 3.14 * raio ** 2
    print(f"O valor da area é: {area}")
def perimetro(raio):
    perimetro = 3.14 * 2 * raio
    print(f"O valor do perimetro é: {perimetro}")

raio = int(input("Insira o valor do raio: "))
area(raio)
raio = int(input("Insira o valor do raio: "))
perimetro(raio)


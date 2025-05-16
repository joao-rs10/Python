def exibe_mensagem():
    print("Exemplo do programa utilizando funções")


def numero_primo(numero):
    cont = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            cont += 1
    if cont == 2:
        print(f"O número {numero} é Primo")
    else:
        print(f"O número {numero} não é Primo")


def soma(a, b):
    c = a + b
    print(f'A soma de {a} + {b} = {c}')


def criar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        n = int(input("Numero: "))
        lista.append(n)
    return lista


def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media


# programa principal
exibe_mensagem()

n = int(input("Digite um numero: "))
numero_primo(n)

soma(10, 20)

t = int(input("Informe o tamanho da lista: "))
lista = criar_lista(t)
print(lista)

print(f"Média da lista: {calcular_media(lista):.2f}")

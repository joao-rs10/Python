#Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#a. A média aritmética dos números armazenados na lista.
#b. O somatório dos números pares armazenados na lista.

lista_media=[]
lista_soma=[]
for i in range(10):
    num= int(input("Digite um número: "))
    lista_media.append(num)
    media = sum(lista_media) / len(lista_media)
    if num % 2 == 0:
        lista_soma.append(num)
print(sum(lista_soma))
print(media)


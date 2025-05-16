#Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, e
#os números ímpares em outra lista. Exiba as duas listas ao usuário.
lista_par=[]
lista_impar=[]
for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
print(lista_par)
print(lista_impar)


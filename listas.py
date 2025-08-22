#TUPLA
#Estrutura heterogênea
#Estrutura imutável

tupla = (2, 5, 7, 210, 40)
print(tupla)

#tupla vazia
tupla = ()
print(tupla)

#tupla com 1 elemeto
tupla = (10,)
print(tupla)


tupla = (2, 5, 7, 210, 40)
print(tupla[1])

indice = tupla.index(7)
print(indice)

print(max(tupla))
print(min(tupla))
print(sum(tupla))

for item in tupla:
    print(item)

#operação de conversão
# list: converte uma tupla em lista

tupla = (3, 4, 6)
lista = list(tupla)
print(lista)
lista.append(100)
lista.append(300)
print(lista)


# Tupla: converte uma lista em tupla
tupla = tuple(lista)
print(lista)

# preencher tupla

lista = []
for i in range(5):
    numero = int(input("Numero: "))
    lista.append(numero)
print(lista)
tupla = tuple(lista)
print(tupla)
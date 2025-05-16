lista = [3, 10, 6, 1, 4, 5, 4, 10]
print(lista)

# len(lista): retorna o tamanho da lista
print(len(lista))

# max(lista): retorna o maior valor
print(max(lista))

# min(lista): retorna o menor valor
print(min(lista))

nomes = ['Paulo', 'Ana', 'Joao']
print(max(nomes))

# sum(lista): retorna o somatório da lista
print(sum(lista))

media = sum(lista) / len(lista)
print(media)

# append(item): insere um item no final da lista
lista = [4, 6, 10, 3, 4, 3, 1, 3,3,3,3,3, 200, 200]
lista.append(100)
print(lista)
lista.append(200)
print(lista)

# insert(indice, item): insere um item em um indice especifico da lista
lista.insert(0, 300)
print(lista)

# pop(indice): remove um item de um índice
lista.pop(2)
print(lista)

# remove(item): remove a primeira ocorrencia de um item
lista.remove(100)
print(lista)

# remover todas as ocorrencia de um item
while 3 in lista:
    lista.remove(3)
print(lista)

# index(item): retorna o indice da primeira ocorrencia de um item na lista
print(lista.index(200))

# lista.sort(): ordena uma lista em ordem crescente
lista = [5, 8, 10, 4, 1, 200, 60]
lista.sort()
print(lista)

# lista.sort(reverse=True): ordena uma lista em ordem decrescente
lista = [5, 8, 10, 4, 1, 200, 60]
lista.sort(reverse=True)
print(lista)

nomes = ["Joao", "Pedro", "Ana"]
nomes.sort()
print(nomes)

# count(item): Retorna a quantidade de ocorrencia de um item
lista = [4, 6, 6, 4, 7, 8, 9, 6]
print(lista.count(6))

# concatenação de listas
lista1 = [4, 6, 7, 8]
lista2 = [100, 200, 4]
lista3 = lista2 + lista1
print(lista3)
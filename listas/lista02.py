# ------------------------------------------------------------------------------
# LISTA

# Armazena uma coleção de itens, organizados sequencialmente.
# Os itens são delimitados por colchetes [ ] e separados por vírgulas.
numeros = [5, 6, 20, 10, 3, 25]
print(numeros)

nomes = ['Ana', 'Paulo', 'João', 'Fernando', 'Marcela']
print(nomes)

# Listas são estruturas heterogêneas (podem armazenar dados de tipos diferentes)
lista = [1, 4, 5.99, 5.23, 'Ana', 'Paulo']
print(lista)

# Lista vazia
lista = []
print(lista)

# Índices: representam a posição de cada item.
# O primeiro item sempre é zero.
# São utilizados para acessar um item específico da lista.
lista = [3, 6, 19, 89]
print(lista[2])
print(lista[0])
soma = lista[0] + lista[2]
print(soma)

# Índices negativos: acessam a lista a partir do último item.
# O último item sempre é -1.
lista = [3, 6, 19, 89]
print(lista[-1])
print(lista[-2])
print(lista[-3])

# ------------------------------------------------------------------------------
# Alterar um item da lista
lista = [3, 6, 19, 89]
lista[0] = 100
lista[-1] = 200
print(lista)

# Inserir um item no final da lista
lista = [3, 6, 19, 89]
lista.append(500)
lista.append(600)
print(lista)

# Inserir um item em um índice específico
lista = [3, 6, 19, 89]
lista.insert(1, 500)
print(lista)

# remover item da lista
lista = [3, 6, 19, 89]
lista.pop(0)
print(lista)
lista.pop(2)
print(lista)

# Verificar o tamanho de uma lista
tamanho = len(lista)
print(tamanho)

# ------------------------------------------------------------------------------
# Preencher uma lista com entradas do usuário (tamanho fixo)
lista_nomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)
print(lista_nomes)

# Preencher uma lista com entradas do usuário (tamanho indeterminado)
lista_nomes = []
while True:
    nome = input("Digite um nome: ")
    if nome == "":          # encerra quando usuário informar um nome vazio
        break
    lista_nomes.append(nome)
print(lista_nomes)

# ------------------------------------------------------------------------------
# Percorrer os itens da lista
lista = [4, 7, 10, 45, 22, 100]
for item in lista:
    print(item)

# Exemplo:
# Contar a quantidade de números ímpares da lista
cont = 0
for item in lista:
    if item % 2 != 0:
        cont += 1
print(f'Quantidade de impares: {cont}')

# ------------------------------------------------------------------------------
# Pecorrer os índices da lista
lista = [5, 70, 55, 7, 9, 20]
for i in range(len(lista)):         # 0,1,2,3,4,5
    print(lista[i])

# Exemplo:
# Substituir os números ímpares da lista por zero
for i in range(len(lista)):         # 0,1,2,3,4,5
    if lista[i] % 2 != 0:
        lista[i] = 0
print(lista)
# ------------------------------------------------------------------------------

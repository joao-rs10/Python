#Solicite os nomes e as idades de 10 pessoas. Armazene os nomes em uma lista e as
#idades em outra lista.
#Na sequência, exiba os nomes de todas as pessoas que possuem idade maior ou igual
#a 18 anos

lista_nomes = []
lista_idade = []

for i in range(10):
    nome = input("Digite o nome: ")
    lista_nomes.append(nome)
    idade = int(input("Digite a idade: "))
    lista_idade.append(idade)
print(lista_nomes)
print(lista_idade)
for i in range(len(lista_idade)):
    if lista_idade[i] >= 18:
        print(lista_nomes[i])

#Crie uma função que aceite um parâmetro nomeado itens que seja uma lista de
#strings. A função deve imprimir cada item da lista em linhas separadas

def imprimir_itens(itens: list[str]):
    for item in itens:
        print(item)

imprimir_itens( ["Maçã", "Banana", "Laranja", "Uva"])

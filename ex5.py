#Implemente uma função que conte quantas palavras existem em uma string.

def contar_palavras(frase):
    # Divide a frase em palavras e conta o número de palavras
    palavras = frase.split()
    print (len(palavras))
contar_palavras("amarelo verde")



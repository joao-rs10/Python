def extrair_palavras(frase):
    # Divide a frase em palavras e retorna a lista
    return frase.split()

# Solicita ao usuário que insira uma frase
entrada = input("Digite uma frase: ")
resultado = extrair_palavras(entrada)

# Exibe a lista de palavras
print(resultado)

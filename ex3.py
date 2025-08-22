def contar_vogais(texto):
    vogais = "aeiouAEIOU"  # Inclui vogais minúsculas e maiúsculas
    contador = 0

    for caractere in texto:
        if caractere in vogais:
            contador += 1

    print(contador)
contar_vogais("a,e,i,o")
#Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#a) o maior número da lista
#b) o menor número da lista
#c) a média dos números contidos na lista

def preencher_lista_e_analisar():
    lista_numeros = []

    print("=== PREENCHIMENTO DA LISTA ===")

    # Preenche a lista com 10 números inteiros
    for i in range(10):
        while True:
            try:
                numero = int(input(f"Digite o {i + 1}º número inteiro: "))
                lista_numeros.append(numero)
                break
            except ValueError:
                print("❌ Por favor, digite um número inteiro válido.")

    # Exibe a lista completa
    print(f"\n📋 Lista preenchida: {lista_numeros}")

    # Calcula o maior número
    maior_numero = max(lista_numeros)

    # Calcula o menor número
    menor_numero = min(lista_numeros)

    # Calcula a média
    media = sum(lista_numeros) / len(lista_numeros)

    # Exibe os resultados
    print("\n=== RESULTADOS DA ANÁLISE ===")
    print(f"🔺 Maior número da lista: {maior_numero}")
    print(f"🔻 Menor número da lista: {menor_numero}")
    print(f"📊 Média dos números: {media:.2f}")

    return lista_numeros, maior_numero, menor_numero, media


# Executa o programa
if __name__ == "__main__":
    preencher_lista_e_analisar()




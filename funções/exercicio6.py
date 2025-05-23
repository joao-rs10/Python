'''
Faça um programa para uma calculadora simples com as seguintes operações: adição, subtração,
multiplicação e divisão.
O programa começa apresentando ao usuário um menu de opções semelhante ao mostrado abaixo:
Calculadora:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair do programa
Selecione sua opção:
Crie uma função chamada Menu, que exiba o menu acima e retorna a opção do usuário para o
programa principal. Se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
opção válida.
De acordo com a opção do usuário, chame uma das seguintes funções: adicao, subtracao,
multiplicacao, divisao, passando como parâmetros dois números também informados pelo usuário.
Após a execução da operação o programa volta a apresentar o menu inicial até que o usuário encerre
o programa com a opção 5.
'''
def menu():
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Sair")
    while True:
        opcao = int(input("Selecione sua opção: "))
        if opcao in [1, 2, 3, 4, 5]:
            return opcao
        else:
            print("Opção inválida. Por favor, insira uma opção válida (1 a 5).")

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        print("Erro! Divisão por zero.")
        return None
    else:
        return a / b


def calcular():
    while True:
        # Chama a função menu para obter a opção do usuário
        opcao = menu()

        if opcao == 5:
            print("Saindo do programa...")
            break

        # Solicita os dois números do usuário
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        # Realiza a operação correspondente à opção selecionada
        if opcao == 1:
            print(f"O resultado da adição é: {adicao(num1, num2)}")
        elif opcao == 2:
            print(f"O resultado da subtração é: {subtracao(num1, num2)}")
        elif opcao == 3:
            print(f"O resultado da multiplicação é: {multiplicacao(num1, num2)}")
        elif opcao == 4:
            resultado = divisao(num1, num2)
            if resultado is not None:
                print(f"O resultado da divisão é: {resultado}")

        # O programa volta para o menu após cada operação
        input("\nPressione Enter para continuar...")


# Executa o programa
calcular()

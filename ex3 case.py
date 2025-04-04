num = int(input('Digite um número inteiro: '))

resto = num % 3

match resto:
    case 0:
        print(f'O número {num} é multiplo de 3')
    case _:
        print(f' O número {num} não é multiplo de 3')


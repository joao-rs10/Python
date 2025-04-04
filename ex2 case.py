num = float(input("Digite um número: "))

print('1 - Dobro')
print('2 - Metade')
print('3 - 10% do número')

opcoes= int(input('Selecione uma das opções acima: '))

match opcoes:
    case 1:
        resultado = 2 * num
        print(f'O dobro do valor é: {resultado}')
    case 2:
        resultado = num // 2
        print(f"A metade do valor é {resultado}")
    case 3:
        resultado = num * 0.10
        print(f'10% do valor é: {resultado + num} ')
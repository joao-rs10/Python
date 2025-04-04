valor= float(input("Digite o valor do produto: "))

print('C - Cliente comum')
print('F - Funcionário')
print('V - Cliente Vip')
tipo= input('Informe o tipo de cliente: ')

match tipo:
    case 'c' | 'C':
        print(f'Valor sem desconto: {valor}')
    case 'f' | 'F':
        valor = valor - (valor * 10 // 100)
        print(f'Valor com 10% de desconto: {valor}')
    case 'v' | 'V':
        valor = valor - (valor * 5 // 100)
        print(f'Valor com 5% de desconto: {valor}')
    case _:
         print('Tipo de cliente inválido.')


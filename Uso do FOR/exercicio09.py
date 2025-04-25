#9. Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N.

num = int(input("Digite um número: "))
fatorial = 1

for i in range(1, num+1):
        fatorial = fatorial * i
print(f"O fatorial do número {num} é : {fatorial}")
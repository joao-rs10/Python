def notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media < 6:
        print("Reprovado")
    else:
        print("Aprovado")

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
notas(nota1,nota2)
#0. Solicite a quantidade de alunos de uma turma e a quantidade de notas. Para cada aluno, solicite as
#suas notas e exiba a sua respectiva média.
alunos = int(input("Coloque a quantidade de alunos: "))
notas= int(input("Quantas notas são? "))
for i in range(alunos):
    soma = 0
    for n in range(notas):
        nota = int(input("Coloque a nota do aluno: "))
        soma += nota

    media = soma / notas
    print(f"A média das notas é : {media}")

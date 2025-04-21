import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista_alunos)  # embaralha a ordem

print("A ordem de apresentação será:")
for i, nome in enumerate(lista_alunos, start=1):
    print(f"{i}º - {nome}")

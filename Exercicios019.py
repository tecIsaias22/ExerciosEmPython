import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista_alunos)

print(f"O aluno escolhido para apagar o quadro foi: {escolhido}")

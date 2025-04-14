# Faça um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
sala = float(input("Qual é o seu salário atual? "))

if sala > 1250.00:
    aumento = sala * 0.10
    novoSalario = sala + aumento
    print("Seu salário com aumento é: " + str(novoSalario))
else:
    aumento = sala * 0.15
    novoSalario = sala + aumento
    print("Seu salário com aumento é: " + str(novoSalario))

salario = float(input("Digite o salário do funcionário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("O novo salário do funcionário é: R${:.2f}".format(novo_salario))
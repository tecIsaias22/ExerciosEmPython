dias = int(input('quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))

total = (60 * dias) + (0.15 * km)
print('O total a pagar e de R${:.2f}'.format(total))


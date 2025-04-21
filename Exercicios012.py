loja = float(input('Digite o valor da compra: '))

desconto = loja * 0.05
valor_final = loja - desconto

print('O valor da compra é R${:.2f}, o desconto de 5% é R${:.2f} e o valor final é R${:.2f}'.format(loja, desconto, valor_final))

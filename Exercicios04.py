valor = input("Digite algo: ")

print("O tipo primitivo é: ", type(valor))
print("Só tem espaços? ", valor.isspace())
print("É um número? ", valor.isnumeric())
print("É alfabético? ", valor.isalpha())
print("É alfanumérico? ", valor.isalnum())
print("Está em maiúsculas? ", valor.isupper())
print("Está em minúsculas? ", valor.islower())
print("Está capitalizada? ", valor.istitle())
print("É um identificador? ", valor.isidentifier())
print("É um dígito? ", valor.isdigit())

import math

angulo = float(input("Digite o ângulo (em graus): "))

# Converter para radianos, pois as funções trigonométricas do Python usam radianos
radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"O ângulo de {angulo}° tem:")
print(f" - Seno     = {seno:.2f}")
print(f" - Cosseno  = {cosseno:.2f}")
print(f" - Tangente = {tangente:.2f}")

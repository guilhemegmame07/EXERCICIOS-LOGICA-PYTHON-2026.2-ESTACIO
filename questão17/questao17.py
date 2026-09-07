import math

print("=== CÁLCULOS MATEMÁTICOS ===")

numero = float(input("Digite um número real: "))

print()
print("=== RESULTADOS ===")

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"Raiz quadrada: {raiz:.2f}")
else:
    print("Raiz quadrada: não existe raiz real para número negativo.")

print("Valor absoluto:", math.fabs(numero))
print("Arredondamento para cima:", math.ceil(numero))
print("Arredondamento para baixo:", math.floor(numero))

if numero >= 0 and numero == int(numero):
    fatorial = math.factorial(int(numero))
    print("Fatorial:", fatorial)
else:
    print("Fatorial: disponível somente para números inteiros não negativos.")
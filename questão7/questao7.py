print("=== ANÁLISE DO NÚMERO ===")

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "nulo"

if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

print()
print(f"O número {numero} é {sinal} e {paridade}.")
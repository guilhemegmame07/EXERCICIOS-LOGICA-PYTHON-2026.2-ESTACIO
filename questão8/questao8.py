print("=== ESTATÍSTICA DE 10 NÚMEROS ===")

soma = 0
positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))

    soma = soma + numero

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

media = soma / 10

print()
print("=== RELATÓRIO ESTATÍSTICO ===")
print("Soma:", soma)
print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Números pares:", pares)
print("Números ímpares:", impares)
print(f"Média: {media:.2f}")
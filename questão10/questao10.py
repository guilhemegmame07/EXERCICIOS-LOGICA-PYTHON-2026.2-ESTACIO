print("=== ANÁLISE DE TEMPERATURAS ===")

temperaturas = []

for i in range(7):
    temperatura = float(input("Digite a temperatura do dia: "))
    temperaturas.append(temperatura)

maior = temperaturas[0]
menor = temperaturas[0]

for temperatura in temperaturas:
    if temperatura > maior:
        maior = temperatura

    if temperatura < menor:
        menor = temperatura

soma = 0

for temperatura in temperaturas:
    soma = soma + temperatura

media = soma / 7

acima_da_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_da_media = acima_da_media + 1

print()
print("=== RELATÓRIO ===")

print("Temperaturas registradas:", temperaturas)
print(f"Maior temperatura: {maior:.2f} °C")
print(f"Menor temperatura: {menor:.2f} °C")
print(f"Temperatura média: {media:.2f} °C")
print("Dias acima da média:", acima_da_media)
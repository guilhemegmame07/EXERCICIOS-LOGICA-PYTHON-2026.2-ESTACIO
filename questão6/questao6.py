print("=== ORDENAÇÃO DE TRÊS NÚMEROS ===")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2:
    if numero1 > numero3:
        maior = numero1

        if numero2 > numero3:
            meio = numero2
            menor = numero3
        else:
            meio = numero3
            menor = numero2

    else:
        maior = numero3
        meio = numero1
        menor = numero2

else:
    if numero2 > numero3:
        maior = numero2

        if numero1 > numero3:
            meio = numero1
            menor = numero3
        else:
            meio = numero3
            menor = numero1

    else:
        maior = numero3
        meio = numero2
        menor = numero1

print()
print("=== RESULTADO ===")
print("Maior número:", maior)
print("Número intermediário:", meio)
print("Menor número:", menor)
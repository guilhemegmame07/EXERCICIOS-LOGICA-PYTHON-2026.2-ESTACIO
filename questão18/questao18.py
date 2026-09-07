import random

print("=== LANÇAMENTO DE DOIS DADOS ===")

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

soma = dado1 + dado2

print("Resultado do primeiro dado:", dado1)
print("Resultado do segundo dado:", dado2)
print("Soma dos dados:", soma)

print()
print("=== 10 LANÇAMENTOS ===")

quantidade_sete = 0

for i in range(10):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    soma = dado1 + dado2

    print("Lançamento", i + 1, "- Soma:", soma)

    if soma == 7:
        quantidade_sete = quantidade_sete + 1

print()
print("Quantidade de vezes que a soma foi 7:", quantidade_sete)
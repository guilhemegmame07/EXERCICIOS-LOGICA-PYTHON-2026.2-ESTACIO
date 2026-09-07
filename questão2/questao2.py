print("=== CALCULADORA ===")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
potenciacao = numero1 ** numero2

print()
print("=== RESULTADOS ===")
print("Adição:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Potenciação:", potenciacao)

if numero2 == 0:
    print("Divisão:", "Divisão por zero não permitida")
    print("Divisão inteira:", "Divisão por zero não permitida")
    print("Resto da divisão:", "Divisão por zero não permitida")
else:
    divisao = numero1 / numero2
    divisao_inteira = numero1 // numero2
    resto = numero1 % numero2

    print("Divisão:", divisao)
    print("Divisão inteira:", divisao_inteira)
    print("Resto da divisão:", resto)
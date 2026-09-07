print("================================")
print(" GERENCIAMENTO DE NÚMEROS")
print("================================")

numeros = []

opcao = -1

while opcao != 0:

    print()
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        numero = int(input("Digite um número: "))
        numeros.append(numero)
        print("Número cadastrado com sucesso.")

    elif opcao == 2:
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            print("Números cadastrados:")

            for numero in numeros:
                print(numero)

    elif opcao == 3:
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            maior = numeros[0]

            for numero in numeros:
                if numero > maior:
                    maior = numero

            print("Maior número:", maior)

    elif opcao == 4:
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            menor = numeros[0]

            for numero in numeros:
                if numero < menor:
                    menor = numero

            print("Menor número:", menor)

    elif opcao == 5:
        if len(numeros) == 0:
            print("Nenhum número cadastrado.")
        else:
            soma = 0

            for numero in numeros:
                soma = soma + numero

            media = soma / len(numeros)

            print(f"Média: {media:.2f}")

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")
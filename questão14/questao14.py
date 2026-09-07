print("=== SISTEMA DE NOTAS DA TURMA ===")


def cadastrar_estudantes():
    estudantes = []

    for i in range(5):
        print()
        print("Estudante", i + 1)

        nome = input("Nome: ")

        nota1 = float(input("Primeira nota: "))
        while nota1 < 0 or nota1 > 10:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
            nota1 = float(input("Primeira nota novamente: "))

        nota2 = float(input("Segunda nota: "))
        while nota2 < 0 or nota2 > 10:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
            nota2 = float(input("Segunda nota novamente: "))

        nota3 = float(input("Terceira nota: "))
        while nota3 < 0 or nota3 > 10:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
            nota3 = float(input("Terceira nota novamente: "))

        media = (nota1 + nota2 + nota3) / 3

        estudante = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "media": media
        }

        estudantes.append(estudante)

    return estudantes


def mostrar_resultado(estudantes):
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    maior_media = estudantes[0]
    menor_media = estudantes[0]

    print()
    print("=== MÉDIA DOS ESTUDANTES ===")

    for estudante in estudantes:
        print(f"{estudante['nome']} - Média: {estudante['media']:.2f}")

        if estudante["media"] >= 7:
            aprovados = aprovados + 1
        elif estudante["media"] >= 5:
            recuperacao = recuperacao + 1
        else:
            reprovados = reprovados + 1

        if estudante["media"] > maior_media["media"]:
            maior_media = estudante

        if estudante["media"] < menor_media["media"]:
            menor_media = estudante

    print()
    print("=== RESUMO DA TURMA ===")
    print("Maior média:", maior_media["nome"], "-", f"{maior_media['media']:.2f}")
    print("Menor média:", menor_media["nome"], "-", f"{menor_media['media']:.2f}")
    print("Quantidade de aprovados:", aprovados)
    print("Quantidade em recuperação:", recuperacao)
    print("Quantidade de reprovados:", reprovados)


estudantes = cadastrar_estudantes()

mostrar_resultado(estudantes)
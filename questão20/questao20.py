print("========================================")
print("        SISTEMA ACADÊMICO")
print("========================================")


estudantes = []


def cadastrar_estudante():
    print()
    print("=== CADASTRAR ESTUDANTE ===")

    nome = input("Nome: ")

    idade = int(input("Idade: "))

    while idade <= 0:
        print("Idade inválida. Digite uma idade positiva.")
        idade = int(input("Idade novamente: "))

    curso = input("Curso: ")

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

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "situacao": situacao
    }

    estudantes.append(estudante)

    print("Estudante cadastrado com sucesso!")


def listar_estudantes():
    print()
    print("=== LISTA DE ESTUDANTES ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
    else:
        for estudante in estudantes:
            print()
            print("Nome:", estudante["nome"])
            print("Idade:", estudante["idade"])
            print("Curso:", estudante["curso"])
            print("Nota 1:", estudante["nota1"])
            print("Nota 2:", estudante["nota2"])
            print("Nota 3:", estudante["nota3"])
            print(f"Média: {estudante['media']:.2f}")
            print("Situação:", estudante["situacao"])


def consultar_estudante():
    print()
    print("=== CONSULTAR ESTUDANTE ===")

    nome = input("Digite o nome do estudante: ")

    encontrado = False

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():
            print()
            print("Nome:", estudante["nome"])
            print("Idade:", estudante["idade"])
            print("Curso:", estudante["curso"])
            print("Nota 1:", estudante["nota1"])
            print("Nota 2:", estudante["nota2"])
            print("Nota 3:", estudante["nota3"])
            print(f"Média: {estudante['media']:.2f}")
            print("Situação:", estudante["situacao"])

            encontrado = True

    if encontrado == False:
        print("Estudante não encontrado.")


def alterar_dados():
    print()
    print("=== ALTERAR DADOS ===")

    nome = input("Digite o nome do estudante: ")

    encontrado = False

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():

            print()
            print("Estudante encontrado.")

            novo_nome = input("Novo nome: ")
            nova_idade = int(input("Nova idade: "))
            
            while nova_idade <= 0:
                print("Idade inválida. Digite uma idade positiva.")
                nova_idade = int(input("Nova idade novamente: "))

            novo_curso = input("Novo curso: ")

            nova_nota1 = float(input("Nova primeira nota: "))

            while nova_nota1 < 0 or nova_nota1 > 10:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
                nova_nota1 = float(input("Nova primeira nota novamente: "))

            nova_nota2 = float(input("Nova segunda nota: "))

            while nova_nota2 < 0 or nova_nota2 > 10:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
                nova_nota2 = float(input("Nova segunda nota novamente: "))

            nova_nota3 = float(input("Nova terceira nota: "))

            while nova_nota3 < 0 or nova_nota3 > 10:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
                nova_nota3 = float(input("Nova terceira nota novamente: "))

            nova_media = (nova_nota1 + nova_nota2 + nova_nota3) / 3

            if nova_media >= 7:
                nova_situacao = "Aprovado"
            elif nova_media >= 5:
                nova_situacao = "Recuperação"
            else:
                nova_situacao = "Reprovado"

            estudante["nome"] = novo_nome
            estudante["idade"] = nova_idade
            estudante["curso"] = novo_curso
            estudante["nota1"] = nova_nota1
            estudante["nota2"] = nova_nota2
            estudante["nota3"] = nova_nota3
            estudante["media"] = nova_media
            estudante["situacao"] = nova_situacao

            print("Dados alterados com sucesso!")

            encontrado = True

    if encontrado == False:
        print("Estudante não encontrado.")


def remover_estudante():
    print()
    print("=== REMOVER ESTUDANTE ===")

    nome = input("Digite o nome do estudante: ")

    encontrado = False

    for estudante in estudantes:
        if estudante["nome"].lower() == nome.lower():

            print("Estudante encontrado:", estudante["nome"])

            confirmacao = input("Deseja realmente remover? (s/n): ")

            if confirmacao.lower() == "s":
                estudantes.remove(estudante)
                print("Estudante removido com sucesso.")
            else:
                print("Remoção cancelada.")

            encontrado = True
            break

    if encontrado == False:
        print("Estudante não encontrado.")


def gerar_relatorio():
    print()
    print("=== RELATÓRIO DA TURMA ===")

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    total = len(estudantes)

    maior_media = estudantes[0]
    menor_media = estudantes[0]

    soma_medias = 0

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for estudante in estudantes:

        soma_medias = soma_medias + estudante["media"]

        if estudante["media"] > maior_media["media"]:
            maior_media = estudante

        if estudante["media"] < menor_media["media"]:
            menor_media = estudante

        if estudante["media"] >= 7:
            aprovados = aprovados + 1
        elif estudante["media"] >= 5:
            recuperacao = recuperacao + 1
        else:
            reprovados = reprovados + 1

    media_geral = soma_medias / total

    print("Total de estudantes:", total)
    print("Maior média:", maior_media["nome"], "-", f"{maior_media['media']:.2f}")
    print("Menor média:", menor_media["nome"], "-", f"{menor_media['media']:.2f}")
    print(f"Média geral: {media_geral:.2f}")
    print("Aprovados:", aprovados)
    print("Recuperação:", recuperacao)
    print("Reprovados:", reprovados)


opcao = -1

while opcao != 0:

    print()
    print("========================================")
    print("        SISTEMA ACADÊMICO")
    print("========================================")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Consultar estudante")
    print("4 - Alterar dados")
    print("5 - Remover estudante")
    print("6 - Gerar relatório da turma")
    print("0 - Encerrar sistema")
    print("========================================")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_estudante()

    elif opcao == 2:
        listar_estudantes()

    elif opcao == 3:
        consultar_estudante()

    elif opcao == 4:
        alterar_dados()

    elif opcao == 5:
        remover_estudante()

    elif opcao == 6:
        gerar_relatorio()

    elif opcao == 0:
        print("Sistema encerrado.")

    else:
        print("Opção inválida.")
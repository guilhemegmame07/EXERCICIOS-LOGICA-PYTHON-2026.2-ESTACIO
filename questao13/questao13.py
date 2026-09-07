print("=== AGENDA DE CONTATOS ===")

contatos = []

for i in range(5):
    print()
    print("Contato", i + 1)

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contatos.append(contato)

print()
print("=== CONSULTA DE CONTATO ===")

nome_consulta = input("Digite o nome da pessoa que deseja consultar: ")

encontrado = False

for contato in contatos:
    if contato["nome"] == nome_consulta:
        print()
        print("=== DADOS DO CONTATO ===")
        print("Nome:", contato["nome"])
        print("Telefone:", contato["telefone"])
        print("E-mail:", contato["email"])

        encontrado = True

if encontrado == False:
    print("Contato não encontrado.")
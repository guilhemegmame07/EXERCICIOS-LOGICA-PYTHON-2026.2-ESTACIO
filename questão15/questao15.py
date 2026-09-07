print("=== CADASTRO DE CIDADES ===")

cidades = []

for i in range(5):
    print()
    print("Cidade", i + 1)

    nome = input("Nome da cidade: ")
    estado = input("Estado (sigla): ")
    populacao = int(input("População: "))

    cidade = {
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    }

    cidades.append(cidade)

maior_populacao = cidades[0]
menor_populacao = cidades[0]

populacao_total = 0

for cidade in cidades:
    populacao_total = populacao_total + cidade["populacao"]

    if cidade["populacao"] > maior_populacao["populacao"]:
        maior_populacao = cidade

    if cidade["populacao"] < menor_populacao["populacao"]:
        menor_populacao = cidade

media_populacao = populacao_total / len(cidades)

print()
print("=== DADOS DAS CIDADES ===")

for cidade in cidades:
    print("Nome:", cidade["nome"])
    print("Estado:", cidade["estado"])
    print("População:", cidade["populacao"])
    print()

print("=== RESUMO ===")
print("Cidade com maior população:", maior_populacao["nome"])
print("População:", maior_populacao["populacao"])

print("Cidade com menor população:", menor_populacao["nome"])
print("População:", menor_populacao["populacao"])

print("População total:", populacao_total)
print(f"Média populacional: {media_populacao:.2f}")
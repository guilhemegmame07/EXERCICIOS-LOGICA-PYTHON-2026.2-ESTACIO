print("=== CADASTRO DE PRODUTOS ===")

produtos = []

for i in range(5):
    print()
    print("Produto", i + 1)

    nome = input("Nome do produto: ")
    preco = float(input("Preço unitário: "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

print()
print("=== PRODUTOS CADASTRADOS ===")

for produto in produtos:
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print()

total_estoque = 0

for produto in produtos:
    valor = produto["preco"] * produto["quantidade"]
    total_estoque = total_estoque + valor

maior_preco = produtos[0]

for produto in produtos:
    if produto["preco"] > maior_preco["preco"]:
        maior_preco = produto

print("=== RESUMO DO ESTOQUE ===")
print(f"Valor total do estoque: R$ {total_estoque:.2f}")
print("Produto com maior preço:", maior_preco["nome"])
print(f"Maior preço unitário: R$ {maior_preco['preco']:.2f}")
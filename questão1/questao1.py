print("=== CADASTRO DE PERFIL PESSOAL ===")

nome = input("Digite seu nome completo: ")

idade = int(input("Digite sua idade: "))

while idade < 0:
    print("A idade não pode ser negativa.")
    idade = int(input("Digite sua idade novamente: "))

altura = float(input("Digite sua altura em metros: "))

while altura <= 0:
    print("A altura deve ser maior que zero.")
    altura = float(input("Digite sua altura novamente: "))

cidade = input("Digite a cidade onde você mora: ")

print()
print("================================")
print("     CARTÃO DE IDENTIFICAÇÃO")
print("================================")
print("Nome completo:", nome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Cidade:", cidade)
print("================================")
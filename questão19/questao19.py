print("=== ANÁLISE DE FRASE ===")

frase = input("Digite uma frase: ")

frase_sem_espacos = frase.strip()
palavras = frase_sem_espacos.split()

letra = input("Digite uma letra para pesquisar: ")

quantidade_caracteres = len(frase)
quantidade_palavras = len(palavras)

primeira_palavra = palavras[0]
ultima_palavra = palavras[-1]

quantidade_letra = frase_sem_espacos.lower().count(letra.lower())

print()
print("=== RESULTADO ===")
print("Quantidade de caracteres:", quantidade_caracteres)
print("Quantidade de palavras:", quantidade_palavras)
print("Primeira palavra:", primeira_palavra)
print("Última palavra:", ultima_palavra)
print("Quantidade de ocorrências da letra:", quantidade_letra)
print("Frase em maiúsculas:", frase_sem_espacos.upper())
print("Frase em minúsculas:", frase_sem_espacos.lower())
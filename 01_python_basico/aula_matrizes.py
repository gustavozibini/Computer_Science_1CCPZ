"""Aula - Matrizes: uma lista que guarda outras listas (linhas e colunas)."""

# Cada item é uma lista pequena: [música, artista]
musicas = [
    ["3 l b", "bob"],
    [" n m t", "ozzy"],
    [" hino c", "corintia"],

]

# O for de fora percorre cada linha; o de dentro percorre cada informação da linha
for musica in musicas:
    for info in musica:
        print(info)
    print()  # linha em branco para separar as músicas

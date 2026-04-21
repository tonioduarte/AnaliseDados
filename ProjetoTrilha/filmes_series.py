import json

# Artifícios para as questôes:
dados = json.load(open("mini_projeto_1/movies_and_series.json", encoding="utf-8"))
filmes = dados["data"]["movies"]
series = dados["data"]["series"]
filme_serie = filmes + series
maior = filme_serie[0]
total = 0
generos = []

# Questão 1 e 5:
for i in filme_serie:
    print()
    print(i["title"], "é um filme/serie contido no json")
    total += 1

print()
print(f"O total de filmes e series contidos no json é {total}")

# Questão 3:
for i in filme_serie:
    if i["rating"] > maior["rating"]:
        maior = i

print()
print(maior["title"], "possui a maior nota entre os filmes e series sendo ela:", maior["rating"])

# Questão 4:
print()
for i in filme_serie:
    for genero in i["genres"]:
        if genero not in generos:
            generos.append(genero)

print("Os filmes/ series possuem os seguintes gêneros:")
for genero in generos:
    print(genero)

# Questão 5:

print()
quantidade = 0

for i in filme_serie:
    if "title" in i:
        quantidade += 1

print(f"O total de filmes e series contidos no json é {quantidade}")

# Questão 6:

print()
plataformas = []

for i in filme_serie:
    for nome in i["streaming"].keys():
        if nome not in plataformas:
            plataformas.append(nome)

print("Plataformas:")
for p in plataformas:
    print(p)

# Questão 7:

print("\nDisponíveis em 4K na Netflix:")

for i in filme_serie:
    if "Netflix" in i["streaming"]:
        netflix = i["streaming"]["Netflix"]

        if netflix["available"] and "resolution" in netflix:
            if "4K" in netflix["resolution"]:
                print(i["title"])

# Questão 8:

for i in filmes:
    if i["title"] == "The Shawshank Redemption":
        print()
        print("Disponível em:")

        #for chave, valor in dicionario.items():
        for nome, dados_stream in i["streaming"].items(): #nome recebe a chave, dados recebe o valor da chave
            if dados_stream["available"]:
                print(nome, dados_stream["url"])

# Questão 9:

print()
for i in filme_serie:
    for ator in i["cast"]:
        print(ator["actor"], "-", ator["character"])

# Questão 10:

print()
maior_salario = 0
ator_maior = ""

for i in filme_serie:
    for ator in i["cast"]:
        if ator["salary"] > maior_salario:
            maior_salario = ator["salary"]
            ator_maior = ator["actor"]

print("\nMaior salário:", ator_maior, maior_salario)

# Questão 11:

print()
for i in filmes:
    for local in i["production"]["filmingLocations"]:
        print(local)
        
# Questao 12:

print()
for i in filmes:
    print(i["directors"], "dirigiu o filme", i["title"])

# Questão 13:

print()
maior_bi = filmes[0]

for i in filmes:
    if i["production"]["boxOffice"]["revenue"] > maior_bi["production"]["boxOffice"]["revenue"]:
        maior_bi = i

print("\nMaior bilheteria:", maior_bi["title"])

# Questão 14:

total = 0

print()
for i in filmes:
    total += i["production"]["boxOffice"]["profit"]

media = total / len(filmes)
print("Lucro médio:", media)

# Questão 15:

print()
for i in filmes:
    vendas = i["production"]["boxOffice"]["ticketSales"] #i [varias vezes] p pegar um valor só, crio um for em caso de precisar pegar varios valores em um dic.
    print(i["title"], "-", vendas["domestic"], vendas["international"])

# Questão 16:

print()
for i in filme_serie:
    for premio in i["awards"]:
        print(premio["year"], premio["award"], premio["category"])

# Questão 17:

print()
for i in filme_serie:
    for premio in i["awards"]:
        if premio["won"]:
            print(i["title"])

# Questão 18:

print()
for f in filmes:
    for premio in f["awards"]:
        if premio["category"] == "Best Picture":
            print(premio["year"], "-", premio["nominees"])

# Questão 19:


melhor_comentario = None

print()
for i in filme_serie:
    for r in i["reviews"]:
        if melhor_comentario is None or r["details"]["helpfulVotes"] > melhor_comentario["details"]["helpfulVotes"]:
            melhor_comentario = r

print(melhor_comentario["comment"])

# Questão 20:

total = 0

print()
for f in filmes:
    total += f["rating"]

print("Média:", total / len(filmes))

# Questão 21:

print()
for i in filme_serie:
    for r in i["reviews"]:
        if r["details"]["date"] < "2022":
            print(r["comment"])
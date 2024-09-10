linguagens_programacao = ["Java", "C", "C#", "Python", "JavaScript", "Ruby"]

linguagens_programacao.sort()
print(linguagens_programacao)

linguagens_programacao.sort(reverse=True)
print(linguagens_programacao)

linguagens_programacao.sort(key= lambda x: len(x))
print(linguagens_programacao)


linguagens_programacao.sort(key = lambda x: len(x), reverse=True)
print(linguagens_programacao)
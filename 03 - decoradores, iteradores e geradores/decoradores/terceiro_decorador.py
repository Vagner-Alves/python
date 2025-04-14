def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("python")
print(tecnologia)
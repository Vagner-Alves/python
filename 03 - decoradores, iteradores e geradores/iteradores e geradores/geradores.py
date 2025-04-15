def fibonacci(limite):
    a, b = 0, 1
    while a < limite:
        yield a 
        a, b = b, a+ b

for numero in fibonacci(10):
    print(numero)
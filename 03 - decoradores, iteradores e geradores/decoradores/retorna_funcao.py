def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mult(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div

somar = calculadora("+")
subtracao = calculadora("-")
multiplicacao = calculadora("*")
divisao = calculadora("/")

print(subtracao(2,3))
print(somar(2,2))
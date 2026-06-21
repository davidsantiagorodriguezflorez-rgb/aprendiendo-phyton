def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    else:
        return a / b

operaciones = [
    ("suma", 8, 5),
    ("resta", 9, 3),
    ("multiplicacion", 8, 6),
    ("division", 8, 0),
    ("suma", 160, 19),
    ("multiplicacion", 1608, 20183),
]

for nombre, num1, num2 in operaciones:
    if nombre == "suma":
        resultado = sumar(num1, num2)
    elif nombre == "resta":
        resultado = restar(num1, num2)
    elif nombre == "multiplicacion":
        resultado = multiplicar(num1, num2)
    elif nombre == "division":
        resultado = dividir(num1, num2)
    print(nombre, "de", num1, "y", num2, "=", resultado)

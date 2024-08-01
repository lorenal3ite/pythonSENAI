def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
lado1 = 5
lado2 = 5
lado3 = 5

print(tipo_triangulo(lado1, lado2, lado3))

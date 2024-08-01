def operacoes_basicas(num1, num2):
    # Adição
    soma = num1 + num2

    # Subtração
    subtracao = num1 - num2

    # Multiplicação
    multiplicacao = num1 * num2

    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Não é possível dividir por zero."

    print(f"Adição: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")


num1 = 10
num2 = 5
operacoes_basicas(num1, num2)
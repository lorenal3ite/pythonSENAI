def mostrar_menu():
    print("Selecione a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

def realizar_operacao(operacao, num1, num2):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Não é possível dividir por zero."
    else:
        return "Opção inválida."


while True:
    mostrar_menu()
    opcao = int(input("Digite o número da operação desejada: "))
    if opcao == 0:
        print("Saindo...")
        break
    elif opcao >= 1 and opcao <= 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = realizar_operacao(opcao, num1, num2)
        print("Resultado:", resultado)
    else:
        print("Opção inválida. Tente novamente.")
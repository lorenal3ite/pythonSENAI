print("Escreva se você deseja descobrir a tensão elétrica, a corrente elétrica, a resistência elétrica ou a resistência do resistor")

print("0 = sair")
print("1 = tensão elétrica")
print("2 = resistênca elétrica")
print("3 = corrente elétrica")
print("4 = resistência resistor")


formula = input("digite qual fórmula você deseja descobir:")

while formula != "0":
    if formula == "1":
        print("tensão elétrica")
        while True:
            try:
                resistencia = float(input("qual a resistência elétrica em volts? "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

        while True:
            corrente = float(input("qual a corrente elétrica? "))
            if corrente > 0:
                break
        tensao = resistencia * corrente
        print(" a tensão elétrica é", tensao, "V")

    elif formula == "2":
        print("resistência elétrica")
        while True:
            try:
                tensao = float(input("qual a tensão elétrica em ohms? "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

        while True:
            corrente = float(input("qual a corrente elétrica? "))
            if corrente > 0:
                break
        resistencia = tensao / corrente
        print("a resistência elétrica é", resistencia, "Ω")

    elif formula == "3":
        print("corrente elétrica")
        while True:
            try:
                tensao = float(input("qual a tensão elétrica em amperes? "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

        while True:
            resistencia = float(input("qual a resistência elétrica? "))
            if resistencia > 0:
                break
        corrente = tensao / resistencia
        print("a corrente elétrica é", corrente, "A")

    elif formula == "4":
        print("resistência do resistor")
        while True:
            try:
                tensaofonte = float(input("digite a tensão da fonte em ohms:"))
                if tensaofonte > 0:
                    break
            except ValueError:
                print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

        while True:
            try:
                tensaoled = float(input("digite a tensão do LED:"))
                if tensaoled > 0:
                    break
            except ValueError:
                print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

        while True:
            correnteled = float(input("digite a corrente do LED:"))
            if correnteled > 0:
                break
        resistenciaresistor = ( tensaofonte - tensaoled) / correnteled
        print(" a resistência do resistor é", resistenciaresistor)

    else:
        print("Essa opção é inválida.")

    print("0 = sair")
    print("1 = tensão elétrica")
    print("2 = resistênca elétrica")
    print("3 = corrente elétrica")
    print("4 = resistência resistor")

    formula = input("digite qual fórmula você deseja descobir:")
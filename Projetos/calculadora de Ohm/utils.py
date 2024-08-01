print("Bem vindo a Calculadora de Ohm, escreva se voce deseja descobrir a tensão elétrica ou a resistencia do resistor")
def calcular_tensao():
    print("tensão elétrica")
    while True:
        try:
            resistencia = float(input("qual a resistencia elétrica em ohms? "))
            if resistencia > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    while True:
        try:
            corrente = float(input("qual a corrente elétrica em amperes? "))
            if corrente > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    tensao = resistencia * corrente
    print("A tensão elétrica é", tensao, "V")

def calcular_resistencia():
    print("resistência elétrica")
    while True:
        try:
            tensao = float(input("qual a tensão elétrica em volts? "))
            if tensao > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    while True:
        try:
            corrente = float(input("qual a corrente elétrica em amperes? "))
            if corrente > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    resistencia = tensao / corrente
    print("A resistência elétrica é", resistencia, "Ω")

def calcular_corrente():
    print("corrente elétrica")
    while True:
        try:
            tensao = float(input("qual a tensão elétrica em volts? "))
            if tensao > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    while True:
        try:
            resistencia = float(input("qual a resistência elétrica em ohms? "))
            if resistencia > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    corrente = tensao / resistencia
    print("A corrente elétrica é", corrente, "A")

def calcular_resistencia_resistor():
    print("resistência do resistor")
    while True:
        try:
            tensaofonte = float(input("digite a tensão da fonte em volts:"))
            if tensaofonte > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    while True:
        try:
            tensaoled = float(input("digite a tensão do LED em volts:"))
            if tensaoled > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    while True:
        try:
            correnteled = float(input("digite a corrente do LED em amperes:"))
            if correnteled > 0:
                break
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")

    resistenciaresistor = (tensaofonte - tensaoled) / correnteled
    print("A resistência do resistor é", resistenciaresistor, "Ω")

def main():
    while True:
        print("0 = sair")
        print("1 = tensão elétrica")
        print("2 = resistência elétrica")
        print("3 = corrente elétrica")
        print("4 = resistência resistor")

        formula = input("Digite qual fórmula você deseja descobrir: ")

        if formula == "0":
            break
        elif formula == "1":
            calcular_tensao()
        elif formula == "2":
            calcular_resistencia()
        elif formula == "3":
            calcular_corrente()
        elif formula == "4":
            calcular_resistencia_resistor()
        else:
            print("Essa opção é inválida.")

if __name__ == "__main__":
    main()

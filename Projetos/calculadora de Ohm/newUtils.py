def receber_resistencia():
    while True:
        try:
            resistencia = float(input("qual a resistência elétrica em ohms? "))
            if resistencia > 0:
                return resistencia
            else:
                print(("Precis ser maior que 0."))
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")
def receber_corrente():
    while True:
        try:
            corrente = float(input("qual a corrente elétrica em amperes? "))
            if corrente > 0:
                return corrente
            else:
                print("Precis ser maior que 0.")
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")
def receber_tensao():
    while True:
        try:
            tensao = float(input("qual a tensão elétrica em volts? "))
            if tensao > 0:
                return tensao
            else:
                print("Precis ser maior que 0.")
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")
def receber_tensao_font():
    while True:
        try:
            tensaofonte = float(input("digite a tensão da fonte em volts:"))
            if tensaofonte > 0:
                return tensaofonte
            else:
                print("Precis ser maior que 0.")
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")
def receber_tensao_led():
    while True:
        try:
            tensaofonte = float(input("digite a tensão da fonte em volts:"))
            if tensaofonte > 0:
                return tensaofonte
            else:
                print("Precis ser maior que 0.")
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")
def receber_corrente_led():
    while True:
        try:
            correnteled = float(input("digite a corrente do LED em amperes:"))
            if correnteled > 0:
                return correnteled
            else:
                print("Precis ser maior que 0.")
        except ValueError:
            print("Valor inválido, digite um número utilizando o ponto como separador. EX: 1.0")
def calcular_tensao():
    print("tensão elétrica")
    resistencia = receber_resistencia()
    corrente = receber_corrente()
    tensao = resistencia * corrente
    return tensao

def calcular_resistencia():
    print("resistência elétrica")
    tensao = receber_tensao()
    corrente = receber_corrente()
    resistencia = tensao / corrente
    return resistencia

def calcular_corrente():
    print("corrente elétrica")
    tensao = receber_tensao()
    resistencia = receber_resistencia()
    corrente = tensao / resistencia
    return corrente

def calcular_resistencia_resistor():
    print("resistência do resistor")
    tensaofonte = receber_tensao_font()
    tensaoled = receber_tensao_led()
    correnteled = receber_corrente()
    resistenciaresistor = (tensaofonte - tensaoled) / correnteled
    return resistenciaresistor

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
            tensao = calcular_tensao()
            print("A tensão elétrica é", tensao, "V")
        elif formula == "2":
            resistencia = calcular_resistencia()
            print("A resistência elétrica é", resistencia, "Ω")
        elif formula == "3":
            corrente = calcular_corrente()
            print("A corrente elétrica é", corrente, "A")
        elif formula == "4":
            resistencia_resistor = calcular_resistencia_resistor()
            print("A resistência do resistor é", resistencia_resistor, "Ω")
        else:
            print("Essa opção é inválida")

if __name__ == "__main__":
    main()




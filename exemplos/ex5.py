def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade Grau I"
    elif imc < 40:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"

peso = 70 # em kg
altura = 1.75 # em metros
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
print("IMC:", imc)
print("Classificação:", classificacao)
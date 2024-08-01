ano_nasc = int(input("Informe o ano de nascimento da pessoa: "))
idade = 2024 - ano_nasc

if idade <= 18:
    print("É maior de idade")

elif idade > 18:
    print("essa pessoa não existe")

else:
    print("É menor de idade")
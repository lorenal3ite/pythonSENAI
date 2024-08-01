import datetime
def saudacao(nome):
    hora_atual = datetime.datetime.now().hour
    if hora_atual < 12:
        return f"Bom dia,{nome}!"
    elif 12 <= hora_atual < 18:
        return f"Boa tarde,{nome}!"
    else:
        return f"Boa noite,{nome}!"
nome = input("Digite seu nome: ")
print(saudacao(nome))

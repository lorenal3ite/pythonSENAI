import random
print("Seja Bem-Vindo ao EvenorUp. O jogo de chutes para escolher par ou impar muito divertido!")
print(" Para jogar, escolha par ou impar e depois um numero para mostrar o resultado")

print("Bem vindo ao jogo de Par ou Ímpar!")

if input("Digite 'ok' para começar o jogo: ") == "ok":
    print("O jogo está começando..")
else:
    print("Comando inválido. Tente novamente.")
while True:
    try:

        escolha_usuario = input("Escolha par ou ímpar: ")
        numero_usuario =  int(input("Escolha um numero"))

        numero_computador = random.randint(1, 10)
        print("numero_computador", numero_computador)

        soma = numero_usuario + numero_computador
        print("soma", soma)

        resultado = 'par' if soma % 2 == 0 else 'impar'
        print("a soma é", soma, "é o resultado", resultado)

        if (escolha_usuario == "par" and resultado) or (escolha_usuario == "impar" and resultado):
            print("Você perdeu.")
        else:
                print("Você ganhou!")
                jogar_novamente = input("Deseja continuar?? (s/n): ")

        if jogar_novamente != 's':
           print("Obrigado por jogar!")
           break

    except ValueError:
        print("O nosso sistema aceita apenas numeros. Exemplo: 20, 21,22")



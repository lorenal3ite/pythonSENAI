import random
print("Seja bem vindo ao LevelGuessPheNumber! Faça seu chute para jogar! 😜")
print(" Voce ira escolher um numero vamos mostrar se o numero esta maior ou menor que o numero misterioso escolhido!")

if input("Digite 'ok' para começar o jogo 😘: ") == "ok":
    print("O jogo está começando 😎...")
print("Para iniciar o jogo escolha um número de 0 a 100:")
numero_aleatorio = random.randint(0, 100)
tentativas = 0

while True:
    try:
        chute = int(input("Digite o numero do chute desejado: "))
        tentativas = tentativas + 1

        if chute < numero_aleatorio:
            print("o número é maior.")
        elif chute > numero_aleatorio:
            print("o número é menor")
        else:
            print("Parabéns! Você acertou o número 🎉.")

            jogador_novamente = input("Quer jogar novamente? (s/n): ")
            if jogador_novamente != "s":
                print("obrigada por jogar")
                break
    except ValueError:
        print("Digite apenas numeros Ex: 01 02 03 04 05 06")


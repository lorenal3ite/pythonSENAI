#o while repete tudo que esta dentro dele
while True:
    #o try vai tentar executar esse bloco de código
    try:
        numeros = int(input('Digite seu numero: '))

        #o if verifica se a idade é valida
    if nota > 0 and nota <= 100:
            print("idade:", nota)
            # o break sai do while
            break
        else:
            print("idade invalida")


    #caso der errado execute aqui
    except ValueError:
        print("Digite a sua idade em numero. Ex: 26")
print("Digite dois numeros para obter a média de um aluno")
print("")
numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))
soma = numero_1 + numero_2
media = soma / 2

print(f"A media dos valors é igual a {media}")

if media > 70:
    print("O aluno esta aprovado")

elif media == 70:
    print("O aluno esta aprovado por pouco")

else:
    print("O aluno esta reprovado")
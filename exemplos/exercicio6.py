num_1 = float(input("Primeiro numero:"))
num_2 = float(input("Segundo numero:"))
num_3 = float(input("Terceiro numero:"))

if num_1 >= num_2 and num_1 >= num_3:
    print("O primeiro numero é maior")
elif num_2 >= num_3:
    print("O segundo numero é o maior")
else:
    print("O terceiro numero é o maior")
def converter_temperatura(temperatura_celsius):
    # Convertendo para Fahrenheit
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

    # Convertendo para Kelvin
    temperatura_kelvin = temperatura_celsius + 273.15

    return temperatura_fahrenheit, temperatura_kelvin


# Exemplo
celsius = 25
fahrenheit, kelvin = converter_temperatura(celsius)
print(f"{celsius} graus Celsius são {fahrenheit:.2f} graus Fahrenheit e {kelvin:.2f} Kelvin.")

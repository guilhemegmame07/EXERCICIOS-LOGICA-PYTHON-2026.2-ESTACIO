print("=== CONVERSÃO DE TEMPERATURA ===")

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print()
print("=== RESULTADOS ===")
print(f"Celsius: {celsius:.2f} °C")
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin: {kelvin:.2f} K")
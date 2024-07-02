numeros_base = [2, 3, 4, 5, 6, 7, 8, 9]
expoentes = [2, 2, 2, 2, 2, 2, 2, 2]

for base, expoente in zip (numeros_base, expoentes):
    resultado = pow(base, expoente)
    print(f"{base} elevado a {expoente} é igual a {resultado}")
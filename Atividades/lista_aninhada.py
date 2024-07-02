lista_aninhada = [[1, 5, 3], [12, 18], [21, 36, 48]]
soma_total = sum(sum(sublista) for sublista in lista_aninhada)
print(f"A soma dos elementos é: {soma_total}")
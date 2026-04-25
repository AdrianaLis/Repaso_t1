a = [7, 3, 5, 6, 11, 2, 12]

for pasada in range(len(a) - 1):  
    # Bucle interno: compara parejas
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            # Intercambio
            a[i], a[i + 1] = a[i + 1], a[i]

print("¡Ordenado correctamente con {a[i]} pasadas!")
print(a)

print("¡Ordenado correctamente!")
print(a)

try:
    numero = int(input("Introduce un número entero positivo mayor a 10: "))
    if numero <= 10:
        raise ValueError("El número debe ser mayor a 10.")
    impares = [str(i) for i in range(2, numero + 1) if i % 2 != 0]
    print("Números impares:", ", ".join(impares))
except ValueError as e:
    print("Error:", e)

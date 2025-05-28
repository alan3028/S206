try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero < 0:
        raise ValueError("El número debe ser positivo.")
    cuenta_atras = [str(i) for i in range(numero, -1, -1)]
    print("Cuenta atrás:", ", ".join(cuenta_atras))
except ValueError as e:
    print("Error:", e)

try:
    año = int(input("Ingrese un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"{año} es un año bisiesto.")
    else:
        print(f"{año} no es un año bisiesto.")
except ValueError:
    print("Error: Ingrese un año válido (número entero).")
except Exception as e:
    print(f"Error inesperado: {e}")
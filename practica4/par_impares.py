try:
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
except ValueError:
    print("Error: Debe ingresar un número entero válido.")
except Exception as e:
    print(f"Error inesperado: {e}")
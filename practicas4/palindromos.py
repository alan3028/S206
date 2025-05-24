try:
    cadena = input("Ingrese una cadena de caracteres: ").lower().replace(" ", "")
    if not cadena:
        raise ValueError("Cadena vacía")
    
    cadena_limpia = ''.join(c for c in cadena if c.isalnum())
    if cadena_limpia == cadena_limpia[::-1]:
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error inesperado: {e}")
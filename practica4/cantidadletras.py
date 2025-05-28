try:
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra para buscar en la frase: ")
    if len(letra) != 1:
        raise ValueError("Debes introducir solo una letra.")
    cantidad = frase.lower().count(letra.lower())
    print(f"La letra '{letra}' aparece {cantidad} veces en la frase.")
except ValueError as e:
    print("Error:", e)

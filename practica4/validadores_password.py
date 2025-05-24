try:
    contraseña = input("Ingrese una contraseña: ")
    mensajes_error = []
    
    if len(contraseña) < 10:
        mensajes_error.append("Contraseña demasiado corta.")
    if not any(c.isdigit() for c in contraseña):
        mensajes_error.append("Debe contener al menos un número.")
    if not any(c in "!@#$%^&*()_+{}[]:;<>,.?~" for c in contraseña):
        mensajes_error.append("Debe contener al menos un carácter especial.")
    
    if mensajes_error:
        print("\n".join(mensajes_error))
    else:
        print("Contraseña válida.")
        
except Exception as e:
    print(f"Error inesperado: {e}")
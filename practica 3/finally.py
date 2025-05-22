try:
    num = int(input("Ingresa un número: "))
    resultado = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
finally:
    print("este bloque de codigo se va a ejcutar si ocurre una excepcion o no")
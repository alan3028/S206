try:
    num = int(input("Ingresa un número: "))
    resultado = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

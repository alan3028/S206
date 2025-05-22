def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as e:
    print(f"Error: {e}")

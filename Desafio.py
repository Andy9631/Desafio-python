def es_primo(n):
    """Devuelve True si n es un número primo, de lo contrario False."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

# Encuentra todos los números primos entre 1 y 250
primos = []
for num in range(1, 251):
    if es_primo(num):
        primos.append(str(num))

# Guarda los resultados en el archivo results.txt
with open("results.txt", "w") as archivo:
    archivo.write("\n".join(primos))
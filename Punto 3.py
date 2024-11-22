def numero_mayor(numeros):  
    """  
    Determina el número mayor en una lista de números.  
  
    Parámetros:  
    numeros (list): Lista de números.  
  
    Retorna:  
    number: El número mayor en la lista.  
    """  
    if not numeros:  
        return None  # Retorna None si la lista está vacía  
  
    mayor = numeros[0]  # Suponemos que el primer número es el mayor inicialmente  
    for numero in numeros:  
        if numero > mayor:  
            mayor = numero  
    return mayor  
  
# Ejemplo de uso  
numeros = [3, 41, 52, 26, 38, 57, 9, 49]  
mayor = numero_mayor(numeros)  
if mayor is not None:  
    print(f"El número mayor en la serie es: {mayor}")  
else:  
    print("La lista de números está vacía.")  

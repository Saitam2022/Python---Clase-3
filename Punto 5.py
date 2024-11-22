def calcular_factorial(n):  
    """  
    Calcula el factorial de un número entero positivo.  
  
    Parámetros:  
    n (int): El número entero positivo del cual se desea calcular el factorial.  
  
    Retorna:  
    int: El factorial del número dado.  
    """  
    if n < 0:  
        raise ValueError("El número debe ser un entero positivo.")  
    elif n == 0 or n == 1:  
        return 1  
    else:  
        factorial = 1  
        for i in range(2, n + 1):  
            factorial *= i  
        return factorial  
  
# Ejemplo de uso  
numero = int(input("Introduce un número entero positivo: "))  
try:  
    resultado = calcular_factorial(numero)  
    print(f"El factorial de {numero} es: {resultado}")  
except ValueError as e:  
    print(e)  

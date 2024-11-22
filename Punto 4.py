def dibujar_rectangulo(filas, columnas):  
    """  
    Dibuja un rectángulo de X filas y X columnas.  
  
    Parámetros:  
    filas (int): Número de filas del rectángulo.  
    columnas (int): Número de columnas del rectángulo.  
    """  
    for i in range(filas):  
        print('*' * columnas)  
  
# Ejemplo de uso  
filas = int(input("Introduce el número de filas: "))  
columnas = int(input("Introduce el número de columnas: "))  
dibujar_rectangulo(filas, columnas)  

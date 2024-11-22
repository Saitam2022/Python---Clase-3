def calcular_promedio(notas):  
    """  
    Calcula el promedio de una lista de notas.  
  
    Parámetros:  
    notas (list): Lista de números representando las notas.  
  
    Retorna:  
    float: El promedio de las notas.  
    """  
    if not notas:  
        return 0  # Retorna 0 si la lista de notas está vacía  
  
    suma = sum(notas)  
    cantidad = len(notas)  
    promedio = suma / cantidad  
    return promedio  
  
# Ejemplo de uso  
notas = [85, 90, 78, 92, 88]  
promedio = calcular_promedio(notas)  
print(f"El promedio de las notas es: {promedio}")  

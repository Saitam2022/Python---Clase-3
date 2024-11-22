def es_color_primario(color):  
    """  
    Determina si un color es primario e imprime un mensaje correspondiente.  
  
    Parámetros:  
    color (str): El nombre del color a verificar.  
    """  
    # Lista de colores primarios  
    colores_primarios = ['rojo', 'azul', 'amarillo']  
      
    # Convertimos el color a minúsculas para hacer la comparación a mayúsculas/minúsculas  
    color = color.lower()  
      
    if color in colores_primarios:  
        print(f"El color {color} es primario.")  
    else:  
        print(f"El color {color} no es primario.")  
  
# Ejemplo de uso  
es_color_primario("Rojo")  
es_color_primario("Verde")  

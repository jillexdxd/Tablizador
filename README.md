# Tablizador

## Clase (Tabla) Uso:
  ### 1. Importar tabla desde tablizador
    from Tablizador import Tabla

  ### 2. Asignar las cabeceras para describir el contenido (columnas o campos)
    
    cabeceras = ["Col 1", "Col 2", "Col 3"]

  ### 3. Asignar el contenido a una matriz (filas)
    
    contenido = [["El 1", "El 2", "El 3"],
                ["El 4", "El 5", "El 6"],
                ["El 7", "El 8", "El 9"],
                ["El 10", "El 11", "El 12"],
                ["El 13", "El 14", "El 15"],
                ["El 16", "El 17", "El 18"]]
                
  ### 3. Instancio el objeto tabla con el primer parametro de las cabeceras y el segundo del contenido

    tabla = Tabla(cabeceras, contenido)
    
  ### 4. Ya podemos imprimir la tabla bien formateada
  
    tabla.imprimir()

# Ejemplos:
 ![asd](https://user-images.githubusercontent.com/96015392/210078200-5ca10006-0b68-44dc-9e96-151b28458989.PNG)

from Tablizador import Tabla

#Uso:
#Asigno las cabeceras para describir el contenido (columnas o campos)
cabeceras = ["Col 1", "Col 2", "Col 3"]

#Asigno el contenido a una matriz
contenido = [["El 1", "El 2", "El 3"],
            ["El 4", "El 5", "El 6"],
            ["El 7", "El 8", "El 9"],
            ["El 10", "El 11", "El 12"],
            ["El 13", "El 14", "El 15"],
            ["El 16", "El 17", "El 18"]]


#Instancio el objeto tabla con el primer parametro de las cabeceras y el segundo del contenido
tabla = Tabla(cabeceras, contenido)

#Ya podemos imprimir la tabla bien formateada
tabla.imprimir()
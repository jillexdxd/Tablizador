class Tabla:

    def __init__(self, head, content):
        self.head = head
        self.content = content
        self.longCol = self.__calcularTabla()

    #Necesito calcular las dimensiones máximas de las columnas para centrarlas dinamicamente y correctamente. devolverá por ejemplo: [2, 5, 10]
    def __calcularTabla(self):
        lengths = []
        numCol = []

        # Recibo los atributos pero los casteo a string para calcular lo que ocupan
        head = [str(el) for el in self.head] 
        content =  [str(el) for el in self.content]

        for col in head:
            numCol.append(len(col))
        lengths.append(numCol)

        for fil in content:
            lengths.append([])
            for el in fil:
                lengths[len(lengths)-1].append(len(el))

        longCol = []

        #En el caso de que la tabla sea asimétrica
        try:
            for c in range(len(lengths[0])):
                may = 0
                for f in range(len(lengths)):
                    if lengths[f][c] > may:
                        may = lengths[f][c]
                longCol.append(may+2)
            
            return longCol
        except Exception:
            print("La tabla no es simetrica, asegurese que todas las filas incluyendo las cabeceras tengan la misma cantidad de columnas")
            return None



    def imprimir(self):            
        longCol = self.longCol
        if longCol == None:     #Si la tabla es asimétrica __calcularTabla() devuelve None, por lo cual se interrumpe el metodo imprimir
            return None

        linea = ""
        for el in longCol:
            linea += "+" + "-"*el
        linea += "+"

        #Ahora asigno mis filas incluidas las columnas a solo una matriz, haciendo mas comodo trabajar con ellas, inserto las cabeceras al principio
        tabla = self.content
        tabla.insert(0, self.head)

        for fil in tabla:
            print(linea)
            for col in range(len(fil)):
                print(f"|{fil[col]:^{longCol[col]}}", end="")
            print("|")
        print(linea)
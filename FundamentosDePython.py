def nuevoTema(tema):
    print("\n==========", tema, "========== \n")

#Este es un comentario
if __name__ == "__main__": #Es es otro comentario
    nuevoTema("Operadores aritméticos")
    print("Operador suma (\"+\"), 5 + 3 : ", 5 + 3)
    print("Operador cociente //, 5 // 3 : ", 5 // 3)
    print("Operador potencia (**), 5 ** 3 : ", 5 ** 3)

    nuevoTema("Operadores lógicos")
    print("Operador and (True and False): ", True and False)

    #Actividad: Imprimir la tabla de verdad de los operadores lógicos.

    nuevoTema("Operadores de comparación")
    print("2 == 3", 2 == 3)
    #Actividad: Agregar los demás operadores de comparación.

    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 6.2547
    Variable3 = "Pepe"

    dos_palabras = "Hola"

    print(variable1, _variable2, Variable3)

    a, b, c = 5, 10, "Welcome"
    print(a)
    print(b)
    print(c)

    nuevoTema("Enteros")
    w = 105
    x = 78658965265432
    y = -256
    z = 0b00110011
    d = 0xffa

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(d, type(d))

    nuevoTema("Flotantes")
    x = 1297.50
    print(x, type(x))
    y = 0.50594
    print(y, type(y))

    nuevoTema("Números complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema("Booleanos")
    lis = [8]
    print(lis, "is", bool(lis))

    t = ()
    print(t, "is", bool(t))

    new = "Hello"
    print(new, "is", bool(new))

    num = 99
    print(num, "is", bool(num))

    comp = 1 + 0j
    print(comp, "is", bool(comp))

    val = None #None equivale a Null
    print(val, "is", bool(val))

    nuevoTema("Listas")
    a = [10, 20.5, "Python List"]
    print(a)
    print(a[1])
    a[1] = "Hola"
    print(a)

    nuevoTema("Tuplas")
    t = (25, "tupla", 1 + 10j)
    print("t[1] = ", t[1])
    print("t[0:2] = ", t[0:2])
    #t[1] = "Hola"   #Operación no válida en tuplas.
    #print(t)

    nuevoTema("Conjuntos")
    a = {50, 20, 30, 10, 40}
    print("a = ", a)
    print(type(a))
    #print("a[1] = ", a[1]) #No tiene índice.

    nuevoTema("Diccionarios")
    d = {1:"Val1", 2:"val2"}
    print(d, type(d))
    print("d[1] = ", d[1])
    print("d[2] = ", d[2])

    nuevoTema("Cadenas")

    cadena1 = "Esto es una cadena"
    cadena2 = 'Esto también es una cadena'

    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))

    cadenaMultilinea = ''' Esto es una cadena
    de varias líneas    con     tabulares   y
    saltos
    de
    línea'''
    print(cadenaMultilinea, type(cadenaMultilinea))

    cadena3 = ''
    print(cadena3, type(cadena3))

    print("Segmentación de cadenas:")
    print(cadena1[5:11])
    print(cadena1[:5])
    print(cadena1[7:])
    print(cadena1[-8:-1])
    print(cadena1[0:18:1])
    print(cadena1[0:18:2])
    print(cadena1[0:18:3])

    cadena4 = (cadena1 + " ") * 5

    print(cadena4)

    nuevoTema("Tipos mutables e inmutables")
    #Cada objetos está definido por su identidad, tipo y valor.
    x = 10
    print("identidad: ", id(x))
    print("Tipos: ", type(x))
    print("Valor: ", x)

    lista1 = [1, 2, 3, 4]
    lista2 = list("6789")
    lista3 = [1, "Hola", 3.14, [1, 2, 3]]
    print("Lista1: ", lista1)
    print("Lista2: ", lista2)
    print("Lista3: ", lista3)

    conjunto = set(["Manzana1", "Manzana", "Manzana", "Pera", "Durazno", "Durazno"])
    print("Conjunto: ", conjunto)

    diccionario = {
        "Nombre": "Konrado",
        "Edad": "38",
        "Documento": 123456789
    }
    print("Diccionario: ", diccionario)
    print("Diccionario nombre", diccionario["Nombre"])

    '''
    nuevoTema("Entrada de datos desde teclado.")
    print("¿Cómo te llamas?")
    nombre = input()
    print("Hola ", nombre)

    aPaterno = input("¿Cuál es tu apellido paterno?")
    print(nombre + " " + aPaterno)

    aMaterno = input("¿Cuál es tu apellido materno?")
    print(nombre + " " + aPaterno + aMaterno)

    print(type(nombre))
    '''

    n1 = float(input("Ingresa un número: "))
    print(type(n1))

    n2 = float("32e10")
    print(n2)

    cadena = (234E47)
    print(cadena)
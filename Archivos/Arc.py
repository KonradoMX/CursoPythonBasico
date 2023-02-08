#import sys
#sys.path.append('../pythonProject1')

#from FundamentosDePython import nuevoTema

#nuevoTema("Archivos")

file = open("EjemploArchivo.txt", "w")
file.write("Este es el contenido del archivo")
file.close()

print("Archivo creado, escrito y cerrado")
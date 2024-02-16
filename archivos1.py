from io import open


#Crea el archivo
#archivo_texto=open('anombres.txt', 'a')
#r es de read
archivo_texto=open('anombres.txt', 'r')
#print(archivo_texto.read())
#print(archivo_texto.readlines())


#Establecer la posición donde queremos mandar llamar el cursor
#archivo_texto.seek(0)
#print(archivo_texto.read())


#archivo_texto.write('n datos en el archivo')


for lineas in archivo_texto.readlines():
    print(lineas.rstrip())
    
archivo_texto.close()
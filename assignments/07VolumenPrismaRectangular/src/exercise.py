def volumentotal (base,altura,profundidad):
    return base*altura*profundidad
def main():
    #escribe tu código abajo de esta línea
    base = input ("dame la base: " ) ##Tenias que converit a entero
##Indentar el código correctamente.
altura = input ("dame la altura: ")
profundidad = input ("dame la profundidad: ")

print ("el volumen total del prisma es:", volumentotal) ##Llamar la función con los parámetros requeridos entre paréntesis
    pass

if __name__=='__main__':
    main()

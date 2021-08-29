def volumentotal (base,altura,profundidad):
    return base*altura*profundidad
def main():
    #escribe tu código abajo de esta línea
    base = input ("dame la base: " )
altura = input ("dame la altura: ")
profundidad = input ("dame la profundidad: ")

print ("el volumen total del prisma es:", volumentotal)
    pass

if __name__=='__main__':
    main()

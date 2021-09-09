def Calbanene ():
    return albanene * 12 #cuál es el valor de albanene, al estar en main, no es una variable global

def Cplumones (): 
    return plumones * 35  #plumnos no es una variable global, debiste pasarlas como parámetros

def total ():
    return Cplumones/ Calbanene ##Llamado de funciones con paréntesis
def main():
    #escribe tu código abajo de esta línea
    plumones = input("dame la cantidad de plumones")
albanene = input ("dame la cantidad de papel ")

print ("el numero maximo de tarjetas que se puede hacer es de :",total) ##Llamado de funciones con paréntesis
    
    pass

if __name__=='__main__':
    main()

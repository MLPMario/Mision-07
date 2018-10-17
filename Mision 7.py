#Autor: Luis Mario Cervantes Ortiz
#Descripción: Uso de ciclos while


def dividirNum(dividiendo,divisor): #Función para saber la division de los números
    residuo = 0
    cociente = 0

    if dividiendo-divisor<0:
        print("Error de calculo") #Si no se puede dividir el numero
    else:
        while dividiendo - divisor >= residuo:
            residuo = divisor*cociente
            cociente = cociente + 1
        print(dividiendo, "/", divisor, "=", cociente-1, " y sobra", dividiendo-residuo)


def numMayor(): #Funcion para saber el numero mayor
    print("Teclee una lista de numeros para saber cual es el mayor")
    num_Mayor = 0
    numero=int(input("Teclee un número [Teclee -1 para salir]: "))

    if numero == -1:    #Al ingresar -1 antes de ingresar otros datos marca esto
        print("No hay valor")
    else:
        while numero != -1:
            if numero > num_Mayor:
                num_Mayor=numero
            numero=int(input("Teclee un número [Teclee -1 para salir]: "))
        print("El numero mayor es:",num_Mayor)


def leerOpcionMenu(): #El menu del programa
    print("Mision 07. Ciclos While")
    print("Autor: Luis Mario Cervantes Ortiz")
    print("Matricula: A01376958")
    print("1. Calcular divisiones")
    print("2. Encontrar el numero mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción:"))
    return opcion


def main(): #Se pregunta al ussuario que quiere hacer
    opcion = leerOpcionMenu()
    while opcion != 3:
        if opcion == 1:
            print("Calcula tu división ")
            dividiendo = int(input("Dime el dividiendo: "))
            divisor = int(input("Dime el divisor: "))
            dividirNum(dividiendo,divisor)
            opcion=leerOpcionMenu()
        elif opcion == 2:
            numMayor()
            opcion=leerOpcionMenu()
        elif opcion>3:
            print("Error, teclee 1,2 o 3 porfavor ")
            opcion=leerOpcionMenu()
    print("Gracias por usar el programa")


main()
def imprimir_menu():
    print("\t\t\tBienvenido al juego del ahorcado")
    print("1. Nuevo Juego")
    print("2. Salir")
def buscar_letra(palabra,letra,juego):
    for x in range(0,len(palabra)):
        if palabra[x]==letra:
            juego[x]=letra
    return juego
def cargar_posibilidades():
    lista_palabras = []
    f = open("Entrada.txt", "r")
    for linea in f:
        lista_palabras.append(linea)
    f.close()
    return lista_palabras
def crear_juego(numero,palabra):
    juego=[]
    for j in range(0,len(palabra)):
        juego.append("_")
    return juego
def intento(i,palabra,juego):
    letra=input("Ingrese una letra: ")
    if letra in palabra:
       juego=buscar_letra(palabra,letra,juego)
       cadena=""
       for c in juego:
           cadena=cadena+c
       print(cadena)
    else:
        i=i+1
        print("Uhhh, te equivocaste, ahora solo te quedan",7-i,"intentos")
    resultado=[i,juego]
    return resultado

def main():
    i=0
    import random
    imprimir_menu()
    opcion=eval(input("Ingrese una opcion (1/2): "))
    while opcion!=1 and opcion!=2:#Comprobamos la entra del usuarios sea valida
        print("Opcion invalida")
        imprimir_menu()
        opcion = eval(input("Ingrese una opcion (1/2): "))
    while opcion==1:
        if opcion==1:
            numero=random.randint(0,50)
            lista_palabras=cargar_posibilidades()
            palabra=list(lista_palabras[numero])
            palabra.remove("\n")
            juego=crear_juego(numero,palabra)
            resultado=[i,juego]
            while resultado[0]<=6 and ("_"in resultado[1]):
                resultado=intento(resultado[0],palabra,juego)
            if resultado[0]==7:
                print("Lo sentimos su ciudadano fue ahorcado")
            else:
                print("Felicitaciones Ganaste")
        imprimir_menu()
        opcion = eval(input("Ingrese una opcion (1/2): "))
main()

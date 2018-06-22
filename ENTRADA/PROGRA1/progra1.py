def calcular_salida(codigo, fichero): # Calcula una lista como salida
    salida = []  # Genera la lista vacia
    for linea in fichero:  # Recorre cada linea en el fichero
        for letra in linea:  # Recorre cada letra de la linea
            if (letra == '\n'): # Si el caracter es un salto de linea, entonces se lo agrega un salto de linea
                salida.append('\n')
            else: # Si no es, simplemente calcula el caracter equivalente dentro de la lista 'codigo'
                indice = codigo.index(letra) - 5
                salida.append(codigo[indice])
    return salida
def mostrar_salida(salida):
    cadena = "" # La cadena servira para imprimir todos los datos juntos
    for letra in salida: # Se agregan cada letra a la variable cadena
        cadena = cadena + (letra)
    print(cadena)
    return
def main():
    import msvcrt  # Para simular el pause
    codigo = [' ', '!', '"', '#', '$', '%', '&',
              "'", '(', ')', '*', '+', ',', '-', '.', '/', '0',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', ':',
              ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D',
              'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
              'Y', 'Z', '[', ' ', ']', '^', '_', '`', 'a', 'b',
              'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
              'x', 'y', 'z', '{', '|', '}', '~']
    fichero = open('progra1.txt', 'r')   # Lectura de datos del fichero
    salida = calcular_salida(codigo, fichero)  # Calcula salida
    mostrar_salida(salida) # Presenta salida
    msvcrt.getch()  # Para esperar un enter y salir
main()


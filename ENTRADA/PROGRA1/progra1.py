'''

Porgrama 1
'''
import msvcrt # Para simular el pause

codigo = [' ', '!', '"', '#', '$', '%', '&',
"'", '(', ')', '*', '+', ',', '-', '.', '/', '0',
'1', '2', '3', '4', '5', '6', '7', '8', '9', ':',
';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
'Y', 'Z', '[', ' ', ']', '^', '_', '`', 'a', 'b',
'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
'x', 'y', 'z', '{', '|', '}', '~', '',  '', '', '', '', '', '\n', '', '', '', '', '\n']

# Lectura de datos del fichero

fichero = open('progra1.txt', 'r')
def calcular_salida(codigo, fichero):
    salida = []
    for linea in fichero:
        for letra in linea:
            indice = codigo.index(letra) - 5
            salida.append(codigo[indice])
    return salida

def mostrar_salida(salida):
    cadena = ""
    for letra in salida:
        if (letra == '\n'):
            cadena = cadena + ('\n')
        else:
            cadena = cadena + (letra)

    print(cadena)
    return

salida = calcular_salida(codigo, fichero)
mostrar_salida(salida)



msvcrt.getch() # Para esperar un enter al salir

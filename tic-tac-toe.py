import colorama
from colorama import Fore
from colorama import Style
valorPorDefecto = "-"
JugadasPosibles = ["X","O"]

def printBoard ():
    for i in range(len(tablero)):
        print(tablero[i],end=" ")
        if (i + 1) % 3 == 0:
            print()

def printBoardFinal (solucion):
    for i in range(len(tablero)):
        if solucion.count(i)>0:
            print(f"{Fore.GREEN}{Style.BRIGHT}{tablero[i]}{Style.RESET_ALL}",end=" ")

        else : print(tablero[i],end=" ")
        if (i + 1) % 3 == 0:
            print()

def evaluarTablero ():
    result = 0
       # 0
    if (tablero[0] == tablero[1] == tablero[2] and tablero[0]!=valorPorDefecto)  :
        result = tablero[0]
        printBoardFinal([0,1,2]) 
    elif (tablero[0] == tablero[3] == tablero[6] and tablero[0]!=valorPorDefecto): 
        result = tablero[0]
        printBoardFinal([0,3,6]) 
    elif  (tablero[0] == tablero[4] == tablero[8] and tablero[0]!=valorPorDefecto):  
        result = tablero[0]
        printBoardFinal([0,4,8]) 
    #1
    elif (tablero[1] == tablero[4] == tablero[7] and tablero[1]!=valorPorDefecto):
        result = tablero[1]
        printBoardFinal([1,4,7]) 
    #2 

    if (tablero[2] == tablero[5] == tablero[8] and tablero[2]!=valorPorDefecto) :
        printBoardFinal([2,5,8]) 
        result = tablero[2]
    elif (tablero[2] == tablero[4] == tablero[6] and tablero[2]!=valorPorDefecto):
        printBoardFinal([2,4,6]) 
        result = tablero[2]
    #3
    elif (tablero[3] == tablero[4] == tablero[5] and tablero[3]!=valorPorDefecto):
        printBoardFinal([3,4,5]) 
        result = tablero[3]
    #6
    elif (tablero[6] == tablero[7] == tablero[8] and tablero[6]!=valorPorDefecto):
        printBoardFinal([6,7,8]) 
        result = tablero[6]
    
    if result == 0: 
        if tablero.count(valorPorDefecto) == 0 : 
            print ("empate")
            printBoard() 
            return False
        return True
    else: 
        print(f"Gano el jugador: {result}")
        return False

def jugada (turno):
    while True:
    
        jugadaActual =input(f"Ingrese un numero para {JugadasPosibles[turno]}: ")
        if jugadaActual.isdigit():
            jugadaActual = int(jugadaActual) -1
            if  jugadaActual <=8 and jugadaActual >= 0:
                if tablero[jugadaActual ] == valorPorDefecto :

                    tablero[jugadaActual]=JugadasPosibles[turno]

                    break
                else: 
                    print("jugada invalida La celda ya este ocupada")
                    printBoard()
            else: 
                print("jugada invalida por favor ingrese un numero entre 1 y 9")
                printBoard()
        else: 
            print("jugada invalida por favor ingrese un numero entre 1 y 9")
            printBoard()

def play ():
    numJugadas = 0

    while numJugadas < 9:  
   
        turno = 0
        while turno < 2: 
            printBoard()
            jugada(turno)
            numJugadas+=1                
            turno+=1
            if numJugadas >= 5: 
                continuarJugando = evaluarTablero()
                if not(continuarJugando) :
                    return
print(
f"""Bienvenido a Tic Tac Toe
>se necesitan dos jugadores para empezar.   
>El juego consiste en ir dibujando X/O en las diferentes celdas.
>La forma de ganar es que alguno de los dos pueda lograr que tres de las posibilidades (X/O) queden continuas,
puede ser de forma horizontal, vertical o diagonal. 
Ejemplos de cuando gana X:
   Diagonal  Horizontal  Vertical
    X O X     X X X       X O -
    O X O     O O -       X O -
    X - -     - - -       X - -

>Instrucciones de juego

Para poder jugar se le va a solicitar el numero en donde quiere depositar su jugada. 
Las posibilidades son:
    1 2 3
    4 5 6 
    7 8 9
Aclaracion importante, si la celda esta ocupada o se ingresa alguna posicion distinta a las que son 
validas para jugar se le notificara que la jugada es invalida y se le va a pedir que ingrese nuevamente 
la posicion.
""")        
jugar = input ("presione enter para continuar")
jugar = True
while jugar:
    tablero =[valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto]
    play()
    continuar = input ("quiere seguir jugando? Ingrese n o no para salir, y cualquier otra tecla para continuar jugando: ")
    print(continuar)
    continuar = continuar.lower()
    if continuar.startswith("n"):
        jugar = False
        print("Usted ha decidido cerrar el juego. Saludos")
    
    

import colorama
from colorama import Fore
from colorama import Style
valorPorDefecto = "-"
tablero =[valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto,valorPorDefecto]
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

def evaluar ():
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
            return False
        return True
    else: 
        print(f"Gano el jugador: {result}")
        return False

def jugada (turno):
    while True:
        jugada =input("Ingrese un numero: ")
        if jugada.isdigit():
            jugada = int(jugada) -1
            if tablero[jugada ] == valorPorDefecto and jugada <=8 and jugada >= 0:
                if turno == 1:
                    tablero[jugada]="X"
                else : tablero[jugada]="O"
                break
            else: 
                print("jugada invalida vuelve a intentarlo")
                printBoard()
        else: 
            print("jugada invalida vuelve a intentarlo")
            printBoard()

def play ():
    numJugadas = 0

    while numJugadas < 9:  
   
        turno = 1
        while turno < 3: 
            printBoard()
            jugada(turno)
            numJugadas+=1                
            turno+=1
            if numJugadas >= 5: 
                continuar = evaluar()
                if not(continuar) :

                    return
        



play()
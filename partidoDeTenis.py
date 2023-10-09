
""" * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
 """


def impresion(player1, player2):
    ipl1 = ""
    ipl2 = ""
    result = ""
    if player1 == 3 and player2 == 3:
        result = "deuce"
    elif player1 == 4 and player2 == 3:
        result = "Ventaja P1"
    elif player2 == 4 and player1 == 3:
        result = "Ventaja P2"
    elif player1 >= 4  :
        result = "Ganó P1"
    elif player2 >= 4:
        result = "Ganó P2"

    else : 
        if player1 == 0:
            ipl1 = "Love"
        elif player1 == 1:
            ipl1 = "15"
        elif player1 == 2:
            ipl1 = "30"
        elif player1 == 3:
            ipl1 = "40"

        if player2 == 0:
            ipl2 = "Love"
        elif player2 == 1:
            ipl2 = "15"
        elif player2 == 2:
           ipl2 = "30"
        elif player2 == 3:
            ipl2 = "40"

    return  result if len(result) != 0 else f"{ipl1} - {ipl2}"


def puntaje(list):
    p1 = 0
    p2 = 0
    for i in range(len(list)):
        if list[i] == "P1":
            p1 += 1
        elif list[i] == "P2":
            p2 += 1
        else: 
            print(f"No puedo procesar el dato en la posicion {i}")
            break
        if p1 == 4 and p2 == 4:
            p1 -= 1
            p2 -= 1

        result = impresion(p1, p2)
        print(result)
        if result.startswith("Gan"):
            break


        


puntos = ["P1","P2","P2","P2", "P1", "P1", "P2", "P1", "P2", "P2"]

puntaje(puntos)

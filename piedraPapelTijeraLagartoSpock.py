""" /*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
Reglas
Tijeras cortan papel
Papel cubre piedra
Piedra aplasta lagarto
Lagarto envenena Spock
Spock destruye tijeras
Tijeras decapitan lagarto
Lagarto come papel
Papel desaprueba Spock
Spock vaporiza piedra
Piedra aplasta tijeras"""

movimientos = ["🗿","📄","✂️","🦎","🖖" ]
movimientosLetra =["r","p","t","l","s"] 
def reglas (a,b):
    if a==b:
        return 0
    if a == "✂️":
        if b == "🗿":
            return -1
        elif b == "🦎":
            return 1
        elif b == "🖖":
            return -1
        else :#b == "📄":
            return 1
    elif a == "🗿":
        if b == "✂️":
            return 1
        elif b == "🦎":
            return 1
        elif b == "🖖":
            return -1
        else :#b == "📄":
            return -1
    elif a == "🦎":
        if b == "✂️":
            return -1
        elif b == "🗿":
            return -1
        elif b == "🖖":
            return 1
        else :#b == "📄":
            return 1       
    elif a == "📄":
        if b == "✂️":
            return -1
        elif b == "🗿":
            return 1
        elif b == "🖖":
            return 1
        else :#b == "🦎":
            return -1       
    else: # a == "🖖":
        if b == "✂️":
            return 1
        elif b == "🗿":
            return 1
        elif b == "📄":
            return -1
        else :#b == "🦎":
            return -1                          

def puntaje (entrada):
    resultado = 0
    for i in range(len(entrada)):

        a,b = entrada[i]
        if a in movimientos and b in movimientos:
            resultado += reglas(a,b)
        elif a not in movimientos:
            return "Player 1 hizo un movimiento invalido"
        else:
            return "Player 2 hizo un movimiento invalido"
    
    if(resultado==0):
        return "Tie"
    elif resultado <0:
        return f"Ganador Player 2"
    else: return f"Ganador Player 1"

def inicioJuego():
    inp = ""
    while inp == "" or inp!= "no" :
        while True:
            print("""Los posibles movimientos son:  
            >p para PAPEL "📄" >t para TIJERAS  >s para SPOCK "🖖" >r para PIEDRA (rock) "🗿" >l para Lagarto "🦎" 
            """)
            userInput= input(f" Ingrese movimiento player 1: ")
            if userInput in movimientosLetra:
                userInput = movimientos[movimientosLetra.index(userInput)]
                break 
        while True:
            print("""Los posibles movimientos son:  
            >p para PAPEL "📄" >t para TIJERAS  >s para SPOCK "🖖" >r para PIEDRA (rock) "🗿" >l para Lagarto "🦎" 
            """)
            user2Input= input(f" Ingrese movimiento player: 2: ")
            if user2Input in movimientosLetra:
                user2Input = movimientos[movimientosLetra.index(user2Input)]
                break 
        
        entrada.append ((userInput,user2Input))
        print(entrada)
        print("Desea continuar?")
        inp = input("enter para continuar, no para salir")

entrada= []#("🖖","🗿"),("🗿","✂️"), ("✂️","🗿"), ("📄","🗿")

        

""" # testing
for i in movimientos: 
    for j in movimientos:
        tupla = (i,j)
        entrada.append(tupla)
        print(entrada)
        resultado = puntaje(entrada)
        print (f"Resultado: ({resultado})")
    entrada.clear()
"""
inicioJuego()
print(f"Movimientos:  {entrada}")
resultado = puntaje(entrada)
print (f"Resultado: {resultado}")



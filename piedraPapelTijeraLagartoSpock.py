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
    elif a == "🖖":
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
        return f"Player 2 {resultado}"
    else: return f"Player 1 {resultado}"

entrada= [("🖖","🗿"),("🗿","✂️"), ("✂️","🗿"), ("📄","🗿")]#

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

print(f"Movimientos:  {entrada}")
resultado = puntaje(entrada)
print (f"Resultado: {resultado}")



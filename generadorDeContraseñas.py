import random
"""/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "<", ">", "/", "?", "|"]

def generatePassword(num):
    if num <=16 and num >= 8:     
        pwd = ""
        for i in range(num+1):
            random_integer = random.randint(1, len(letters))-1  # Generates a random integer between 1 and 100
            pwd= pwd + letters[random_integer]
        return pwd

#lenght = int(input("ingrese la longitud que va a tener la contraseña: "))
for i in range(8,178):
    if i <=16 and i >= 8: 
        pwd=generatePassword(i)
        print(pwd)
    else:
        print("Longitud invalida para la contraseña, debe tener una longitud entre 8 y 16.\nNo se pudo ejecutar el generador de contraseñas. ")

        
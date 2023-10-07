# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


def replace(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "fizz"
    else:
        return num


def replace2(num):
    return "fizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Buzz" if num % 5 == 0 else "fizz" if num % 3 == 0 else num


for i in range(1, 101):
    j = replace2(i)
    print(i)

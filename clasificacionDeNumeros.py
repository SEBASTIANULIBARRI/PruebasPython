"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */"""
import math

def esPar(num):
    return "es par" if num%2==0 else "es impar"
def fib (num):
    previous =0 
    actual = 1
    if previous== num:
       return "es un numero de fibonacci" 
    
    while actual< num:
        aux = actual
        actual+= previous
        previous=aux
   
    if actual== num:
        return "es un numero de fibonacci"
    else: # Si viene por acaa es que no existe el num dentro del arreglo
        return "no es un numero de fibonacci" 
 

def esPrimo(num):
    if num >1:
        roof = math.floor(math.sqrt(num))+1
        for i in range(2,roof):
            if num%i == 0: 
                return "no es primo"
            
        return "es primo"
    else :     return "no es primo"


for i in range(0,1000):
    print(f" el numero {i}: {esPar(i)}, {esPrimo(i)} y {fib(i)}")


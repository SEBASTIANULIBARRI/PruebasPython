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

def esPrimo(num):
    if num >=0:
        roof = math.floor(math.sqrt(num))+1
        for i in range(2,roof):
            if num%i == 0: 
                return "no es primo"
            
        return "es primo"
    else :     return "no es primo"
for i in range(2,35):
    print(f" el numero {i}: {esPar(i)}  y {esPrimo(i)}")


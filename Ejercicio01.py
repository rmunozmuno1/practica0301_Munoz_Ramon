"""Escribir dos funciones, una función que reciba un número entero positivo n y
 calcule el número de fibonacci asociado a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta."""
import datetime
def calculo_recursivo(n):
    if n <=1:
        return n
    else:
        return calculo_recursivo(n-1) + calculo_recursivo(n-2)

St = datetime.datetime.now()
print (calculo_recursivo(10))
Et = datetime.datetime.now()
print (Et - St)
"""Esta funcion nos realiza un codigo fibonacci mediante calculo recursivo tenemos una entrada llamada n y despues nos metemos en 
una condición si n es menor o igual a 1 devolvera el calcula n y si no realizara el calculo n-1 + n-2 haciendo un return hasta 
que n sea menor o igual a 1"""

def calculo_bucle(n):
    
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
St = datetime.datetime.now()
print   (calculo_bucle(10))
Et = datetime.datetime.now()
print (Et - St)

        








    

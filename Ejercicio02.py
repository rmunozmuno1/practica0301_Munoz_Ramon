"""Escribir una función que lea dos ficheros csv con una lista 
larga de datos de personas (50 personas y 1000 personas) y 
llame a dos funciones que pongan su nombre en formato capitalizado y 
calculen la letra de DNI correspondiente. 
Realiza la comprobación de rendimiento con la librería cProfile y muestra los datos.
 Describe que indica cada dato que nos proporciona cProfile."""
import cProfile
def Capital_(a):
    for i in a:
        nombre = i.title()
        print (nombre)
def letra(b):
    Dict_letras = {0:'T',1:'R',2:'W',3:'A',4:'G',5:'M',6:'Y',7:'F',8:'P',9:'D',10:'X',11:'B',12:'N',13:'J',14:'Z',15:'S',
              16:'Q',17:'V',18:'H',19:'L',20:'C',21:'K',22:'E',}
    for i in b:
        a = i.split(",")
        numero = a[1].strip()
        numero = int(numero)
        letra_del_DNI = Dict_letras[numero % 23]
        print ('DNI', a[1], 'La letra es',letra_del_DNI)
def procesamiento_del_fichero_CSV():
    fich = input('Introduzca el nombre de uno de estos dos ficheros: 50.csv o 100.csv')
    with open(fich, 'r') as file:
        lista = file.readlines()
    Capital_(lista)
    letra(lista)
cProfile.run('procesamiento_del_fichero_CSV()')
#creamos un archivo 
##guaedamos en la carpeta del repositor 
#con la extencion .py
#uso numeros aleatorio


from random import randint
aleatoriorandint=(0,20)        #cramos una variable
#y generamos un numero aleatorio entre 0 y 20
print(aleatorio)                #imprimimos en numeros generados


#ejercicios 
#escibir una funcion sorteo() y que reciba 
#una lista de practicantes, y elegir a uno 
#de los practicas aleatoriamente, y 
#retornar esa persona elegida 
#desafio:no volver a retornar a esa persona
#   ya sorteada


from random import randint            
def sorteo(lista_participantes):  #agregar las listas de partisipantes 
    cant=len (lista_participantes)-1
    aleatorio=randint(0,cant)     #creamos una variable
    return lista_participantes[aleatorio]
lista_participantes=["Jaz","Maria","Leo"]    #crear los nombres de los participantes
ganador=sorteo(lista_participantes)
print(ganador)                    #imprimos en numero generado

#DESAFIO: no volver a una persona ya sorteada

from random import randint            
def sorteo(lista_participantes):  
    cant=len (lista_participantes) -0
    aleatorio=randint(0,cant)  
    return lista_participantes[aleatorio]
lista_participantes=["Jaz","Maria","Leo"] 
lista pop=[]  
ganador=sorteo(lista_participantes)
print(ganador) 

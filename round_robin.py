from tabulate import tabulate
from Processo import Processo
import multiprocessing
import os

processo = Processo()

fila = processo.get_lista_processos()

resultados = []

print (fila[1])

print("------------> PROCESSOS <------------")
for process in fila:
    print (process)
    resultados.append(process['burst_time'])
print("\n\n")

print("------------> RESULTADOS <------------")
print (resultados)
print("\n\n")

while (len(resultados) > 0) :
    cont = 0
    for processo in resultados :
        quantum = 5

        quanta = resultados[0] - quantum

        if (quanta <= 0) :
            resultados[1] = quanta
            resultados.pop(cont)
            print("BURST CONCLUÍDO : PROCESSO ", resultados[0])
            print(resultados)

        else :
            resultados[1] = quanta
            print("PROCESSO ", fila[0] , "FALTA ", resultados[1])
            print("Contador ", cont)
            cont = cont + 1

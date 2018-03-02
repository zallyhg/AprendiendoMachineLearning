
from math import pow, sqrt

#Obtener media
defmedia(datos):
    sumatoria = sum(datos)
    n = len(datos)
    result = sumatoria / n
    return result

#Obtener la varianza
defvarianza(datos):
    v_media = media(datos)
    varianzalist = []
    for i in datos:
        i = pow((i - v_media), 2)
        varianzalist.append(i)

    v_varianza = sum(varianzalist) / len(varianzalist)
    return v_varianza

#Obtener la desviacion Estandar
defdesviacionEstandar(datos):
    desviacion = sqrt(varianza(datos))
    return desviacion

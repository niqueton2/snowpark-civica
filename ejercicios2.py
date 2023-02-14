# Falto profe, los pibes arman la clase, s epide nombre y edad de la peña 


def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        
        nombre = input('Ingrese el nombre del pana: ')
        edad = int(input ('Ingrese edad del pana: '))
        compañero= (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key = lambda x:x[1])
    asistente = compañeros[0][0]
    profe = compañeros[-1][0]
    return asistente,profe

asis,profe = obtener_compañeros(5)

print(f'El profesor es {profe} y su asistente es {asis}')
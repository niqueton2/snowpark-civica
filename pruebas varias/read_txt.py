
# Lo primero lo abrimos

archivo_sin_leer= open('hey.txt',encoding='UTF-8')

# Lo podemos leer entero en una variable

#archivo=archivo_sin_leer.read()

# Lo podemos leer encapsulanod cada linea en un elemento d eun array

archivo = archivo_sin_leer.readlines()

# También leer solo la primera linea con readline()

print (archivo)
# Finalmente lo cerramos con 
archivo_sin_leer.close()


# Para leer txt de mejor manera

with open('hey.txt'):
    #Se abre, se jecuta el bloque este y luego se cierra automátic
    print('hola');
    

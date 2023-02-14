# Usando el operador * podemos hacer que varias variables de entradfa sean una
# digamos que rellena una lista con los elementos que le damos

# def suma(*numeros):
#     return sum(numeros)

# resultado= suma(1,3,5,7,8,9,6,7)
# print(resultado)

# funciones lmabda , son anónimas y se almacenan en una variables

# multiplicar_por_dos = lambda x : x*2

# Sencillo y rápido, no hace falta return, no apta para hacer más de un cálculo


numeros = [1,2,3,4,5,6,7,8,9,10]

def es_par(num) :
    if num % 2 == 0:
        return True
    
numeros_pares = filter(es_par,numeros)

a = list(numeros_pares)
print(a)

# Forma rápida de harlo con lambda, devulve true si metemos una condición
numeros_impares = filter(lambda numero:numero%2 == 1,numeros)

import streamlit as st


st.write(" Test del Gaylord  ")



nombre = st.text_input('¿Estas preparado?, Dime como te llamas valiente : ')

def saludo(nombre,formal=True):
    if formal:
        return (f'Buenas {nombre}, es un gusto conocerte')
    else:
        return (f'Que pasa {nombre}, como vas perranco')


amigos=['Carlos','Diego','Iñigo','Asier','Pepe','Gonzalo','Iñigo']

print(f'nombre: {nombre}')

if nombre in amigos:
    apoyo1=saludo(nombre,False)
elif bool(nombre):
    apoyo1='La primera mayúscula si no te importa'
else:
    apoyo1=saludo(nombre)




   
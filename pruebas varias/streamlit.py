import streamlit as st
import pandas as pd

lista1 = ['Eugenio', 'Leopoldo']
df=pd.DataFrame(lista1,columns=['Afortunados'])

st.header('CHEKEATE ESTA APP  :sunglasses:')
st.subheader('Todo lo que sé me lo enseño Mayorgas')

nombre = st.text_input('Dime tu nombre campeón/a :')
df_2=pd.DataFrame([nombre],columns=['Afortunados'])

if nombre:
    df_3=pd.concat([df,df_2])
    st.write('Felicidades!! ',df_3, 'Has entrado en la lista de gente que me come los huevos \n',' ( por debajo del culo )')
    a=0


if st.button('Pinchame anda'):
    st.write('Buena pinchada perri')
    a=1;
    st.write('')
    
    
nota = st.slider('¿Como te sientes ?',0,10)
    
if nota:
        st.write('Me refería a como de gilipollas te sientes en realidad')
        
        if nota<5:
            st.write('¿Solo un ',nota,' ? Pues pareces más tio')
        elif nota<8:
            st.write('Un ',nota,' no está mal, pero tu concretamente aspiras a más')
        else:
            st.write(' Un ',nota,' !! Eso ya es que lo eres, enhorabuena jefe')
    

ydat=[10,8,9,6,5,4,3,1,-1,0,-2]

df_y=pd.DataFrame(ydat)


c1,c2 = st.columns(2)

c1.line_chart(df_y)

option = c2.selectbox('¿A que crees que corresponde esta gráfica ?',('Mmmmmm','Mi desempeño sexual en los últimos tiempos ',' Evolución de la luz del sol que recibo',' Fluctuación del precio de mi alma'))
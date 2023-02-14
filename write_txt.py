# Con la 'w' podemos escribir y sobreescribir si pusiesemos 'a' solo podemos agregar 

with open('hey.txt','w',encoding='UTF-8') as archivo:
    
    # Sobreescribiendo el archivo
    
    archivo.write('Hey bro \n como vas wey')
    
    # Con esto no se sobreescribe, se añade a lo q hay
    
    archivo.writelines(['Que pasa loco \n','Estas activo?'])
    

import csv


# así es como la libreria csv

# with open('huy.csv') as archivo:
#     reader = csv.reader(archivo)
#     for row in reader:
#         print(row)
        

# Con pandas vamos más chetados

import pandas as pd

df = pd.read_csv('huy.csv',names=['Nombre','Apellido','Edad'])

df_1 = df.sort_values('Edad')

print(df_1)
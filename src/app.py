import pandas as pd
import numpy as np
from datetime import datetime

# lectura de archivo de data
df = pd.read_csv('/workspaces/Caso_Uso_S4/data/process/DataSet.csv',sep='|')
# guardar cantidad de filas y columnas
filas = df.shape[0]
columnas = df.shape[1]
print(f'El archivo ha sido procesado correctamente, posee {filas} filas y {columnas} columnas')

# Muestre la %de1 que hay en el dataset
# print(df['top'].value_counts(1))
porc_target = df['top'].value_counts(1)[1]
print(f'El archivo cuenta con {porc_target} de artistas que pertenecen al top 100 de los premios billboard')

# Guardar el porcentaje final
fecha = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'/workspaces/Caso_Uso_S4/data/OutPut/OutputFinal_{fecha}.csv'
df['top'].value_counts(1).to_csv(filename,
                                 sep='|',
                                 index=False)
print('Proceso Culminado, Archivo generado Satisfactoriamente')
print(f'Nombre del Archivo {filename}')
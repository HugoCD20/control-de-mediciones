from models.Bd import medicionesQuery, semanaQuery, data_sets
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

semanas = semanaQuery()
def operacion_dataset(dataset):
    data_set = np.array(dataset)
    size= data_set.size
    data_set = np.reshape(data_set, shape=(1,size), order="C")
    return data_set

def establecer_dataset(semana):
    temperatura, humedad, fecha = data_sets(semana)
    temperatura_dataset = operacion_dataset(temperatura)
    humedad_dataset = operacion_dataset(humedad)
    fecha_dataset = operacion_dataset(fecha)
    return temperatura_dataset, humedad_dataset, fecha_dataset



temperatura_dataset, humedad_dataset, fecha_dataset = establecer_dataset(1)

df = pd.DataFrame({
    'fecha': fecha_dataset[0],
    'temperatura': temperatura_dataset[0],
    'humedad': humedad_dataset[0]
})

df['fecha']=pd.to_datetime(df['fecha'],dayfirst=True)
df_resample = df.resample('D', on='fecha').mean()

plt.plot(df_resample.index, df_resample['temperatura'])
plt.show()


from models.Bd import medicionesQuery, semanaQuery, data_sets
from matplotlib import pyplot as plt
import numpy as np

semanas = semanaQuery()

temperatura, humedad, fecha = data_sets(semanas[0][0])

temperatura_data_set = np.array(temperatura)

s_temperatura = temperatura_data_set.size

temperatura_dataset = np.reshape(temperatura_data_set, shape=(1,s_temperatura), order="C")

print(temperatura_dataset)

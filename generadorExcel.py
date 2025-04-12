from models.Bd import medicionesQuery, semanaQuery
import pandas as pd

semanas = semanaQuery()

with pd.ExcelWriter("mediciones_por_semana.xlsx", engine="openpyxl") as writer:
    for i in semanas:
        datos = []
        medicion = medicionesQuery(i[0])

        for l in medicion:
            senso = {
                "Temperatura": l[2],
                "Humedad": l[3],
                "Fecha": l[4]
            }
            datos.append(senso)

        df = pd.DataFrame(datos)
        nombre_hoja = f"Semana_{i[1]}" 
        df.to_excel(writer, sheet_name=nombre_hoja, index=False)

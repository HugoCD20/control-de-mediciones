import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from models.Bd import generarSemana as nSemana, insertMedicion as insertar
import re

# Inicializar Firebase
cred = credentials.Certificate('credentials/credenciales.json')
firebase_admin.initialize_app(cred)

baseDatos = firestore.client()
doc_ref = baseDatos.collection('Temperatura').order_by('fecha')  # Ordenar por el campo 'fecha'
docs = doc_ref.get()

id_semana = nSemana()

def formatear_fecha(fecha):
    """Convierte la fecha en string ISO o datetime a un formato legible."""
    if isinstance(fecha, str):
        try:
            fecha = datetime.fromisoformat(fecha)
        except ValueError:
            print(f"⚠ Error al convertir la fecha: {fecha}")
            return None
    return fecha.strftime("%Y-%m-%d %H:%M:%S")  

for doc in docs:
    data = doc.to_dict()
    fecha = formatear_fecha(data['fecha'])
    print(f"Documento: {doc.id} → {fecha}")

    # elige hasta donde migrar
    if re.match(r"^2025-04-12", fecha):
        break

    # Migrar el dato
    insertar(id_semana, data['temperatura'], data['humedad'], fecha)
    print(f"Insertado-> {fecha}")

    # Eliminar el documento de Firestore
    baseDatos.collection('Temperatura').document(doc.id).delete()
    print(f"Documento eliminado: {doc.id}")

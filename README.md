# Control de Mediciones - Invernadero

Este proyecto automatiza la gestión y migración de datos de temperatura y humedad de un invernadero. Permite migrar datos desde Firebase Firestore a una base de datos local SQLite y exportarlos a reportes de Excel organizados por semanas.

## Estructura del Proyecto

- **`scripts.py`**: Script principal de migración.
  - Conecta a Firebase Firestore.
  - Descarga documentos de la colección `Temperatura`.
  - Formatea las fechas y organiza los datos.
  - Inserta los datos en la base de datos local (`Invernadero.db`).
  - Elimina los documentos procesados de Firestore para mantener la base de datos en la nube limpia.
  
- **`generadorExcel.py`**: Generador de reportes.
  - Consulta la base de datos local (`Invernadero.db`).
  - Genera un archivo Excel (`mediciones_por_semana.xlsx`).
  - Crea una hoja por cada semana registrada con los datos de temperatura y humedad.

- **`models/Bd.py`**: Capa de acceso a datos.
  - Gestiona la conexión a SQLite.
  - Define el esquema de la base de datos (tablas `mediciones` y `semanas`).
  - Provee funciones para insertar y consultar datos.

- **`credentials/credenciales.json`**: (No incluido en el repositorio por seguridad) Archivo de credenciales de servicio de Firebase necesario para la autenticación.

## Requisitos

- Python 3.x
- Librerías listadas en `requirements.txt` (si existe) o instalar manualmente:
  - `firebase-admin`
  - `pandas`
  - `openpyxl`

## Instalación

1.  Clonar el repositorio.
2.  Crear y activar un entorno virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Asegurarse de tener las credenciales de Firebase en `credentials/credenciales.json`.
4.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### 1. Migración de Datos
Ejecutar el script para descargar datos de Firebase y guardarlos localmente:
```bash
python scripts.py
```
*Nota: El script tiene una fecha límite de migración configurada (actualmente `2025-04-12`).*

### 2. Generación de Reportes
Ejecutar el generador para crear el archivo Excel con los datos históricos:
```bash
python generadorExcel.py
```
El archivo `mediciones_por_semana.xlsx` se generará en el directorio raíz.

## Base de Datos Local
El proyecto utiliza SQLite (`Invernadero.db`) con dos tablas principales:
- `semanas`: Registro de semanas.
- `mediciones`: Registros individuales de temperatura y humedad vinculados a una semana.

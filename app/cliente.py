import os
from datetime import datetime

# Carpeta donde se guardan los archivos de clientes
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def normalizar_nombre(nombre):
    return nombre.strip().lower().replace(" ", "_")

def ruta_archivo_cliente(nombre):
    return os.path.join(DATA_DIR, f"{normalizar_nombre(nombre)}.txt")

def crear_cliente(nombre, tipo_servicio, descripcion):
    archivo = ruta_archivo_cliente(nombre)

    if os.path.exists(archivo):
        return f"El cliente '{nombre}' ya existe."

    with open(archivo, "w", encoding="utf-8") as f:
        f.write(f"Cliente: {nombre.strip()}\n")
        f.write(f"Fecha de registro: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("Servicios contratados:\n")
        f.write(f"- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {tipo_servicio}: {descripcion}\n")

    return f"Cliente '{nombre}' creado correctamente."

def modificar_cliente(nombre, nuevo_servicio, descripcion):
    archivo = ruta_archivo_cliente(nombre)

    if not os.path.exists(archivo):
        return f"El cliente '{nombre}' no existe."

    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {nuevo_servicio}: {descripcion}\n")

    return f"Servicio agregado al cliente '{nombre}'."

def consultar_cliente(nombre):
    archivo = ruta_archivo_cliente(nombre)

    if not os.path.exists(archivo):
        return f"El cliente '{nombre}' no existe."

    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

def listar_clientes():
    archivos = [f for f in os.listdir(DATA_DIR) if f.endswith('.txt')]
    if not archivos:
        return "No hay clientes registrados aún."
    clientes = [f.replace('.txt', '') for f in archivos]
    return "\n".join(f"- {c}" for c in sorted(clientes))

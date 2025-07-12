import sys
from cliente import crear_cliente, modificar_cliente, consultar_cliente, listar_clientes

def mostrar_ayuda():
    print("""
Uso:
  python app/main.py comando [argumentos]
Comandos disponibles:
  crear        "Nombre Cliente" "Tipo Servicio" "Descripción"
  modificar    "Nombre Cliente" "Tipo Servicio" "Descripción"
  consultar    "Nombre Cliente"
  listar
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        mostrar_ayuda()
        sys.exit(1)

    comando = sys.argv[1].lower()

    if comando == "crear" and len(sys.argv) == 5:
        print(crear_cliente(sys.argv[2], sys.argv[3], sys.argv[4]))    elif comando == "modificar" and len(sys.argv) == 5:
        print(modificar_cliente(sys.argv[2], sys.argv[3], sy

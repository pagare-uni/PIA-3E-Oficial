import logging
import sho
import abu
import PasswordGen
import Portscan
import SysteminfoScript
from os import system
from colorama import init

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("main_script.log"),
        logging.StreamHandler()
    ]
)

def show_menu():
    print("\n")
    print("""\
    
    ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
    ████╗░████║██╔════╝████╗░██║██║░░░██║
    ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
    ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░

    ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░
    ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░
    ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
    ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
    ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝
          
    """)
    print("1. Módulo Shodan")
    print("2. Módulo IP Abuse Database")
    print("3. Módulo Generador de Contraseñas")
    print("4. Módulo Escaneo de Puertos")
    print("5. Módulo Información del Sistema")
    print("6. Salir")

def execute_module(option):
    if option == '1':
        logging.info("Usuario seleccionó el Módulo Shodan.")
        sho.main()  # Llama a la función main de sho.py
    elif option == '2':
        logging.info("Usuario seleccionó el Módulo IP Abuse Database.")
        abu.main()  # Llama a la función main de abu.py
    elif option == '3':
        logging.info("Usuario seleccionó Módulo Generador de Contraseñas.")
        PasswordGen.main()  # Llama a la función main de PasswordGen.py
    elif option == '4':
        logging.info("Usuario seleccionó Módulo Escaneo de Puertos.")
        Portscan.main()  # Llama a la función main de Portscan.py
    elif option == '5':
        logging.info("Usuario seleccionó Módulo Información del Sistema.")
        SysteminfoScript.main()  # Llama a la función main de SysteminfoScript.py
    elif option == '6':
        logging.info("Usuario decidió salir.")
        print("Saliendo...")
        return False
    else:
        logging.warning("Opción no válida seleccionada.")
        print("Opción no válida. Por favor, selecciona una opción del menú.")
    return True

def main():
    # Inicializar colorama para uso de colores en la salida
    init(autoreset=True)

    logging.info("Inicio del programa principal.")
    while True:
        system("cls")  # Limpiar la pantalla
        show_menu()
        option = input("Selecciona una opción: ")
        if not execute_module(option):
            break
    logging.info("Fin del programa principal.")

if __name__ == "__main__":
    main()

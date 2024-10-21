import shodan
import ipaddress
import logging
from os import system
from colorama import init, Fore

# Configuracion del loggin 
logging.basicConfig(
    level=logging.DEBUG,  # Nivel mínimo de mensajes que se registrarán
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato de los mensajes
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
    filename='shodan.log',  # Archivo donde se guardarán los logs
    filemode='a'  # Modo de escritura a para no sobreescribir 
)

# Función para validar el API Key
def validate_API_key(max_attempts=3):
    attempts = 0  # Contador de intentos

    while attempts < max_attempts:
        API_key = input("Ingresa un API Key válida para Shodan: ")
        
        try:
            # Inicializar el cliente de Shodan
            api = shodan.Shodan(API_key)
            
            # Intentar realizar una consulta simple para verificar si el API key es válido
            api.info()
            logging.info("API Key válida.")
            return api
        except shodan.APIError as e:
            logging.error(f"Error con el API Key: {e}")
            print("API Key inválida. Inténtalo de nuevo.")
            attempts += 1  # Incrementar el contador de intentos

    print("Has excedido el número máximo de intentos.")
    logging.error("Número máximo de intentos alcanzado para la clave API de Shodan.")
    print("Presione enter para continuar ")
    input()
    return None  # Devolver None si no se ingresó una clave válida

# Función para validar una dirección IP
def validate_IP(ip):
    try:
        # Usar el módulo ipaddress para verificar si es una IP válida
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Función para buscar dispositivos y recopilar información
def find_devices(api, consult):
    try:
        # Realizar la búsqueda en Shodan
        results = api.search(consult)
        logging.info(f'Resultados encontrados para "{consult}": {results["total"]}')

        # Recorrer los resultados y mostrar información clave
        for device in results['matches']:
            ip = device['ip_str']
            port = device['port']
            organization = device.get('org', 'Desconocido')
            operative_system = device.get('os', 'Desconocido')

            logging.info(f'IP: {ip}, Puerto: {port}, Organización: {organization}, Sistema Operativo: {operative_system}')
            print(f'IP: {ip}')
            print(f'Puerto: {port}')
            print(f'Organización: {organization}')
            print(f'Sistema Operativo: {operative_system}')
            print('-' * 50)
        print("Presione enter para continuar ")
        input()

    except shodan.APIError as e:
        logging.error(f'Error en la búsqueda: {e}')
        print("Presione enter para continuar ")
        input()

# Función para buscar vulnerabilidades en un dispositivo específico
def find_vulnerabilities(api, ip):
    try:
        # Obtener detalles del host en Shodan
        host = api.host(ip)

        logging.info(f'Información del dispositivo {ip}:')
        print(f'Información del dispositivo {ip}:')
        print(f'País: {host.get("country_name", "Desconocido")}')
        print(f'Sistema Operativo: {host.get("os", "Desconocido")}')
        print(f'Puertos Abiertos: {host["ports"]}')

        # Mostrar las vulnerabilidades encontradas
        if 'vulns' in host:
            logging.info('Vulnerabilidades encontradas:')
            print('Vulnerabilidades encontradas:')
            for vulnerability in host['vulns']:
                cve = vulnerability.split(':')[-1]
                logging.info(f'CVE: {cve}')
                print(f'CVE: {cve}')
        else:
            logging.info('No se encontraron vulnerabilidades.')
            print('No se encontraron vulnerabilidades.')
        print("Presione enter para continuar ")
        input()

    except shodan.APIError as e:
        logging.error(f'Error obteniendo detalles del host: {e}')
        print("Presione enter para continuar ")
        input()

# Función para mostrar el menú de consultas predefinidas
def select_consult():
    print("\n--- Selecciona una consulta ---")
    consults = ['apache', 'nginx', 'IIS', 'ftp', 'ssh']
    for i, consult in enumerate(consults, 1):
        print(f"{i}. {consult}")
    option = input("Selecciona una opción (1-5): ")

    # Validar que la opción ingresada sea correcta
    if option.isdigit() and 1 <= int(option) <= 5:
        return consults[int(option) - 1]
    else:
        logging.warning("Opción no válida en selección de consulta.")
        print("Opción no válida. Intenta de nuevo.")
        return select_consult()

# Función para mostrar el menú y ejecutar las funciones según la elección
def show_menu(api):
    while True:
        system("cls")  # Limpiar la pantalla
        print("""      
              
        ░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░███╗░░██╗
        ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗████╗░██║
        ╚█████╗░███████║██║░░██║██║░░██║███████║██╔██╗██║
        ░╚═══██╗██╔══██║██║░░██║██║░░██║██╔══██║██║╚████║
        ██████╔╝██║░░██║╚█████╔╝██████╔╝██║░░██║██║░╚███║
        ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝
              
        """)
        print("\n--- Menú de Shodan ---")
        print("1. Buscar dispositivos")
        print("2. Buscar vulnerabilidades en un dispositivo")
        print("3. Salir")
        option = input("Selecciona una opción: ")

        if option == '1':
            consult = select_consult()
            find_devices(api, consult)
        elif option == '2':
            ip = input("Ingresa la IP del dispositivo para buscar vulnerabilidades: ")
            
            # Validar la IP antes de proceder
            if validate_IP(ip):
                find_vulnerabilities(api, ip)
            else:
                logging.warning("IP no válida ingresada.")
                print("IP no válida. Por favor, ingresa una IP correcta.")
                print("Presione enter para continuar ")
                input()
        elif option == '3':
            logging.info("Salida del programa.")
            print("Saliendo...")
            break
        else:
            logging.warning("Opción no válida en el menú principal.")
            print("Opción no válida. Intenta de nuevo.")

# Programa principal
def main():
    # Inicializar colorama para uso de colores en la salida
    init(autoreset=True)

    # Llamar a validate_API_key en lugar de pedir API_key directamente
    api = validate_API_key()  # Validar la clave API sin necesidad de pasarla como argumento

    if api:
        # Mostrar el menú de opciones
        show_menu(api)
    else:
        logging.error("No se puede continuar sin un API Key válido.")
        print("No se puede continuar sin un API Key válido.")

# Ejecutar el programa principal si el script se llama directamente
if __name__ == "__main__":
    main()

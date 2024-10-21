import requests
import logging
from os import system
from colorama import init, Fore

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ip_abuse_module.log"),
        logging.StreamHandler()
    ]
)

# Función para solicitar la clave API
def validate_api_key(max_attempts=3):
    attempts = 0  # Contador de intentos

    while attempts < max_attempts:
        api_key = input("Ingresa un API Key válida: ")
        
        if len(api_key) == 80:  # Asumiendo que las API Keys son de 80 caracteres
            logging.info("Clave API válida ingresada.")
            return api_key
        else:
            logging.warning("Clave API inválida ingresada. Debe tener 80 caracteres.")
            print("Clave API inválida. Inténtalo de nuevo.")
            attempts += 1  # Incrementar el contador de intentos

    print("Has excedido el número máximo de intentos.")
    logging.error("Número máximo de intentos alcanzado para la clave API.")
    return None  # Devolver None si no se ingresó una clave válida

# URL base de la API de IP Abuse
URL = 'https://api.abuseipdb.com/api/v2/check'

# Función para buscar información de una IP
def search_ip_abuse(ip_address, api_key):
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'  # Tiempo en días para los reportes
    }

    # Realizar la solicitud a la API
    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()  # Lanza un error si la respuesta es 4xx o 5xx
        data = response.json()
        return data
    except requests.RequestException as e:
        logging.error(f"Error en la solicitud: {e}")
        print("Error al realizar la solicitud. Verifica la conexión y la clave API.")
        return None

# Procesar y mostrar la información
def show_ip_info(data):
    if data:
        print(f"Dirección IP: {data['data']['ipAddress']}")
        print(f"País: {data['data']['countryCode']}")
        print(f"Reportes totales: {data['data']['totalReports']}")
        print(f"Actividad abusiva: {data['data']['abuseConfidenceScore']}%")
        
        # Verificar si hay reportes disponibles
        if 'reports' in data['data'] and data['data']['reports']:
            # Mostrar los detalles de los reportes
            for report in data['data']['reports']:
                print(f"Fecha del reporte: {report['reportedAt']}")
                print(f"Comentario: {report['comment']}")
                print("-----")
        else:
            print("No hay reportes disponibles para esta IP.")
    else:
        print("No se pudo obtener información.")

# Función para ejecutar la búsqueda de IP
def main():
    # Inicializar colorama para uso de colores en la salida
    init(autoreset=True)

    API_key = validate_api_key()  # Solicitar la clave API al inicio de la función main
    if API_key is None:
        print("No se pudo obtener una clave API válida. Saliendo del módulo.")
        return  # Salir si no se obtuvo una clave válida

    while True:
        system("cls")  # Limpiar la pantalla
        print("""\
        
        ██╗██████╗░  ██████╗░░█████╗░████████╗░█████╗░
        ██║██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
        ██║██████╔╝  ██║░░██║███████║░░░██║░░░███████║
        ██║██╔═══╝░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
        ██║██║░░░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
        ╚═╝╚═╝░░░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

        ░█████╗░██████╗░██╗░░░██╗░██████╗███████╗
        ██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔════╝
        ███████║██████╦╝██║░░░██║╚█████╗░█████╗░░
        ██╔══██║██╔══██╗██║░░░██║░╚═══██╗██╔══╝░░
        ██║░░██║██████╦╝╚██████╔╝██████╔╝███████╗
        ╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═════╝░╚══════╝
              
        """)
        target = input("Ingresa la dirección IP que deseas consultar (o 'salir' para terminar): ")
        if target.lower() == 'salir':
            logging.info("El usuario ha decidido salir.")
            break
        info_ip = search_ip_abuse(target, API_key)  # Pasar la API key a la función
        show_ip_info(info_ip)

if __name__ == "__main__":
    main()

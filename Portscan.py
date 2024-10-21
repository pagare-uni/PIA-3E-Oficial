import socket #Modulo necesario para la revision de puertos 
import logging #Modulo para guardar un registro de lo que hace el script
import requests #Modulo necesario para obtener la ip publica 
import ipaddress # Este Modulo nos sirve para validar la IP

# Este modulo nos sera necesario para la ventana de seleccion de carpeta 
import tkinter as tk
# Modulos necesarios para limpiar la pantalla y revisar existencias 
import os 
from os import system

# Modulo para asignar colores a las impresiones de pantalla 
from colorama import init,Fore 

#Modulo necesario para manejar las ventanas emergentes 
from tkinter.filedialog import askdirectory


# Funcion simple que desplega el mennu 
def menu(): 
    logging.info("Imprimiendo menu")
    system("cls") #Limpiando pantalla

    print("""
    
    ███████╗░██████╗░█████╗░░█████╗░███╗░░██╗███████╗░█████╗░
    ██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗
    █████╗░░╚█████╗░██║░░╚═╝███████║██╔██╗██║█████╗░░██║░░██║
    ██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██║╚████║██╔══╝░░██║░░██║
    ███████╗██████╔╝╚█████╔╝██║░░██║██║░╚███║███████╗╚█████╔╝
    ╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░╚════╝░

    ██████╗░███████╗
    ██╔══██╗██╔════╝
    ██║░░██║█████╗░░
    ██║░░██║██╔══╝░░
    ██████╔╝███████╗
    ╚═════╝░╚══════╝

    ██████╗░██╗░░░██╗███████╗██████╗░████████╗░█████╗░░██████╗
    ██╔══██╗██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
    ██████╔╝██║░░░██║█████╗░░██████╔╝░░░██║░░░██║░░██║╚█████╗░
    ██╔═══╝░██║░░░██║██╔══╝░░██╔══██╗░░░██║░░░██║░░██║░╚═══██╗
    ██║░░░░░╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██████╔╝
    ╚═╝░░░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═════╝░

            """)
    print("Seleccione opcion")
    print("")
    print("1. Escaner de puertos")
    print("2. Salir")




    return


# Funcion que realiza el escaneo de puertos
def port_scan():
    system("cls") # Limpiar pantalla 
    while True: # Ciclo necesario para validacion de datos de entrada 
        logging.info("Imprimiendo menu de port_scan")
        try:
            #Se le pide al usuario seleccionar una opcion
            print("Seleccione la opcion de puertos a escanear \n")
            print("1-Escanear puertos de mi IP privada \n ")
            print("2-Escanear puertos de mi IP publica \n")
            print("3-Escanear puertos de IP personalizada \n")
            #Variable que almacena la opcion y revisa que sea entera 
            option=int(input())

            if option==1: # Esta opcion extrae la ip de la computadora
                ip=socket.gethostbyname(socket.gethostname())
                system("cls") #Limpiar pantalla
                logging.info("El usuario ingreso con IP privada") 
                break # Rompiendo el ciclo para acceder a la opcion siguiente

            elif option==2: # Esta opcion extrae la ip publica de una pagina
                try:
                    #Realizamos un request que nos devuelve nuestra ip publica
                    ip=requests.get('http://checkip.amazonaws.com')
                    if ip.status_code==200:
                        ip=requests.get('http://checkip.amazonaws.com').text.strip()
                        system("cls") #Limpiar pantalla 
                        logging.info("El usuario ingreso con IP publica")
                        break # Rompiendo el ciclo

                    else: # Opcion por si no se encontro la ip publica
                        print("No se puede obtener la ip publica")
                        logging.info("No se encontro ip publica")
                #Exepcion por si el request fallla
                except (requests.ConnectionError, requests.Timeout): 
                    system("cls")
                    print(Fore.RED+"ERROR NO SE PUDO OBTENER LA IP PUBLICA, REVISE SU CONEXION WIFI")
                    print("Presione enter para continuar ")
                    input()
                    logging.error("No se pudo realizar la solicitud ")
                    
            # En esta opcion el usuario ingresa la IP        
            elif option==3:
                try:
                    print("")
                    print("Ingrese la direccion IP")
                    ip=input()
                    # Revisando que la ip sea valida 
                    ipv = ipaddress.ip_address(ip) 
                    logging.info("El usuario ingreso con IP personalizada")
                    break   
                except ValueError: # Exepcion por si la ip no existe 
                    system("cls")
                    print("")
                    print(Fore.RED+ "Direccion IP invalida")
                    print("")
                    print("Presione enter para continuar ")
                    input()
                    system("cls")
                    logging.error("El usuario ingreso una IP invalida")
                    
            else: # Si se ingresa otro numero se repite el menu 
                port_scan()
                system("cls")
                logging.info("Reeimprimiendo menu")
        except ValueError: # Exepcion por si se ingresa otro dato
                system("cls")  
                print(Fore.RED+"Dato no valido")
                logging.error("Reeimprimiendo menu")

    logging.info(f"El usuario ingreso con la Ip: {ip}")
    logging.info("Iniciando funcion port_list()")

    #Se ejecuta la funcion port_list
    portlist=port_list() 

    # Asignamos las listas para guardar los puertos cerrados y abiertos
    closePort=[]
    openPort=[]

    system("cls") # Limpiamos pantalla 
    print("Ip : ",ip) #Imprimos la ip a la cual estamos haciendo el escaneo
    
    # Aqui ya iniciamos ahora si lo que es el escaneo de puertos 
    # El for nos permite escanear todos los puertos de la lista
    logging.info("Iniciando escaneo de puertos...")
    for port in portlist:  
        try: # Hacemos el escaneo de puertos 
            # Clase socket
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1) # Le asignamos el tiempo

            #Esta variable nos sirve para cuando marque una exepcion
            # Lo que va a significar que esta cerrado o no responde 
            result= sock.connect((ip,port))

            print("Puerto",port," Abierto")
            # Si responde agregamos el puerto a la lista 
            openPort.append(port)
            sock.close #Cerramos la conexion

        except (socket.timeout, socket.error): # Exepcion 
            print("Puerto: ",port," Cerrado")
            # Si no responde agregamos el puerto a la lista
            closePort.append(port)
            
        finally:
            sock.close()  # cerrando el socket por si hubo error
    logging.info("Finalizo el escaneo de puertos ")  
    logging.info(f"Puertos abiertos: {openPort}")     
    logging.info(f"Puertos cerrados: {closePort}")     

    # Imprimiendo leyenda
    print("")
    print(Fore.RED + "Recuerde que tener un puerto abierto no es necesariamente malo")
    print(Fore.RED + "Es importante entender el porque este esta abierto ")
    print("..........................................")
    print("Presione enter para continuar ")
    input() # Input para que el usuario pueda leer 

    #Desplegamos un mini menu en caso de que el usuario quiera hacer reporte
    while True: # Ciclo de validacion
        try:
            print("Desea realizar un reporte (y/n)")
            reporOption=str(input()) #Validamos que la opcion sea un string
            reporOption=reporOption.lower() # Lo hacemos minisculas 
            # Validamos si el usuario quiere mas signos de puntuacion
            if reporOption=="y":
                logging.info("El usuario quiso hacer un reporte")
                # Iniciamos la funcion que genera un reporte 
                genreport(closePort,openPort,ip)
                break # Finalizamos port_scan

            elif reporOption=="n":
                logging.info("El usuario no quiso hacer un reporte")
                system("cls")
                break # Finalizamos port_scan

            else:
                logging.error("El usuario ingreso un caracter invalido")
                print(Fore.RED+"Opcion invalida")

        except ValueError: # Exepcion
            print(Fore.RED+"La opción que ingreso es invalida")
            logging.error("El usuario ingreso un caracter invalido")
    
    return 0


# Funcion que asigna los puertos a escanear 
def port_list():
    while True:
        logging.info("Imprimiendo Menu de port_list")
        try:
            #Menu de la funcion
            print("Selecciona una opcion para los puertos a escanear \n")
            print("1-Escanear puertos mas comunes \n")
            print("2-Escanear puertos personalizados \n")

            #Validando que la opcion sea un int 
            Portsoption = int(input())

            # Opcion de los puertos mas comunes 
            if Portsoption == 1:
                portlist=[# Lista de puertos comunes abiertos
                20,  # FTP Data Transfer
                21,  # FTP Control
                22,  # SSH
                23,  # Telnet
                25,  # SMTP
                53,  # DNS
                67,  # DHCP Server
                68,  # DHCP Client
                80,  # HTTP
                110, # POP3
                143, # IMAP
                443, # HTTPS
                3389 # RDP
                ]
                logging.info("El usuario escogio los puertos comunes")
                break #Rompiendo ciclo

            #Opcion 2 donde el usuario elige los puertos
            elif Portsoption == 2:
                logging.info("El usuario escogio sus propios puertos")
                system("cls") #Lipiando panatalla
                print("Ingrese de que puerto a que puerto quiere escanear")
                while True: # Ciclo que valida los datos ingresados 
                    try:
                        print("Puerto inicial: ")
                        firstP = int(input()) #Validamos que sea un entero
                        
                    # Los dos siguientes if tienen la funcion de validar
                    # Que los puertos ingresados por el usuario sean correctos
                    # El primero puerto tiene que ser entre 0 y 65000
                    # Y el segundo entre el primero y menor o igual a 65000
                    # Esto con el fin de evitar errores con los puertos 
                                    
                        if firstP <0:
                            print(Fore.RED+"Numero invalido")
                            logging.info("El usuario ingreso un puerto negativo")
                            print("")
                        elif firstP >= 0 and firstP <= 65000: # La computadora tiene aproximadamente esa cantidad de puertos
                            logging.info(f"El usuario ingreso como puerto inicial: {firstP} ")
                            break
                        else:
                            logging.info("El usuario ingreso un puerto mayor a 65000")
                            print(Fore.RED+"Numero invalido")
                            print("")

                    except ValueError: # Exepcion por si el dato ingresado es invalido
                        print(Fore.RED+"La opción que ingreso es invalida")
                        logging.error("El usuario ingreso un caracter invalido")
                
                while True:
                    try:
                        print("Puerto final: ")
                        lastP = int(input()) # Validamos que sea tipo entero
                       
                        if lastP < firstP:
                            logging.info("El usuario ingreso un puerto final menor al inicial")
                            print(Fore.RED+"Numero invalido")
                            print("")
                        elif lastP >= firstP and firstP <= 65000: # La computadora tiene aproximadamente esa cantidad de puertos
                            lastP=lastP+1
                            logging.info(f"Puerto final : {lastP-1}")
                            break # Rompiendo el ciclo
                        else:
                            logging.info("El usuario ingreso un numero mayor a 65000")
                            print(Fore.RED+"Numero invalido")
                            print("")
                    except ValueError:
                        print(Fore.RED+"La opción que ingreso es invalida")
                        logging.error("El usuario ingreso un caracter invalido")
                # Asigamos el rango de los puertos 
                portlist=range(firstP,lastP)
                break #Rompemos ciclos 
                
            else:
                logging.info("El usuario no ingreso una opcion valida ")
                print(Fore.RED+"Numero invalido")
                       
        except ValueError: # Exepcion para validar dato de entrada
            logging.error("Se ingreso un dato invalido")
            system("cls") #Limpiar pantalla 

    
    return portlist #Retornamos la lista de puertos 


# Funcion para validar la ruta donde guardar el archivo
def directory():
    logging.info("Iniciando directory()")
    #Creamos una clase tk para el manejo de ventanas 

    raiz = tk.Tk()

    #Hacemos que la ventana que no nos importa se cierra 
    raiz.withdraw()

    # Hacemos que la ventanas se generen en primer plano
    raiz.attributes('-topmost', True)

    # Abrir un cuadro de diálogo para elegir una carpeta la 
    # cual se guarda en una variable 

    path = askdirectory(parent=raiz, title="Seleccione una carpeta")
    raiz.destroy() #Cerramos las ventanas 

    # Imprimir la ruta de la carpeta seleccionada
    
    print("Carpeta seleccionada:", path)
    return path


# Funcuin que genera el reporte 
def genreport(closePort,openPort,ip):
    try: # Exepciones para el manejo de archivo
        # Iniciamos la funcion directory
        pathtosave=directory()

        logging.info(f"El usuario selecciono la carpeta {pathtosave}")

        # Variables para el nombre del archivo
        base_filename = "Portscan"
        extension = ".txt"

        #Generamos la ruta completa del archivo
        full_path = os.path.join(pathtosave, base_filename + extension)

        # Si el archivo ya existe, modificar el nombre
        counter = 1
        while os.path.exists(full_path):
            full_path = os.path.join(pathtosave, f"{base_filename}({counter}){extension}")
            counter += 1
        # Aqui ya generamos el archivo y empezamos a guardar los datos , tales como
        # Ip , los puertos abiertos y los puertos cerrados 
        logging.info("Creando reporte ")

        file = open(full_path, "w") #Abrimos el archivo
        file.write(f"Escaneo de puertos de : {ip} \n")
        file.write("Puertos cerrados : \n")
        for x in closePort: # La lista de los puertos cerrados 
            file.write(str(x),)
            file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("Puertos abiertos : \n")
        for i in openPort: # La lista de los puertos abiertos 
            file.write(str(i))
            file.write("\n")
        file.close()# Cerramos el archivo

        logging.info("Reporte generado ")
        logging.info((f"Archivo guardado como: {base_filename}({counter})"))
        print(f"Archivo guardado como: {base_filename}({counter})")
        print("Presione enter para continuar ")
        input()
        system("cls") #Limpiando pantalla 
        
    except PermissionError: #Exepcion por si no se selecciona una carpeta 
        logging.info("El usuario no selecciono una carpeta")
        system("cls")
        print(Fore.RED+"ERROR NO SE ESCOGIO UNA CARPETA")
        print("Presione enter para continuar ")
        system("cls")
    return 0


# Esto permite que el color de las letras no se aplique a todos los prints
init(autoreset=True) 


# Configuracion del loggin 
logging.basicConfig(
    level=logging.DEBUG,  # Nivel mínimo de mensajes que se registrarán
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato de los mensajes
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
    filename='FBDC.log',  # Archivo donde se guardarán los logs
    filemode='a'  # Modo de escritura a para no sobreescribir 
)

def main():
    continue1 = True
    logging.info("Iniciando el script")

    # Ciclo que permite re-ejecutar el script las veces necesarias 
    while continue1:
        try:
            menu()
            option = int(input())
            # Opcion para el escaneo de puertos 
            if option == 1:
                logging.info("Se ingreso al escaneo de puertos")
                port_scan()
            # Opcion para salir 
            elif option == 2:
                continue1 = False
                logging.info("Saliendo...")
                break
            else:
                print("")
        # Exepcion por si el dato ingresado no es valido 
        except ValueError:
            logging.error("Se ingreso un dato invalido")
            print("")


# Verificamos si el script es ejecutado directamente
if __name__ == "__main__":
    main()

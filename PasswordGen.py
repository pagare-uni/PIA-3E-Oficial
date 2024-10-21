# Importamos los módulos necesarios

import string # Para acceder a los caracteres alfanumericos
import random # Aleatoriedad 
import secrets # Para generar números y caracteres más seguros
import logging #Guardar registros 
from os import system # En este script lo usamos simplente para limpiar la pantalla
from colorama import init,Fore # En este scrip lo usamos para cambiar el color de las impresiones 

# Funcion que valida la longuitd de la contraseña
def validate_args(number):
    logging.info("Iniciando función validate_args")

    # Un if para validar la longuitud de la contraseña 
    if number >= 6 and number < 20:
        print("")
        print("Creando contraseña...")

    # Si es menor a 6 se le asiganara este 
    elif number < 6:
        print("")
        print(Fore.RED + "Es recomendable una contraseña con mínimo 6 caracteres.")
        print(Fore.RED + "Por lo que la longuitd de su contraseña sera 6")       
        number=6
        print("Creando contraseña...") 
        
    # Si es mayor a 20 se le asiganara este    
    else:
        print("")
        print(Fore.RED +"El límite recomendado es de 20 caracteres ")
        number=20
        print("Creando contraseña...") 
                 
    return number

# Funcion que imprime el menu
def menu():
    logging.info("Imprimiendo menu")
    system("cls") #Limpiando pantalla

    print("""
    ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░██████╗░░█████╗░██████╗░  ██████╗░███████╗
    ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
    ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║██║░░██║██║░░██║██████╔╝  ██║░░██║█████╗░░
    ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔══██╗  ██║░░██║██╔══╝░░
    ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║██████╔╝╚█████╔╝██║░░██║  ██████╔╝███████╗
    ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝

    ░█████╗░░█████╗░███╗░░██╗████████╗██████╗░░█████╗░░██████╗███████╗███╗░░██╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░██║██╔══██╗██╔════╝
    ██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░██████╔╝███████║╚█████╗░█████╗░░██╔██╗██║███████║╚█████╗░
    ██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██╗██╔══██║░╚═══██╗██╔══╝░░██║╚████║██╔══██║░╚═══██╗
    ╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║██║░░██║██████╔╝███████╗██║░╚███║██║░░██║██████╔╝
    ░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░
            """)
    print("Seleccione opcion")
    print("")
    print("1. Generar contraseña")
    print("2. Salir")




    return

# Funcion para crear la contraseña
def pasww():
    logging.info("Iniciando funcion pasww()")
    # Limpiamos la terminal e imprimimos unas indicaciones breves 
    system("cls")
    print(text)

    logging.info("Pidiendo longuitd de contraseña")
    # Validamos que el dato ingresado sea un entero
    while True:
        try:
            
            number= int(input("Ingrese un número: "))
            long=validate_args(number)
            
            break
        # Exepcion por si el dato ingresado no es valido
        except ValueError:
            print("La opción que ingreso no es un numero")
            logging.error("El usuario ingreso un caracter invalido")

    logging.info(f"Longuitud de contraseña : {long}")
    
    
   #
    print("")
    print("")
    # Definimos el conjunto de caracteres que se pueden usar en la contraseña
    while True:
        try:
            Puntopt=print("¿Desea que su contraseña pueda tener mas de 1 signo de puntuacion? (Y/N)")
            Puntopt=str(input())
            Puntopt=Puntopt.lower()
            # Validamos si el usuario quiere mas signos de puntuacion
            if Puntopt=="y":
                characters = string.ascii_letters + string.digits + string.punctuation
                logging.info("El usuario quiso mas signos de puntuacion")
                break
            elif Puntopt=="n":
                characters = string.ascii_letters + string.digits
                logging.info("El usuario no quiso mas signos de puntuacion")
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("La opción que ingreso es invalida")
            logging.error("El usuario ingreso un caracter invalido")

    logging.info("Generando contraseña")
    # Creamos una lista vacía para almacenar los caracteres de la contraseña
    password = []

    # Añadimos al menos un carácter de cada tipo a la contraseña
    password.append(random.choice(string.ascii_lowercase)) # Añadimos una minúscula
    password.append(random.choice(string.ascii_uppercase)) # Añadimos una mayúscula
    password.append(random.choice(string.digits)) # Añadimos un número
    password.append(random.choice(string.punctuation)) # Añadimos un carácter de puntuacion

    # Completamos la contraseña con caracteres aleatorios hasta alcanzar la longitud ingresada
    while len(password) < long:
        password.append(secrets.choice(characters)) # Usamos secrets para mayor seguridad

    # Revolvemos los caracteres para mas aleatoridad 
    random.shuffle(password)

    # Convertimos la lista en un solo string
    password = "".join(password)

    # Imprimimos la contraseña generada
    print("Tu contraseña es:",Fore.RED + password)
    logging.info(f"Contraseña generada : {password}")
    print("Presione enter para continuar ....")
    input()
    system("cls")
    return 0

# Configuracion del loggin 
logging.basicConfig(
    level=logging.DEBUG,  # Nivel mínimo de mensajes que se registrarán
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato de los mensajes
    datefmt='%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
    filename='PasswordGen.log',  # Archivo donde se guardarán los logs
    filemode='a'  # Modo de escritura a para no sobreescribir 
)

# Esto permite que el color de las letras no se aplique a todos los prints
init(autoreset=True) 

# Texto que servira de referencia para la longuitud de contraseña 
text=Fore.RED +"""
El dato a ingresar debe ser la longuitd que quieres que tenga la contraseña (mas de 5), puede ser :
6 a 7 - Contraseña debil 
8 a 12 - Buena contraseña
12 a 20 - Contraseña muy segura 
"""

def main():
    # Variable continue1 para el ciclo
    continue1 = True
    logging.info("Iniciando el script")

    # Ciclo que permite re-ejecutar el script las veces necesarias
    while continue1:
        try:
            while continue1:
                menu()
                option = int(input())

                if option == 1:
                    pasww()
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

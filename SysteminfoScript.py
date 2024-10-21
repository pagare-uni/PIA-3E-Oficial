import logging
import psutil
from os import system
from colorama import init,Fore # En este scrip lo usamos para cambiar el color de las impresiones 

# Funcion que imprime el menu
def menu():
    logging.info("Imprimiendo menu")
    system("cls") # Limpiando pantalla 
    print("""
      
    ██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░░█████╗░██╗░█████╗░███╗░░██╗
    ██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
    ██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║██║░░╚═╝██║██║░░██║██╔██╗██║
    ██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║██║░░██╗██║██║░░██║██║╚████║
    ██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║╚█████╔╝██║╚█████╔╝██║░╚███║
    ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝

    ██████╗░░█████╗░░██████╗██╗░█████╗░░█████╗░  ██████╗░███████╗██╗░░░░░
    ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔══██╗  ██╔══██╗██╔════╝██║░░░░░
    ██████╦╝███████║╚█████╗░██║██║░░╚═╝███████║  ██║░░██║█████╗░░██║░░░░░
    ██╔══██╗██╔══██║░╚═══██╗██║██║░░██╗██╔══██║  ██║░░██║██╔══╝░░██║░░░░░
    ██████╦╝██║░░██║██████╔╝██║╚█████╔╝██║░░██║  ██████╔╝███████╗███████╗
    ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝╚══════╝

    ░██████╗██╗░██████╗████████╗███████╗███╗░░░███╗░█████╗░
    ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔══██╗
    ╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔████╔██║███████║
    ░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║
    ██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██║░░██║
    ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝

    """)
    print("")
    print("")
    print("")
    print("1. Ver Informacion de la RAM")
    print("2. Ver Informacion del disco")
    print("3. Ver informacion del CPU")
    print("4. Salir")

# Funcion sobre informacion de la memoria RAM
def memory():
    system("cls") #Limpiamos pantalla 
    processlist = []
    logging.info("Calculando procesos")
    # Iterar sobre todos los procesos del sistema 
    for process in psutil.process_iter(['name', 'memory_info']):
        try:
            # Añadir a la lista de procesos con su nombre y consumo de memoria
            processlist.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error accediendo al proceso: {e}")

            pass
    
    # Ordenar los procesos por uso de memoria y con el reverse los ordenamos de mayor a menor

    processlist = sorted(processlist, key=lambda p: p['memory_info'].rss,reverse=True)

    # Revisamos la memoria total de la computadora 
    # La multiplicacion es para tener el resultado en Gigabytes

    percent_memory=psutil.virtual_memory().percent # Porecentaje de memoria usado
    avememory=psutil.virtual_memory().available/(1024*1024*1024) # Disponible
    used_memory=psutil.virtual_memory().used/(1024*1024*1024) # Usada
    free_memory=psutil.virtual_memory().free/(1024*1024*1024) # Libre
   
    # Redondeamos a 2 decimales
    percent_memory=round(percent_memory,2)
    avememory=round(avememory,2)
    free_memory=round(free_memory,2)
    used_memory=round(used_memory,2)
    
    #Calculamos la memoria Total y redondeamos
    total_memory = psutil.virtual_memory().total
    total_memory = total_memory /(1024*1024*1024)
    total_memory = round(total_memory,2)
    
    logging.info("Calculando uso de Memoria RAM")

    print("Datos sobre la ram")
    print("")
    print(f"Total de memoria RAM: {total_memory} GB")
    print(f"Uso de la memoria RAM: {percent_memory}%")
    print(f"Memoria disponible: {avememory} GB")
    print(f"Memoria en uso: {used_memory} GB")
    print(f"Memoria libre: {free_memory} GB")
    print("")

    logging.info(f"Total: {total_memory}")
    logging.info(f"Porcentaje: {percent_memory}")
    logging.info(f"Disponble: {avememory}")
    logging.info(f"En uso: {used_memory}")
    logging.info(f"Libre: {free_memory}")

    logging.info("Preguntando al usuario si quiere ver los procesos que mas consumen")
    while True:
        
        try:
            
            print("¿Desea ver los procesos que mas RAM consumen? (y/n)")
            # Validamos el dato 
            option=str(input())
            option=option.lower()

            # Imprimir los 10 procesos que más memoria consumen
            x=0
            if option=="y": # Si acepta empezara el proceso
                logging.info("El usuario acepto")
                for process in processlist[:10]:
                    x=x+1 #Contador 
                    process_ram = process['memory_info'].rss / (1024 * 1024)  # Convertir de bytes a MB
                    percent_ram_process = ((process_ram/1024) / (total_memory )) * 100 #Porcentaje 

                    #Redondeando
                    process_ram = round(process_ram,2)
                    percent_ram_process = round(percent_ram_process,2)

                    print(f"{x}-Nombre del proceso : {process['name']}")
                    print(f"Ram utilizada : {process_ram} MB")
                    print(f"Porcentaje :{percent_ram_process} %")
                    print("")
                print(Fore.RED+"Presione enter para continuar")
                input()
                logging.info("Se imprimieron los procesos")
                break
            elif option=="n":
                logging.info("EL usuario no quiso ver los procesos")
                break
            else:
                print(Fore.RED+"Dato invalido")
                logging.error("Se ingreso un dato invalido")
        except ValueError:
            logging.error("EL usuario ingreso un dato invalido")
            print("Dato invalido")
    return 0

#Funcion para ver informacion del disco
def disk():
    system("cls") #Limpiamos pantalla
    logging.info("Recopilando informacion del disco")
    print("Informacion del disco: ")

    # Extraemos la cantidad de partocopmes 
    disk= psutil.disk_partitions()

    for partition in disk:
        try:
            # Leemos cada particion del disco
            
            disk_usaged = psutil.disk_usage(partition.mountpoint)
            print(f"Partición: {partition.device}")
            print("")
            #Imprimimos punto de montaje , sistema de archivos
            # Espacio total , usado y libre y el porcentaje 
            print(f"  Punto de montaje: {partition.mountpoint}")
            print(f"  Tipo de sistema de archivos: {partition.fstype}")
            print(f"  Espacio total: {disk_usaged.total / (1024**3):.2f} GB")
            print(f"  Espacio usado: {disk_usaged.used / (1024**3):.2f} GB")
            print(f"  Espacio libre: {disk_usaged.free / (1024**3):.2f} GB")
            print(f"  Porcentaje de uso: {disk_usaged.percent}%\n")
            print("")
            print("")

            logging.info(f"PM:{partition.mountpoint}")
            logging.info(f"TSA:{partition.fstype}")
            logging.info(f"EspT:{disk_usaged.total}")
            logging.info(f"EspU{disk_usaged.used}")
            logging.info(f"EspLi{disk_usaged.free}")
            logging.info(f"EspLi{disk_usaged.free}")
            logging.info(f"%{disk_usaged.percent}")

        except PermissionError: #Exepcion
            logging.error("NO SE PUDO LEER EL DISCO")
            print(Fore.RED+"ERROR AL LEER DISCO")
    logging.info("Preguntando al usuario si quiere ver procesos que mas consumen")
    while True:
        try:
            print("¿Desea ver los procesos que mas disco consumen? (y/n)")
            #Validando el dato
            option=str(input())
            option=option.lower()

            # Imprimir los 10 procesos que más memoria consumen
            x=0
            if option=="y":

                logging.info("El usuario acepto")

                # Leyenda informativa
                important_text="""
Se mostrara la cantidad de operaciones de lectura y escritura realizadas
por cada proceso en disco 
(es decir, la cantidad de datos leídos y escritos). Esto refleja el uso de I/O del disco de 
los procesos, no el espacio que ocupan en el almacenamiento.
                """

                print(Fore.RED+important_text)
                # Lista para guardar los procesos
                disk_process = []

                # Calculando todos los procesos
                for process in psutil.process_iter(['name', 'io_counters']):
                    try:
                        io_counters = process.info['io_counters']
                        if io_counters:
                            # Guardamos el proceso y el total de bytes leídos/escritos
                            total_io = io_counters.read_bytes + io_counters.write_bytes
                            disk_process.append((process.info['name'], total_io))
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  
                        pass

                # Ordenar los procesos por el total de bytes leídos/escritos de mayor a menor
                disk_process.sort(key=lambda x: x[1], reverse=True)

                #Contador
                i=0

                #Imprimimos los procesos con su nombre y cantidad
                for name, io in disk_process[:10]:
                    i=i+1
                    print(f"{i}-Proceso: {name} ")
                    print(f"Uso: {io/(1024**3):.2f} GB")
                logging.info("Se imprimieron los procesos ")
                break         
            elif option=="n":
                logging.info("El usuario no quiso ver los procesos ")
                break
            else:
                print(Fore.RED+"Dato invalido")
                logging.error("Se ingreso un dato invalido")
        except ValueError:
            logging.info("El usuario ingreso un dato invalido")
            print("Dato invalido")
    print("")
    print(Fore.RED+"Presione enter para continuar ")
    input()
    return 0

#Funcion para ver informacion de la CPU
def cpu_info():
    system("cls") #Limpiamos pantalla
    logging.info("Analizando informacion de la CPU")
    try:
        # Obtener información del CPU
        frecuency = psutil.cpu_freq()  # Frecuencia del CPU
        total_cpu = psutil.cpu_percent(interval=1)  # Uso total del CPU
        cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)  # Uso del CPU por núcleo
        fisic_cores = psutil.cpu_count(logical=False)  # Núcleos físicos
        total_cores = psutil.cpu_count(logical=True)  # Núcleos totales (lógicos)

        
        print(f"Frecuencia máxima del CPU: {frecuency.max:.2f} MHz")
        print(f"Frecuencia actual del CPU: {frecuency.current:.2f} MHz")
        print(f"Número de núcleos físicos: {fisic_cores}")
        print(f"Número de núcleos lógicos: {total_cores}")
        print(f"Uso total del CPU: {total_cpu}%")

        logging.info(f"Frecuencia máxima del CPU: {frecuency.max:.2f} MHz")
        logging.info(f"Frecuencia actual del CPU: {frecuency.current:.2f} MHz")
        logging.info(f"Número de núcleos físicos: {fisic_cores}")
        logging.info(f"Número de núcleos lógicos: {total_cores}")
        logging.info(f"Uso total del CPU: {total_cpu}%")

        logging.info("Se imprimio el uso por nucleo")
        # Mostrar el uso de CPU por núcleo
        for i, porcentaje in enumerate(cpu_per_core):
            print(f"Núcleo {i}: {porcentaje}%")

        # Obtener estadísticas adicionales del CPU
        statsCPU = psutil.cpu_stats()
        logging.info("Se mostro informacion adicional")

        print(f"\nEstadísticas del CPU:")
        # Numero de context switches desde el boot
        print(f"Context Switches: {statsCPU.ctx_switches}")
        # Numero de interrumpciones desde el boot
        print(f"Interrupciones: {statsCPU.interrupts}") 
        # Numero de llamadas al sistema desde el boot
        print(f"Llamadas al sistema: {statsCPU.syscalls}")
        # Numero de interrumpciones de software desde el boot
        print(f"Interrumpciones de software: {statsCPU.soft_interrupts}")
        print("\n \n")
        print(Fore.RED+"Presione enter para continuar")
        input()
    except PermissionError:
        logging.error("NO SE PUDO EXTRAER LA INFORMACION")
        print("NO SE PUDO EXTRAER LA INFORMACION")
    return 0

def main():
    # Configuracion del loggin
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='SysteminfoScript.log',
        filemode='a'
    )

    continue1 = True
    logging.info("Iniciando el script")

    # Inicializar colorama para uso de colores en la salida
    init(autoreset=True)

    # Ciclo para repetir el menú
    while continue1:
        try:
            menu()
            option = int(input())
            # Opcion para la informacion de la RAM 
            if option == 1:
                logging.info("Se ingreso a informacion de la RAM")
                memory()
            # Opcion para la informacion del disco duro 
            elif option == 2:
                logging.info("Se ingreso a informacion del disco")
                disk()
            # Opcion para la informacion de la CPU
            elif option == 3:
                logging.info("Se ingreso a informacion de la CPU")
                cpu_info()
            # Opcion para salir
            elif option == 4:
                continue1 = False
                logging.info("Saliendo...")
            else:
                print(Fore.RED + "Opción no válida. Inténtalo de nuevo.")
        except ValueError:
            logging.error("Se ingreso un dato invalido")
            print(Fore.RED + "Entrada no válida. Por favor, ingresa un número.")

if __name__ == "__main__":
    main()

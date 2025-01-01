import logging
import os
import datetime

def set_logger():
    # Crear un logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Establecer el nivel de log para el logger

    # Crear un handler para mostrar los logs en la consola (StreamHandler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Establecer el nivel de log para la consola

    directory1 = "logs"

    if not os.path.exists(f"./{directory1}"):
        print(f"./{directory1} no existe, creándolo.")
        os.mkdir(path=f"./{directory1}")
        print(f"./{directory1} Creado.")


    # Crear un handler para guardar los logs en un archivo (FileHandler)
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d-%H-%M-%S")
    ruta = now + "--bruna_log.log"
    file_handler = logging.FileHandler(f"./{directory1}" + os.sep + f"{ruta}")
    file_handler.setLevel(logging.DEBUG)  # Establecer el nivel de log para el archivo

    # Crear un formato para los logs
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Asignar el formato a ambos handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Añadir los handlers al logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("------------")
    logger.info("\n\tBruno")
    logger.info("------------")
    logger.info("Log Seteado- Inicia Bruno Execution")

    # Ejemplo de logs
    return logger

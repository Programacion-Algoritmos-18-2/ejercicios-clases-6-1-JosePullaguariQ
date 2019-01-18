import codecs
import sys

class MiArchivo:#Creamos la clase Miarchivo
    """
    """
    def __init__(self):#Constructor de la clase
        """
        """
        self.archivo = codecs.open("data/datos.txt", "r")#Direccion del archivo que vamos a utilizar y lo leemos con la letra "r"

    def obtener_informacion(self):#Metodo para leer la informacion del archivo
        return self.archivo.readlines()

    def cerrar_archivo(self):#Metodo para cerrar el archivo
        self.archivo.close()

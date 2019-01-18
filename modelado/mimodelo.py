class Operaciones:#Creamos la clase Operaciones
    def __init__(self, listado):#Contructor de la clase Operaciones que recibe el listado ordenado
        self.listaOrden = listado

    def busquedaBinaria(self, elemento):#Metodo de para realizaruna Busqueda Binaria
        elemBusq = elemento                                             #Asignamos a elemBusq el elemento recibido
        inferior = 0                                                    #Declaramos variable inferior inicializada en 0
        superior = len(self.listaOrden) -1                              #Declaramos variable superior con el tamaño del listado
        medio = int((inferior + superior + 1)/ 2)                       #Declaramos variable medio y le enviamos un valor transformado en entero
        ubicacion = -1                                                  #Declaramos variable ubicacion inicializada en -1

        while((inferior <= superior) and (ubicacion == -1)):            #Creamos un ciclo while para realizar la busqueda
            if (elemBusq == self.listaOrden[medio]):                    #Preguntamos si el elemento se encuentra en medio                    
                ubicacion = medio                                       #La ubicacion toma el valor de medio actual
            elif(elemBusq < self.listaOrden[medio]):                    #Sino preguntamos si el elemento es menor al elemento que esta en la posicion medio
                superior = medio - 1                                    #Eliminamos la mitad superior
            else:                                                       #Si no significa que es mayor al elemento que esta en la posicion medio
                inferior = medio + 1                                    #Eliminamos la mitad inferior   
            medio = int((inferior + superior + 1) / 2)                  #Recalculamos el medio con lo que no se elimino

        return ubicacion                                                #Retornamos la ubicacin que es la posicion donde se encuantra el elemento buscado
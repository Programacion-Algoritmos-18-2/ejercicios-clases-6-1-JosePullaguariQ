#Importamos todas la clases que vamos a utilizar
from paquete_archivos.miarchivo import *
from modelado.mimodelo import *

objLeer = MiArchivo()									#Creamos un objeto tipo MiArchivo para leer el archivo

lista = objLeer.obtener_informacion()					#Declaramos una lista para alamacenar la informacion del objeto objLeer
lista = [l.split(",") for l in lista]					#Separamos con el split los datos de la lista con el caracter ",""

listaOrden = []											#Creamos una lista vacia 
for n in lista:											#Creamos un for para recorrer la lista
	for valor in n:										#Creamos un for interno
		listaOrden.append(int(valor))					#Agregamos a la listaOrden los valores convertidos en cadena a enteros

listaOrden.sort()										#Utilizamos el .sort() para ordenar toda la listaOrden
print("\nLista Ordenada")
print(listaOrden)										#Presentamos la lista ordenada

operacion = Operaciones(listaOrden)						#Creamos un objeto tipo Operaciones
elem = int(input("\nIngrese el numero a buscar\n"))		#Pedimos que ingrese el elemento a buscar y lo transformamos a entero
respuesta = (operacion.busquedaBinaria(elem))			#Almacenamos en respuesta la posicion que devuelve el metodo busquedaBinaria

if (operacion.busquedaBinaria(elem) != -1):							#Si lo encuentra al elemento, es decir diferente de -1
	print("La posicion del elemento %d es: %d"%(elem, respuesta))	#Presentamos el elemento ingresado y su posicion
else:																#Si no lo encuentra al elemento
	print("El elemento: %d no existe"%elem)							#Presentamos que no existe dicho elemento

objLeer.cerrar_archivo()								#Cerramos el archivo para leer
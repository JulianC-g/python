import psycopg2
import Utilidades
import Proyecto_y_user_stories
from conexion import dc

is_connection=True

try:
     conexion=psycopg2.connect(**dc)
     Cursor = conexion.cursor()

except :
    print("No se pudo conectar a la base de datos")
    is_connection=False
    input("\n"+"Pulse una tecla para Salir")
    exit()


Validacion = []

def consultar():

    global Validacion

    if is_connection==True:

        Cursor.execute('select * from Proyectos ')

        filas= Cursor.fetchall()

        for fila in filas:
            id=fila[0]
            Validacion.append(id) 
            nombre= fila[1]
            descripcion=fila[2]
            print(f'[{id}] {nombre} \n')
            print(f'Descripcion:{descripcion}'+"\n")

        

def seleccionar_proyecto():

    global Validacion

    consultar()

    Opcion = int(input("Digite el numero del proyecto que desea ver: "))

    Valor_Verificacion= Opcion in Validacion

    if Valor_Verificacion == True:
        Proyecto_y_user_stories.Ejecutar_Seleccion(Opcion)
        Proyecto_y_user_stories.Opciones_UStories()
    
    else:
        print("\n"+"El valor seleccionado no existe, vuelva a intentarlo"+"\n")
        seleccionar_proyecto()


seleccionar_proyecto()




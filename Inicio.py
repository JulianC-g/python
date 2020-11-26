import crearproyecto
import ver_proyecto
import eliminar_proyecto
import Utilidades

# Menu Proyectos

Menu = (
    "------Menu Scrum------"+"\n"
    "1) Crear Proyecto"+"\n"
    "2) Ver Proyecto"+"\n"
    "3) Eliminar Proyecto"
    "4) Salir"+"\n"
    )

print(Menu)

# Seleccionar Opcion

def Seleccion ():

    Opcion = int(input("cual opcion desea escoger: "))

    if Opcion == 1:

        Utilidades.clear()
        crearproyecto.correr_inicio()
        Utilidades.clear()
        print(Menu)
        Seleccion()  
        
    elif Opcion == 2:
        Utilidades.clear()
        ver_proyecto.seleccionar_proyecto()
        Utilidades.clear()
        print(Menu)
        Seleccion()  
    
    elif Opcion == 3:
        Utilidades.clear()
        ver_proyecto.consultar()
        Opcion = int(input("cual opcion desea escoger: "))
        eliminar_proyecto.eliminar(Opcion)
        Utilidades.clear()
        print(Menu)
        Seleccion()
        


    elif Opcion == 4:
        exit()

    else:
        print("Opcion incorrecta"+"\n")
        Seleccion()


Seleccion()


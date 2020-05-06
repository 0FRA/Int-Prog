import os
def continuar():
        input("\nPresione ENTER para continuar...")
        return os.system('cls')
def cambiar_color(color):
    color = color.lower()
    if color == 'rojo':
        os.system('color 40')
        estado = "El color se ha cambiado a Rojo"    
    elif color == 'verde':
        estado = "El color se ha cambiado a Verde"    
        os.system('color 2')
    elif color == 'azul':
        os.system('color 1')
        estado = "El color se ha cambiado a Azul"    
    else:
        return "ERROR: Color inválido."
    return estado

def main():
    os.system('title Datos personales && color 2')
    apellido = "INDEFINIDO"
    nombre   = "INDEFINIDO"
    email    = "INDEFINIDO"
    color    = "DEFAULT"
    salir = False
    while not (salir):
        print("************ DATOS PERSONALES ************\n1. Mostrar datos actuales.\n2. Actualizar nombre.\n3. Actualizar apellido.\n4. Actualizar correo electrónico.\n5. Cambiar color del menu\n6. Salir.")
        op = input("\nSeleccione una opción  [1-6]: ")
        if op == '1':
            os.system('cls')
            print('----- Datos actuales -----')
            print("\nNombre: ", nombre,"\nApellido: ", apellido, "\nE-Mail: ", email,"\nColor:", color)
            continuar()

        elif op == '2':
            os.system('cls')
            print("--- Actualización de datos personales ---")
            nombre = input("\n  Ingrese su nombre: ")
            if len(nombre) > 0:
                print(f"\nHas actualizado tu nombre a {nombre}! ")
            else:
                nombre = "INDEFINIDO"
                print("\nNo has ingresado ningún nombre. Su nombre pasa a ser INDEFINIDO.")
            continuar()

        elif op == '3':
            os.system('cls')
            print("-- Actualización de datos personales ---")
            apellido = input("\n  Ingrese su apellido: ")
            if len(apellido) > 0:
                print(f"\nHas actualizado tu apellido a {apellido}! ")
            else:
                apellido = "INDEFINIDO"
                print("\nNo has ingresado ningún apellido. Su apellido pasa a ser INDEFINIDO.")
            continuar()

        elif op == '4':
            valido = False
            while not (valido):
                os.system('cls')
                print("-- Actualización de datos personales ---")
                email = input("\n  Ingrese su dirección de correo electrónico: ")
                if "@" and "." in email:
                    print(f"\nHas actualizado su dirección de correo electrónico a {email}! ")
                    valido = True
                elif len(email) > 0:
                    print(f'\nERROR: "{email}" no es una dirección de correo electrónico válido.')
                else:
                    print("ERROR: No has ingresado ningún E-Mail.")
                continuar()

        elif op == '5':
                os.system('cls')
                print("---- Cambiar colores del menu ----")
                color = input("Ingrese un color [Rojo, Verde, Azul]: ")
                cambiar_color(color)
                continuar()

        elif op == '6':
            salir = True

        elif op == '':
            print('ERROR: No has ingresado ninguna opción.')
            continuar()
        else:
            print(f'ERROR: la opción "{op}" no existe. Por favor, ingrese una opción válida [1-6]')
            continuar()
#main()


'''
Se necesita un programa para realizar una comparación de la nota promedio
entre dos comisiones de la asignatura Introducción a la Programación. Para
esto, se le debe pedir al usuario que cargue una a una todas las notas de la
primera comisión, y una vez finalizadas, cargar una a una las de la segunda
comisión.
El programa debe informar en pantalla el promedio de cada comisión, y cuál de
las dos es la comisión con mayor promedio. Tenga en cuenta que no se conoce
de antemano la cantidad de alumnos de cada comisión, y las comisiones
pueden tener cantidades diferentes de alumnos.
Para indicar que ha terminado de cargar las notas de una comisión, el usuario
debe ingresar el valor -1. Si al ingresar una nota, la misma no es válida (es decir,
no está entre 1 y 10, y tampoco es -1), se le debe informar del error, y luego
continuar con la carga de notas normalmente, pero sin contabilizar la nota
inválida.
'''
def promedio(comision_notas, cantidad_notas):
    if cantidad_notas > 0:
        return comision_notas / cantidad_notas
    else:
        return 0

def int_pro():

    # Inicializamos contadores en cero.
    com1_notas = 0
    com2_notas = 0
    com1_cant_notas = 0
    com2_cant_notas = 0

    # For que se repite solo dos veces, porque la cantidad de comisiones son dos.
    for comision in [1,2]:
        seguir = True
        print(f"--- Notas de la materia Int. a la Programación. [COMISIÓN {comision}] --- ")
        print (f'Para dejar apuntar notas de la comision {comision}, ingrese "-1".')
        while (seguir):
            nota = input(f"Ingrese nota de la comisión {comision}: ")
            if nota.isdigit() and (10 >= int(nota) > 0):
                nota = int(nota)
                if comision == 1:
                    com1_notas +=  nota
                    com1_cant_notas += 1
                    
                elif comision == 2:
                    com2_notas +=  nota 
                    com2_cant_notas += 1            
            elif nota == "-1":
                seguir = False
            else:
                print("Nota inválida. La nota debe ser un número entre 1 y 10.")


    print("El promedio de la comisión 1 es: ", promedio(com1_notas, com1_cant_notas))
    print("El promedio de la comisión 2 es: ", promedio(com2_notas, com2_cant_notas))

int_pro()
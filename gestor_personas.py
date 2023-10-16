def listar_personas():
    nombres = open('nombre.txt','r').read().splitlines()
    apellidos = open('apellido.txt','r').read().splitlines()
    dnis = open('dni.txt','r').read().splitlines()

    for i in range(len(nombres)):
        print(nombres[i] + "    \t" + apellidos[i] + "    \t" + dnis[i])

def agregar_personas():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = input("Ingrese su dni: ")

    nombre_txt = open('nombre.txt','a')
    nombre_txt.write("\n" + nombre)
    nombre_txt.close()

    apellido_txt = open('apellido.txt','a')
    apellido_txt.write("\n" + apellido )
    apellido_txt.close()

    dni_txt = open('dni.txt','a')
    dni_txt.write("\n" + dni)
    dni_txt.close()

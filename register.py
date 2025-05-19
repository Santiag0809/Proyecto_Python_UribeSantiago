import json
file_path="Data/content.json"

def leer_data():
    with open (file_path,"r") as file:
        return json.load(file)
    
def guardar_data(listar_datos):
    with open (file_path,"w") as file:
        return json.dump(listar_datos,file,indent=4)

def registrar_usuario():
    datos = leer_data()

    if "usuarios" not in datos:
        datos["usuarios"] = []

    email = input("Ingrese su email: ")
    if usuario_existente(email):
        print("El usuario ya existe.")
        return None

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    password = input("Ingrese su contraseña: ")

    nuevo_usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "password": password,
        "gastos": []
    }

    datos["usuarios"].append(nuevo_usuario)
    guardar_data(datos)  
    print("Usuario registrado exitosamente.")
    usuario_actual = nuevo_usuario
    return usuario_actual


def iniciar_sesion():
    datos = leer_data()

    if "usuarios" not in datos:
        print("No hay usuarios registrados.")
        return None

    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")

    for usuario in datos["usuarios"]:
        if usuario["email"] == email and usuario["password"] == password:
            usuario_actual=usuario
            return usuario_actual

    print("Usuario o contraseña incorrectos.")
    return None



def usuario_existente(email):
    datos = leer_data()
    if "usuarios" in datos:
        for usuario in datos["usuarios"]:
            if usuario["email"] == email:
                return True
    return False

def registrar_gasto(usuario):
        print("=============================================")
        print("         Registrar Nuevo Gasto               ")
        print("=============================================")
        print("     Ingrese la información del gasto:       ")
        print(" - Monto del gasto:")
        print(" - Categoría (ej. comida, transporte, entretenimiento, otros):")
        print(" - Descripción (opcional): ")
        print("Ingrese 'S' para guardar o 'C' para cancelar.")
        print("=============================================")
        print("")
        monto=float(input("Ingrese el monto del gasto"))
        categoia=input("En que categoria entra el gasto (Ej.)")
        descripcion=input("¿Desea agregar una descripcion? S/N").lower
        if descripcion =="S":
            descripcion=input("Agregue una descripcion corta del gasto")
        elif descripcion =="N":
            descripcion=("")
        else:
            print("Opcion no valida")
            descripcion=("")


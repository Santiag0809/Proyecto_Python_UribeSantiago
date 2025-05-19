import json
import datetime
from tabulate import tabulate


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
    datos = leer_data()  
    email = usuario["email"]  
    print("=============================================")
    print("         Registrar Nuevo Gasto               ")
    print("=============================================")
    monto = float(input("Ingrese el monto del gasto: "))
    categoria = input("En qué categoría entra el gasto (ej. comida, transporte, etc.): ")
    desea = input("¿Desea agregar una descripción? (S/N): ").strip().lower()
    if desea == "s":
        descripcion = input("Agregue una descripción corta del gasto: ")
    else:
        descripcion = ""


    nuevo_gasto = {
    "monto": monto,
    "categoria": categoria,
    "descripcion": descripcion,
    "fecha": str(datetime.date.today())  
}


    
    for user in datos["usuarios"]:
        if user["email"] == email:
            user["gastos"].append(nuevo_gasto)
            break
    
    guardar_data(datos)
    print("Gasto registrado cajasanmente.")

def listar_gastos(usuario):
    if "gastos" not in usuario or not usuario["gastos"]:
        print("No hay gastos registrados.")
        return

    print("=============================================")
    print("               Listar Gastos                 ")
    print("=============================================")
    print("Seleccione una opción para filtrar los gastos:")
    print("1. Ver todos los gastos")
    print("2. Filtrar por categoría")
    print("3. Filtrar por rango de fechas")
    print("4. Regresar al menú principal")
    print("=============================================")
    option = input("Ingrese una opción numérica: ")

    if option == "1":
        print("Gastos registrados hasta la fecha:")
        print(tabulate(usuario["gastos"], headers="keys", tablefmt="grid"))

    elif option == "2":
        categoria = input("Ingrese la categoría por la que desea filtrar: ")
        filtrados = [g for g in usuario["gastos"] if g["categoria"].lower() == categoria.lower()]
        if filtrados:
            print(f"Gastos en la categoría '{categoria}':")
            print(tabulate(filtrados, headers="keys", tablefmt="grid"))
        else:
            print("No hay gastos registrados en esta categoría.")

    elif option == "3":
        fecha_inicial = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
        fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ")
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_inicial, "%Y-%m-%d").date()
            fecha_fin = datetime.datetime.strptime(fecha_final, "%Y-%m-%d").date()
        except ValueError:
            print("Formato de fecha inválido. Usa el formato YYYY-MM-DD.")
            return

        filtrados = []
        for gasto in usuario["gastos"]:
            gasto_fecha = datetime.datetime.strptime(gasto["fecha"], "%Y-%m-%d").date()
            if fecha_inicio <= gasto_fecha <= fecha_fin:
                filtrados.append(gasto)

        if filtrados:
            print(f"Gastos entre {fecha_inicial} y {fecha_final}:")
            print(tabulate(filtrados, headers="keys", tablefmt="grid"))
        else:
            print("No hay gastos en ese rango de fechas.")

    elif option == "4":
        print("Regresando al menú principal...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

       
        

    

   

    
    

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
    email = usuario["email"]  
    datos = leer_data()
    usuario = usuario_existente(email)  

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
    print("Gasto registrado exitosamente.")

def listar_gastos(usuario):
    datos = leer_data()
    email = usuario["email"]

    usuario_actualizado = None
    for i in datos["usuarios"]:
        if i["email"] == email:
            usuario_actualizado = i
            break
    if not usuario_actualizado ["gastos"]:
        print("Lo siento amiguito, no hay gastos registrados")
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
        print(tabulate(usuario_actualizado["gastos"], headers="keys", tablefmt="grid"))
        return

    elif option == "2":
        categoria = input("Ingrese la categoría por la que desea filtrar: ")
        filtrados = [gastos_v for gastos_v in usuario_actualizado["gastos"] if gastos_v["categoria"].lower() == categoria.lower()]
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
        for gasto in usuario_actualizado["gastos"]:
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

def calcular_totales(usuario):
    email = usuario["email"]
    datos = leer_data()
    usuario_actualizado = None
    for u in datos["usuarios"]:
        if u["email"] == email:
            usuario_actualizado = u
            break
        if not usuario_actualizado ("gastos"):
            print("No hay gastos registrados.")
        return

    print("=============================================")
    print("         Calcular Total de Gastos")
    print("=============================================")
    print("1. Total general")
    print("2. Total por categoría")
    print("3. Regresar al menú principal")
    print("=============================================")

    opcion = input("Seleccione una opción: ")      

    if opcion == "1":
        total_general = sum(g["monto"] for g in usuario_actualizado["gastos"])
        print(f"Total general de gastos: ${total_general:.2f}")

    elif opcion == "2":
        categoria = input("Ingrese la categoría para calcular el total: ")
        total_categoria = sum(
            g["monto"] for g in usuario_actualizado["gastos"]
            if g["categoria"].lower() == categoria.lower()
        )
        print(f"Total de gastos en la categoría '{categoria}': ${total_categoria:.2f}")

    elif opcion == "3":
        print("Regresando al menú principal...")
    else:
        print("Opción inválida. Sellecione otra opción.")
        
def verTodosGastos():
    datos = leer_data() 
    listaGastos = datos["usuario"]["gastos"]
    print(tabulate(listaGastos, headers="keys", tablefmt="grid"))

def generar_Reporte():
    email="usuario"
    datos = leer_data()
    usuario_ac = None
    for i in datos["usuarios"]:
        if i["email"] == email:
            usuario_ac = i
            break
    if not usuario_ac ("gastos"):
        print("No hay gastos registrados.")
        return
    print("=============================================")
    print("         Generar Reporte de Gastos           ")
    print("=============================================")
    print("Seleccione el tipo de reporte:")
    print("1. Reporte diario")
    print("2. Reporte semanal")
    print("3. Reporte mensual")
    print("4. Ir al menú principal")
    print("=============================================")
    opcion = input("Ingrese una opción numérica: ")
    if opcion == "1":
        fecha_reporte = input("Ingrese la fecha en este formato (YYYY-MM-DD)  : ")
        try:
            fecha = datetime.datetime.strptime(fecha_reporte, "%Y-%m-%d").date()
        except ValueError:
            print("Formato de fecha inválido o erroneo. Usa el formato YYYY-MM-DD.")
            return
        reporte_diario = []
        for gasto in usuario_ac["gastos"]:
            gasto_fecha = datetime.datetime.strptime(gasto["fecha"], "%Y-%m-%d").date()
            if gasto_fecha == fecha:
                reporte_diario.append(gasto)
            print("Como desea ver el reporte?")
            print("1. En pantalla")
            print("2. Guardar en archivo")
            opcion_opcion = input("Ingrese una opción numérica: ")
            if opcion_opcion == "1":
                print("Reporte diario:")
                print(tabulate(reporte_diario, headers="keys", tablefmt="grid"))
            elif opcion_opcion == "2":
                with open("reporte_diario.txt", "w") as file:
                    file.write(tabulate(reporte_diario, headers="keys", tablefmt="grid"))
                print("Reporte guardado en 'reporte_diario.txt'")
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
                   

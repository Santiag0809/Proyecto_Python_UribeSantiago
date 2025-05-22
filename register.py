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
    
    fecha_diferente = input("Desea agregar una fecha diferente a la del dia de hoy? (S/N): ").strip().lower()

    if fecha_diferente == "s":
     fecha_input = input("Ingrese la fecha a añadir en este formato (YYYY-MM-DD): ")
     try:
        fecha = datetime.datetime.strptime(fecha_input, "%Y-%m-%d").date()
     except ValueError:
        print("El formato de fecha no es válido. Inténtelo de nuevo.")
        return
    else:
        fecha = datetime.date.today()
    
    nuevo_gasto = {
        "monto":monto,
        "categoria": categoria,
        "descripcion": descripcion,
        "fecha": str(fecha)
    }

    
    for user in datos["usuarios"]:
        if user["email"] == email:
            user["gastos"].append(nuevo_gasto)
            break

    guardar_data(datos)
    print("Gasto registrado cajasanmente.")

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
    retorno=True
    while True:
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

        elif option == "2":
            categoria = input("Ingrese la categoría por la que desea filtrar: ")
            filtrados = [
                g for g in usuario_actualizado["gastos"]
                if g["categoria"].lower() == categoria.lower()
            ]
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
                continue

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
            break  

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
    
    while True:
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
            break
        else:
            print("Opción inválida. Sellecione otra opción.")

def verTodosGastos():
    datos = leer_data() 
    listaGastos = datos["usuario"]["gastos"]
    print(tabulate(listaGastos, headers="keys", tablefmt="grid"))

def generar_Reporte(usuario):
    email = usuario["email"]
    datos = leer_data()
    usuario_ac = None

    for i in datos["usuarios"]:
        if i["email"] == email:
            usuario_ac = i
            break

    if not usuario_ac or "gastos" not in usuario_ac or not usuario_ac["gastos"]:
        print("Lo siento amiguito, no hay gastos registrados.")
        return

    while True:
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
            fecha_dia = datetime.date.today()
            gastos_dia = []

            for gastito in usuario_ac["gastos"]:
                fecha_ver = datetime.datetime.strptime(gastito["fecha"], "%Y-%m-%d").date()
                if fecha_ver == fecha_dia:
                    gastos_dia.append(gastito)

            if not gastos_dia:
                print("No has hecho ningún gasto el día de hoy, amiguito.")
                continue

            print("¿Cómo desea ver el reporte?")
            print("1. En pantalla")
            print("2. Guardar en archivo")
            opcion_opcion = input("Ingrese una opción numérica: ")

            if opcion_opcion == "1":
                print("Reporte diario:")
                print(tabulate(gastos_dia, headers="keys", tablefmt="grid"))

            elif opcion_opcion == "2":
                if "reportes" not in usuario_ac:
                    usuario_ac["reportes"] = {}

                usuario_ac["reportes"]["diario"] = {
                    "fecha": str(fecha_dia),
                    "gastos": gastos_dia
                }

                with open("data/content.json", "w") as carpetita:
                    json.dump(datos, carpetita, indent=4)

                print("Listo amiguito, hemos guardado tu reporte en content.json")

        elif opcion == "2":
            fecha_hoy = datetime.date.today()
            fecha_semana = fecha_hoy - datetime.timedelta(days=7)
            gastos_Semana = []

            for g in usuario_ac["gastos"]:
                ver = datetime.datetime.strptime(g["fecha"], "%Y-%m-%d").date()
                if fecha_semana <= ver <= fecha_hoy:
                    gastos_Semana.append(g)

            if not gastos_Semana:
                print("No hay gastos en los últimos 7 días.")
                continue

            print("¿Cómo desea ver el reporte?")
            print("1. En pantalla")
            print("2. Guardar en archivo")
            opci = input("Ingrese una opción numérica: ")

            if opci == "1":
                print("Reporte semanal: ")
                print(tabulate(gastos_Semana, headers="keys", tablefmt="grid"))

            elif opci == "2":
                if "reportes" not in usuario_ac:
                    usuario_ac["reportes"] = {}

                usuario_ac["reportes"]["semanal"] = {
                    "fecha": str(fecha_hoy),
                    "gastos": gastos_Semana
                }

                with open("data/content.json", "w") as archivo:
                    json.dump(datos, archivo, indent=4)

                print("Listo amiguito, tu reporte de la semana ha sido guardado en content.json")

        elif opcion == "3":
            today = datetime.date.today()
            fecha_mes = today - datetime.timedelta(days=30)
            gastos_mes = []

            for mes in usuario_ac["gastos"]:
                mostrar = datetime.datetime.strptime(mes["fecha"], "%Y-%m-%d").date()
                if fecha_mes <= mostrar <= today:
                    gastos_mes.append(mes)

            if not gastos_mes:
                print("No has hecho gastos en el último mes.")
                continue

            print("¿Cómo desea ver el reporte?")
            print("1. En pantalla")
            print("2. Guardar en archivo")
            opcitres = input("Ingrese una opción numérica: ")

            if opcitres == "1":
                print("Reporte mensual: ")
                print(tabulate(gastos_mes, headers="keys", tablefmt="grid"))

            elif opcitres == "2":
                if "reportes" not in usuario_ac:
                    usuario_ac["reportes"] = {}

                usuario_ac["reportes"]["mensual"] = {
                    "fecha": str(fecha_mes),
                    "gastos": gastos_mes
                }

                with open("data/content.json", "w") as carpetita:
                    json.dump(datos, carpetita, indent=4)

                print("Listo amigazos, tu reporte del mes se ha guardado correctamente en el archivo content.json")

        elif opcion == "4":
            print("Saliendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
                 
def borrar_actualizar(usuario):
    email = usuario["email"]
    datos = leer_data()
    usuario_a = None

    for i in datos["usuarios"]:
        if i["email"] == email:
            usuario_a = i
            break

    if not usuario_a or "gastos" not in usuario_a or not usuario_a["gastos"]:
        print("Lo siento amiguito, no hay gastos registrados.")
        return

    while True:
        print("\n=============================================")
        print("         Editar o Borrar un Gasto            ")
        print("=============================================")
        print("Gastos registrados:\n")
        gastos = usuario_a["gastos"]
        for idx, gasto in enumerate(gastos):
            print(f"{idx + 1}. {gasto['categoria']} - {gasto['monto']} - {gasto['fecha']} - {gasto['descripcion']}")

        print("\n0. Volver al menú anterior")
        opcion = input("\nSeleccione el número del gasto que desea editar o borrar: ")

        if opcion == "0":
            break

        try:
            opcion_int = int(opcion)
            if opcion_int < 1 or opcion_int > len(gastos):
                print("Opción fuera de rango. Intente nuevamente.")
                continue
        except ValueError:
            print("Debes ingresar un número entero válido.")
            continue

        index = opcion_int - 1
        gasto_seleccionado = gastos[index]

        print("\n¿Qué desea hacer con este gasto?")
        print("1. Editar")
        print("2. Borrar")
        accion = input("Ingrese una opción numérica: ")

        if accion == "1":
            print("\nIngrese los nuevos datos del gasto (deja en blanco para mantener el valor actual):")

            nueva_categoria = input(f"Categoría [{gasto_seleccionado['categoria']}]: ")
            nuevo_monto = input(f"Monto [{gasto_seleccionado['monto']}]: ")
            nueva_fecha = input(f"Fecha (YYYY-MM-DD) [{gasto_seleccionado['fecha']}]: ")
            nueva_descripcion = input(f"Descripción [{gasto_seleccionado['descripcion']}]: ")

            if nueva_categoria:
                gasto_seleccionado['categoria'] = nueva_categoria
            if nuevo_monto:
                try:
                    gasto_seleccionado['monto'] = float(nuevo_monto)
                except ValueError:
                    print("Monto inválido. No se actualizó.")
            if nueva_fecha:
                try:
                    datetime.datetime.strptime(nueva_fecha, "%Y-%m-%d")
                    gasto_seleccionado['fecha'] = nueva_fecha
                except ValueError:
                    print("Fecha inválida. No se actualizó.")
            if nueva_descripcion:
                gasto_seleccionado['descripcion'] = nueva_descripcion

            print("Gasto actualizado correctamente.")

        elif accion == "2":
            confirmacion = input("¿Está seguro de que desea borrar este gasto? (s/n): ")
            if confirmacion.lower() == "s":
                gastos.pop(index)
                print("Gasto eliminado con éxito.")
            else:
                print("Operación cancelada.")
        else:
            print("Opción inválida. Intente nuevamente.")
            continue

        with open("data/content.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print("Cambios guardados correctamente.")



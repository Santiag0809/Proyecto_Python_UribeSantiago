from register import registrar_usuario, usuario_existente, iniciar_sesion, registrar_gasto, listar_gastos

print("Bienvenido al sistema de registro de usuarios")
print("1. Registrar usuario")
print("2. Iniciar sesión")
opcion = input("Seleccione una opción (1 o 2): ")

usuario = None

if opcion == "1":
    usuario = registrar_usuario()

elif opcion == "2":
    usuario = iniciar_sesion()

if usuario:
    print(f"\n Sesión iniciada como {usuario['nombre']} ({usuario['email']})")
    
else:
    print(" No se pudo iniciar sesión o registrarse.")

print("")

while usuario:
    print("=============================================")
    print("         Simulador de Gasto Diario")
    print("=============================================")
    print("Seleccione una opción:\n")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        registrar_gasto(usuario)
    if opcion == "2":
        listar_gastos(usuario)
    if opcion == "3":
        print("Función de calcular total de gastos no implementada.")
    if opcion == "4":
        print("Función de generar reporte de gastos no implementada.")
    if opcion == "5":
        print("Estas seguro que desea salir? (S/N): ")
        salir = input().strip().lower()
        if salir == "s":
            print("Saliendo del sistema...")
            break
        else:
            print("Regresando al menú principal...")

        











    
   












    

    
# Simulador de Gasto Diario

El Simulador de Gasto Diario es una aplicación de consola diseñada para ayudar a los usuarios a registrar y monitorear sus gastos diarios en diferentes categorías, como comida, transporte, entretenimiento, entre otros.

Este simulador permite llevar un control básico de los gastos diarios, semanales o mensuales, y obtener un resumen o reporte de los gastos en cada categoría. Toda la información se guarda en un archivo JSON, lo que permite mantener un historial de gastos entre distintas sesiones del programa.

Muchos usuarios desean llevar un registro de sus gastos, pero las aplicaciones de gestión financiera completas pueden ser complicadas y requieren configuraciones avanzadas. Este proyecto ofrece una solución simple y accesible para aquellos que buscan hacer un seguimiento básico de sus gastos en un formato amigable y sin demasiadas complejidades. 

Con el Simulador de Gasto Diario, los usuarios pueden organizar sus gastos de forma práctica y recibir una visión clara de su situación financiera diaria, semanal o mensual.

---

## 🛠️ Tecnologías y Herramientas

- **Python 3**
- Librería `tabulate` para mostrar información en formato de tablas: https://pypi.org/project/tabulate/
- Módulo `datetime` para manejo de fechas
- `json` para almacenamiento de datos
- GitHub para gestión de versiones (con conventional commits)
- Recursos para el diseño de los menús: https://gist.github.com/programmersland/cf9362472f1b9f245415d9cee96c7aef

---

## 📂 Estructura del Proyecto
Proyecto_Python_UribeSantiago/
├── Main/
│ └── main.py
├── register/
│ └── register.py
├── data/
│ └── content.json
├── README.md

## Funciones principales del programa

### 🤑 Registro de gastos
- El usuario podra, una vez iniciado sesion o registrarse ingresar un nuevo gasto, su monto, su categoria y de forma opcional una breve descrión.
- Dicha informacion se almacenara en un archivo JSON junto con la informacion del usuario.

### 📜 Listado de gastos 
- El usuario podra escoger de que manera deseara visualizar sus datos.
- Mediante el uso de categorias fechas y o descripciones ademas de poder verlos todos a la vez.

### ☑ Calcular datos totales y/o por categoria 
- Calcula el total de gastos diarios, semanales o mensuales.
- Muestra el gasto acumulado por categoría.

### ❗❗❗ Generacion de reportes 
- Muestra un resumen de los gastos diarios, semanales o mensuales.
- El reporte puede visualizarse o guardarse en un archivo JSON.

### 🎦 Guardar y Cargar Datos 
- La aplicación carga automáticamente los datos del archivo JSON al iniciar.
- Guarda automáticamente los nuevos registros al cerrar o modificar la información.

### 🦾 / 🗑 Actualizar y o borrar datos 
- El usuario podra acceder a sus gastos ya guardados ademas de poder actualizarlos y o borrar .
- Dichos cambios quedaran guardados dentro de un archivo JSON.
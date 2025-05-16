import json
file="data/content.json"
def leer_data():
    with open (file,"r") as file:
        return json.load(file)
    
def guardar_data(listar_datos):
    with open (file,"w") as file:
        return json.dump(listar_datos,file,indent=4)


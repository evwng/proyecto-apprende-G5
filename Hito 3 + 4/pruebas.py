import json
taller_info = '''{
    "Tipo de Tallerista": "Matemáticas",
    "Insumos Requeridos": {
        "Lápices": 60,
        "Cuadernos": 30,
        "Borradores": 30,
        "Tilex": 10
    }
}'''

json_data = json.loads(taller_info)

print(json_data)


a="HOLA COMO ESTAS }JAJAJA" #i[-7]



import openai
import json
#from modelo_de_clases import *

openai.api_key = "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"

print("Nombra un taller:\n")
prompt_usuario = input()
print("\n")

#taller = Taller(prompt_usuario)
#ubicacion = taller.get_ubicacion(Taller)
ubicacion = ",Providencia--Chile,-33.4314474,-70.6093325,1.html"
formato = ""

prompt = "Genera un JSON con las indentaciones apropiadas a partir de la siguiente descripción de un taller. El diccionario debe contener la siguiente información:\n"
prompt += "\n"
prompt += "Tipo de Tallerista: [Tu descripción aquí en una sola palabra]\n"
prompt += "Insumos Requeridos:\n"
prompt += "[Insumo 1]: [Cantidad requerida como número entero],\n"
prompt += "[Insumo 2]: [Cantidad requerida como número entero],\n"
prompt += "[Insumo 3]: [Cantidad requerida como número entero],\n"
prompt += "...\n"
prompt += "\n"
prompt += "Por favor, proporciona una descripción del taller, incluyendo el tipo de tallerista y la lista de insumos necesarios con las cantidades correspondientes.\n"
prompt += prompt_usuario
prompt += "los insumos tienen que ser consumibles"

completion = openai.Completion.create(engine = "text-davinci-003", prompt = prompt, max_tokens = 2000)

print(completion.choices[0].text)

json_text=completion.choices[0].text
#print(json_text)

i=0
boolean=True
while boolean:
    if json_text[i]=="{":
        i2=i
        boolean=False
    i+=1
print(i2)
i=-1
boolean=True
while boolean:
    if json_text[i]=="}":
        i3=i
        boolean=False
    i-=1
print(i3)

i3 = len(json_text) + 1 + i3
#i3 = -1 -> i3 = largo + 1 - 1 = largo
#i3 = -2 -> i3 = largo + 1 - 2 = largo - 1

json_text=json_text[i2:i3+1]

print(json_text)
json_data = json.loads(json_text)

tipo_tallerista = json_data["Tipo de Tallerista"]

link = "https://www.superprof.cl/s/" + tipo_tallerista + ubicacion

print(link)

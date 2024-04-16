import openai
import json
import creds
from googlesearch import search 
def crear_link(prompt_usuario):

    lugar = "Providencia--Chile,-33.4314474,-70.6093325"

    #Colocar key de openai
    openai.api_key = creds.api_key

    prompt =  "Genera un JSON con las indentaciones apropiadas a partir de la siguiente descripción de un taller. El diccionario debe contener la siguiente información:\n"
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
    
    completion = openai.Completion.create(engine = "gpt-3.5-turbo-instruct", prompt = prompt, max_tokens = 2000)

    json_text=completion.choices[0].text

    i=0
    boolean=True
    while boolean:
        if json_text[i]=="{":
            i2=i
            boolean=False
        i+=1
    i=-1
    boolean=True
    while boolean:
        if json_text[i]=="}":
            i3=i
            boolean=False
        i-=1
    i3 = len(json_text) + 1 + i3

    json_text=json_text[i2:i3+1]

    json_data = json.loads(json_text)

    tipo_tallerista = list(json_data.values())[0]
    
    lista_insumos=[]
    insumos=list(json_data.values())[1:]
    for key in insumos[0]:
        query="comprar "
        query+=key
        query+=" online"

        for link_insumo in search(query, tld="co.in", num=1, stop=1, pause=2): 
            lista_insumos.append((key,link_insumo))

    link = "https://www.superprof.cl/s/" + tipo_tallerista + "," + lugar + ",1.html"

    return link, lista_insumos
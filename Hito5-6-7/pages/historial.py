import streamlit as st
import requests

st.set_page_config(page_title = "Historial", layout = "wide")
st.title = "Historial"

with st.container():
    st.header("HISTORIAL DE BÚSQUEDA")

with st.container():

    id_busqueda = st.text_input("Ingrese el ID de la búsqueda que desea revivir (opcional):", "")

    if st.button("Realizar búsqueda"):
        
        respuesta = requests.get("http://127.0.0.1:8000/busquedas")

        historial = respuesta.json()

        #NO SE INGRESA ID DE BÚSQUEDA -> SE MUESTRA HISTORIAL COMPLETO
        if not id_busqueda:
            for busqueda in reversed(historial):
                with st.expander(f"Búsqueda {busqueda['id']} - Prompt: {busqueda['prompt']}"):
                    st.write("Resultados:")
                    resultados = busqueda["resultados"]
                    if resultados:
                        st.dataframe(resultados,
                                     column_config = {"nombre": "Nombre",
                                                      "precio": "Precio",
                                                      "valoracion": "Valoración",
                                                      "valoracion_cantidad": "Cantidad de valoraciones",
                                                      "contacto": "Contacto",
                                                      "fuente": None,
                                                      "id": None,
                                                      "id_busqueda": None,
                         })
                    else:
                        st.write("No se encontraron resultados para esta búsqueda.")
        
        #SE INGRESA ID DE BÚSQUEDA -> SE MUESTRA RESULTADOS DE DICHA BÚSQUEDA
        else:

            respuesta = requests.get("http://127.0.0.1:8000/busqueda/" + id_busqueda)

            st.write("Respuesta de la búsqueda:")

            if respuesta.status_code == 200:
                resultados = respuesta.json()["resultados"]
                if resultados:
                    st.dataframe(resultados,
                                 column_config = {"nombre": "Nombre",
                                                 "precio": "Precio",
                                                 "valoracion": "Valoración",
                                                 "valoracion_cantidad": "Cantidad de valoraciones",
                                                 "contacto": "Contacto",
                                                 "fuente": None,
                                                 "id": None,
                                                 "id_busqueda": None,
                                })
                else:
                    st.write("No se encontraron resultados para esta búsqueda.")
            elif respuesta.status_code == 400:
                st.write("No se encontraron resultados para la búsqueda con el ID ingresado.")
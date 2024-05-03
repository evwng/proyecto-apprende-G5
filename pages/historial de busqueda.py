import streamlit as st
import requests

st.set_page_config(page_title = "Historial de búsqueda",
                   layout = "wide")

st.title = "Historial de búsqueda"

with st.container():
    
    st.header("HISTORIAL DE BÚSQUEDA")

with st.container():

    id_busqueda = st.text_input("Ingrese el ID de la búsqueda que desea revivir (opcional):", "")

    if st.button("Realizar búsqueda"):

        #NO SE INGRESA ID DE BÚSQUEDA -> SE MUESTRA HISTORIAL COMPLETO
        if not id_busqueda:
            respuesta = requests.get("http://127.0.0.1:8000/busquedas")
            historial = respuesta.json()
            for busqueda in reversed(historial):
                with st.expander(f"ID de la búsqueda: {busqueda['id']} - Prompt: {busqueda['prompt']}"):
                    st.write("Resultados:")
                    resultados = busqueda["resultados_talleristas"]
                    if resultados:
                        st.dataframe(resultados,
                                     column_config = {"nombre": "Nombre",
                                                      "precio": "Precio",
                                                      "valoracion": "Valoración",
                                                      "valoracion_cantidad": "Cantidad de valoraciones",
                                                      "contacto_estado": "Estado del proceso de contacto",
                                                      "contacto": st.column_config.LinkColumn("Contacto",
                                                                                              help = "Página de contacto (Doble click para acceder)",
                                                                                              width = 1000),
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
                resultados = respuesta.json()["resultados_talleristas"]
                if resultados:
                    st.dataframe(resultados,
                                 column_config = {"nombre": "Nombre",
                                                 "precio": "Precio",
                                                 "valoracion": "Valoración",
                                                 "valoracion_cantidad": "Cantidad de valoraciones",
                                                 "contacto_estado": "Estado del proceso de contacto",
                                                 "contacto": st.column_config.LinkColumn("Contacto",
                                                                                         help = "Página de contacto (Doble click para acceder)",
                                                                                         width = 1000),
                                                 "fuente": None,
                                                 "id": None,
                                                 "id_busqueda": None,
                                })
                else:
                    st.write("No se encontraron resultados para esta búsqueda.")
            elif respuesta.status_code == 400:
                st.write("No se encontró la búsqueda con el ID ingresado.")
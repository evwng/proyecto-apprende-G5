import streamlit as st
import json
import requests

def main():

    st.set_page_config(page_title="Proyecto Apprende", layout="wide")

    with st.container():
        st.header("BÚSQUEDA DE TALLERISTAS")

    with st.container():
        termino_busqueda = st.text_input("Ingrese la búsqueda:", "")
    
    if st.button("Realizar búsqueda"):
        
        datos_formulario = {"prompt": termino_busqueda}
        
        respuesta = requests.post("http://127.0.0.1:8000/busqueda", data = json.dumps(datos_formulario))

        st.write("Respuesta de la búsqueda:")

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
            st.write("No se encontraron resultados.")

    with st.container():
        st.write("PROYECTO APPRENDE")
        st.write("Grupo 8:")
        st.markdown("- Néstor Guajardo Carrizo - 202173132-6")
        st.markdown("- Pablo Guzmán Castro - 202173011-7")
        st.markdown("- Eva Wang Liu - 202111004-6")
        st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            list-style-position: inside;
        }
        </style>
        ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
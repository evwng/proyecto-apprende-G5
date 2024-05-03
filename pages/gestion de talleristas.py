import streamlit as st
import requests

st.set_page_config(page_title = "Gestión de talleristas",
                   layout = "wide")

st.title = "Gestión de talleristas"

with st.container():
    
    st.header("GESTIÓN DE TALLERISTAS")

with st.container():

    st.subheader("CAMBIAR ESTADO DEL PROCESO DE CONTACTO CON UN TALLERISTA")

    busquedas = requests.get("http://127.0.0.1:8000/busquedas").json()

    if (len(busquedas) > 0):

        opcion_busqueda = st.selectbox("Elige una búsqueda:",
                                    busquedas,
                                    format_func = lambda x: "Búsqueda: " + x["prompt"])

        opcion_tallerista = st.selectbox("Elige un tallerista:",
                                        opcion_busqueda["resultados_talleristas"],
                                        format_func = lambda x: "Nombre: " + x["nombre"] + ", Estado del contacto: " + x["contacto_estado"])
        
        opcion_contacto_estado = st.selectbox("Elige un estado del proceso de contacto:",
                                            ["Sin contactar", "Contactado y no validado", "Contactado y validado"])
        
        if st.button("Cambiar"):

            request = requests.put("http://127.0.0.1:8000/tallerista/" + opcion_tallerista["id"] + "/" + opcion_contacto_estado)

            if request:
                st.text("¡Estado del proceso de contacto cambiado con éxito!")
            else:
                st.text("Ha ocurrido un error")